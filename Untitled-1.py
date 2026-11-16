import requests
from bs4 import BeautifulSoup

def print_secret_message(doc_url):
    # Get the doc's HTML content
    response = requests.get(doc_url)
    html = response.text

    # Parse the HTML to find the table
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')

    characters = []  # will store (x, y, char) for each entry
    max_x = 0
    max_y = 0

    # Skip the first row since it's just the header (x-coordinate, Character, y-coordinate)
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) < 3:
            continue

        x = int(cols[0].get_text().strip())
        char = cols[1].get_text().strip()
        y = int(cols[2].get_text().strip())

        characters.append((x, y, char))

        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    # Build an empty grid filled with spaces
    grid = []
    for row_num in range(max_y + 1):
        new_row = []
        for col_num in range(max_x + 1):
            new_row.append(' ')
        grid.append(new_row)

    # Place each character in its correct spot
    # IMPORTANT: grid is indexed as grid[y][x], not grid[x][y]
    for x, y, char in characters:
        grid[y][x] = char

    # Print starting from the LARGEST y first, down to 0
    # Because y = 0 is the BOTTOM row, not the top row
    for row_num in range(max_y, -1, -1):
        line = ""
        for char in grid[row_num]:
            line = line + char
        print(line)


# Example usage:
print_secret_message(" https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")
