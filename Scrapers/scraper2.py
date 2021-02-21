# import libraries
import requests
import pandas as pd
import csv
import urllib
from bs4 import BeautifulSoup
url = "https://www.cvedetails.com/vulnerability-list/vendor_id-11651/Schneider-electric.html"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
vuln_table = soup.find("table", attrs={"class": "searchresults"})
vuln_table_data = vuln_table.find_all("tr")

cveids = []
descriptions = []
pubdates = []
updates = []
scores = []
accesses = []


for row in vuln_table_data:
    entries = row.find_all('td')
    if len(entries) > 6 and entries[6].string is not None:
        cveids.append(entries[1].text)
        pubdates.append(entries[5].text)
        updates.append(entries[6].text)
        scores.append(entries[7].text)
        accesses.append(entries[9].text)

for i in range(50):
    print(cveids[i]+" - " + str(descriptions[i])+" - " + pubdates[i]+" - " +
          updates[i]+" - " + scores[i]+" - " + accesses[i])

