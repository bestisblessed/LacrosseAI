import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

current_date = datetime.now().strftime("%m-%d")
html_file_name = f'./data/page_source_{current_date}.html'
with open(html_file_name, 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')
headers = [header.text.strip() for header in table.find_all('th')]
rows = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    if cols:
        rows.append([col.text.strip() for col in cols])

df = pd.DataFrame(rows, columns=headers)
csv_file_name = f'./data/schedule_{current_date}.csv'
df.to_csv(csv_file_name, index=False)
print(f'Data saved to {csv_file_name}.')

