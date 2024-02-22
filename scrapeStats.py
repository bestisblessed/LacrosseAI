import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

file_names = [
    'statsTopScorers.csv',
    'statsAssistLeaders.csv',
    'statsGoalLeaders.csv',
    'statsPointsPerGameLeaders.csv',
    'statsTeamGoalsPerGame.csv',
    'statsTeamGoalsAgainstAvg.csv'
]

current_date = datetime.now().strftime("%m-%d")
with open(f'./data/raw_stats_{current_date}.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
tables = soup.find_all('table', class_='table-striped')

for table, file_name in zip(tables, file_names):
    headers = [header.get('original-title', header.text).strip() for header in table.find_all('th')[1:]]
    rows = []
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if cols:
            rows.append([col.text.strip() for col in cols])
    
    df = pd.DataFrame(rows, columns=headers)
    csv_path = f'./data/{file_name[:-4]}_{current_date}.csv'
    df.to_csv(csv_path, index=False)
    print(f'Data saved to {csv_path}.')

