import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.webometrics.info/en/africa/uganda')
print(page)

soup = BeautifulSoup(page.content, 'html.parser')

with open('uniNames.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['UNI NAMES'])

    repos = soup.find_all("div", {"class":"content"})

    names = soup.find_all("tr",{"class":["odd", "even"] })

    for name in names:

        uni_name = name.find('a')
        
    #print(uni_name)
                 
        w.writerow([uni_name.text])
    
    
    print('University Names Recorded')