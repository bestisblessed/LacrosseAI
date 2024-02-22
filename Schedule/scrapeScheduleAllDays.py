import pandas as pd
from bs4 import BeautifulSoup

with open('./data/page_source.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
tables = soup.find_all('table')

all_days_games = []

for table in tables:
    headers = [header.text.strip() for header in table.find_all('th')]
    rows = []
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        if cols:
            rows.append([col.text.strip() for col in cols])
    if rows:
        all_days_games.extend(rows)

df = pd.DataFrame(all_days_games, columns=headers)
df.to_csv('./data/all_days_games.csv', index=False)

print('All days games saved to all_days_games.csv.')

