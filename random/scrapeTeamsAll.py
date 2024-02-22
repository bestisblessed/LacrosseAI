import pandas as pd
from bs4 import BeautifulSoup

file_names = [
    "teamsStandings.csv",
    'teamsACC.csv',
    'teamsAmericaEast.csv',
    'teamsASUN.csv',
    'teamsAtlantic10.csv',
    'teamsBigEast.csv',
    'teamsBigTen.csv',
    'teamsCAA.csv',
    'teamsDIIndependent.csv',
    'teamsIvyLeague.csv',
    'teamsMAAC.csv',
    'teamsPatriot.csv'
]


# # Load the HTML content
# with open('./data/raw_teams.html', 'r') as file:
#     html_content = file.read()

# # Parse the HTML
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all instances of tables with the class "table-striped"
# tables = soup.find_all('table', class_='table-striped')

# all_dfs = []  # List to hold all DataFrames created from each table

# for table_index, table in enumerate(tables, start=1):
#     # Extract the table headers, skipping the first header row as it is a category header
#     headers = [header.get('original-title', header.text).strip() for header in table.find_all('th')[1:]]

#     # Extract rows, starting from the second row to skip the header row
#     rows = []
#     for row in table.find_all('tr')[1:]:  # skipping the first row which is the header
#         cols = row.find_all('td')
#         if cols:
#             rows.append([col.text.strip() for col in cols])

#     # Create a DataFrame for the current table
#     df = pd.DataFrame(rows, columns=headers)
#     all_dfs.append(df)

#     # Optional: Save each table to a separate CSV file
#     csv_path = f'./data/teams{table_index}.csv'
#     df.to_csv(csv_path, index=False)
#     print(f'Data saved to {csv_path}.')

# Optional: Combine all DataFrames into a single DataFrame if needed
# combined_df = pd.concat(all_dfs, ignore_index=True)

# Load the HTML content
with open('./data/raw_teams.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all instances of tables with the class "table-striped"
tables = soup.find_all('table', class_='table-striped')

for table, file_name in zip(tables, file_names):
    # Extract the table headers, skipping the first header row as it is a category header
    headers = [header.get('original-title', header.text).strip() for header in table.find_all('th')[1:]]

    # Extract rows, starting from the second row to skip the header row
    rows = []
    for row in table.find_all('tr')[1:]:  # Skipping the first row which is the header
        cols = row.find_all('td')
        if cols:
            rows.append([col.text.strip() for col in cols])

    # Create a DataFrame for the current table
    df = pd.DataFrame(rows, columns=headers)

    # Save each table to a separate CSV file using names from the file_names list
    csv_path = f'./data/{file_name}'
    df.to_csv(csv_path, index=False)
    print(f'Data saved to {csv_path}')
