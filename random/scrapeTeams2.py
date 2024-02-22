import pandas as pd
from bs4 import BeautifulSoup

# Load the HTML content
with open('./data/raw_teams.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all instances of tables with the class "table-striped"
tables = soup.find_all('table', class_='table-striped')

# Ensure there is a second instance
if len(tables) < 2:
    raise ValueError("The second instance of 'table-striped' class table does not exist.")
else:
    table = tables[1]  # Select the second instance

# Extract the table headers, skipping the first header row as it is a category header
headers = [header.get('original-title', header.text).strip() for header in table.find_all('th')[1:]]

# Extract rows, starting from the second row to skip the header row
rows = []
for row in table.find_all('tr')[1:]:  # skipping the first row which is the header
    cols = row.find_all('td')
    if cols:
        rows.append([col.text.strip() for col in cols])

# Create a DataFrame and save to CSV
df = pd.DataFrame(rows, columns=headers)
csv_path = './data/teams2.csv'
df.to_csv(csv_path, index=False)

print('Data saved to teams.csv.')
