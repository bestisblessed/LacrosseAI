import pandas as pd
from bs4 import BeautifulSoup

# Load the HTML content
with open('./data/page_source.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table in the HTML - adjust this if you have more than one table or a specific table id/class
table = soup.find('table')

# Extract the table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract rows
rows = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    if cols:
        rows.append([col.text.strip() for col in cols])

# Create a DataFrame and save to CSV
df = pd.DataFrame(rows, columns=headers)
df.to_csv('./data/games.csv', index=False)

print('Data saved to games.csv.')


# from bs4 import BeautifulSoup
# import csv
# import os

# # Read the HTML content from the file
# file_path = 'page_source.html'
# with open(file_path, 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find the table by looking for the 'table' tag with class 'table' and 'table-striped'
# # (based on the structure identified in the provided HTML snippet)
# table = soup.find('table', {'class': ['table', 'table-striped']})

# # Extract the headers from the 'thead' part of the table
# headers = [header.get_text(strip=True) for header in table.find('thead').find_all('th')]

# # Initialize a list to hold all row data
# data = []

# # Extract each row of the table, ignoring the first one since it's the header
# for row in table.find('tbody').find_all('tr'):
#     cols = row.find_all('td')
#     cols_data = []
#     for col in cols:
#         # Extract text directly if it's a text column, otherwise extract the link
#         if col.find('a'):
#             cols_data.append(col.find('a')['href'])
#         else:
#             cols_data.append(col.get_text(strip=True))
#     data.append(cols_data)

# # Define the CSV file path
# csv_file_path = 'games.csv'

# # Write the data to a CSV file
# with open(csv_file_path, mode='w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     writer.writerows(data)

# # Return the path of the CSV file
# csv_file_path
