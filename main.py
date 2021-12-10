from bs4 import BeautifulSoup
import requests
import csv
import re

stockList = []
with open('swiat.csv', newline='', encoding='utf-8-sig') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    for row in spamreader:
        try:

            row = "".join(row)
            stockList.append(row)
            page = requests.get(row)
            data = page.text
            soup = BeautifulSoup(data, 'html.parser')
            p = soup.find('span', {'class': 'price'})
            for tag in soup.find_all('span', string=re.compile(r'EAN')):
                # print(tag.parent.text)
                print(p.text, tag.parent.text, row)

            rows = [p.text, tag.parent.text, row]

            # zapis do csv

            with open('wynik.csv', 'a', newline='', encoding="utf-8") as csvFile:
                writer = csv.writer(csvFile, delimiter=";")
                writer.writerow(rows)

                csvFile.close()

        except:
            pass

"""
















"""
