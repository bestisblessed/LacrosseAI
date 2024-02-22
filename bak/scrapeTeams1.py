import pandas as pd
from bs4 import BeautifulSoup

# Load the HTML content
with open('./data/raw_teams.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the specific table in the HTML based on the screenshot provided
# Assuming the class "table-striped" is unique to this table
table = soup.find('table', class_='table-striped')

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
csv_path = './data/teams.csv'
df.to_csv(csv_path, index=False)

print('Data saved to games.csv.')


# import pandas as pd
# from bs4 import BeautifulSoup

# # Load the HTML content
# with open('./data/raw_teams.html', 'r') as file:
#     html_content = file.read()

# # Parse the HTML
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find the table in the HTML
# table = soup.find('table')

# # Extract the table headers
# headers = [header.text.strip() for header in table.find_all('th')]

# # Extract rows
# rows = []
# for row in table.find_all('tr'):
#     cols = row.find_all('td')
#     if cols:
#         rows.append([col.text.strip() for col in cols])

# # Create a DataFrame and save to CSV
# df = pd.DataFrame(rows, columns=headers)
# df.to_csv('./data/teams.csv', index=False)

# print('Data saved to teams.csv.')
