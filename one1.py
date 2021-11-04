import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.webometrics.info/en/africa/uganda')

soup = BeautifulSoup(page.text, 'html.parser')

with open('uniRanking.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['RANKING', 'WORLD RANKINNG','UNI NAMES', 'IMPACT RANK', 'OPENNES RANK'])

    u_table = soup.find('table', class_ = 'sticky-enabled')
#print(u_table)

    for names in u_table.find_all('tbody'):
        rows = names.find_all('tr')
        for row in rows:
            rank = row.find_all('td')[0].get_text()
            w_rank = row.find_all('td')[1].get_text()
            uni_name = row.find_all('td')[2].get_text()
            i_rank = row.find_all('td')[4].get_text()
            op_rank = row.find_all('td')[5].get_text()
                    
            #print(rank, w_rank, uni_name, i_rank, op_rank)
            w.writerow([rank,w_rank,uni_name,i_rank,op_rank])

print('Ranking Recorded')
