import pandas as pd
from bs4 import BeautifulSoup

with open('./data/page_source.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

tables = soup.find_all('table')

if len(tables) > 1:
    next_day_table = tables[1]
else:
    next_day_table = None

if next_day_table:
    headers = [header.text.strip() for header in next_day_table.find_all('th')]
    rows = []
    for row in next_day_table.find_all('tr'):
        cols = row.find_all('td')
        if cols:
            rows.append([col.text.strip() for col in cols])
    df_next_day = pd.DataFrame(rows, columns=headers)

df_next_day.to_csv('./data/next_days_games.csv', index=False)

