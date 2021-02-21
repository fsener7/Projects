import requests
import re
import urllib
import csv
from bs4 import BeautifulSoup
import xlrd
import pandas as pd


cveids = []
descriptions = []
pubdates = []
cvss2 = []
cvss3 = []
df = pd.read_excel('Products.xlsx')
product_list = df['Product_Name'].tolist()
print("Searching...")
header_added = False
product_list=["SIMATIC S7-1200","SIMATIC S7-1500"]
for query in product_list:
    url = "https://nvd.nist.gov/vuln/search/results?query="+query+"&results_type=overview&form_type=Basic&search_type=all&startIndex=0"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    vuln_table = soup.find("table", attrs={"class": "table"})
    vuln_table_data = vuln_table.tbody.find_all("tr")

    for i in vuln_table_data:
        cveids.append(i.find('th'))
        descriptions.append(i.find('p'))
        pubdates.append(i.find('span'))
    cvss3list = ["cvss3-link", "Cvss3NAText"]
    for cv3 in cvss3list:
        for x in vuln_table.find_all("span", id=cv3):
            cvss3.append(x)
    for x in vuln_table.find_all("span", attrs={"id": "cvss2-link"}):
        cvss2.append(x)

    """print(str(len(cveids))+"Product :"+ query)

    print("--")
    print(len(vuln_table_data))
    for i in range(len(vuln_table_data)):
        if descriptions[i] and cveids[i] and pubdates[i] and cvss2[i] and cvss3[i] is not None:
                print(cveids[i].get_text() + " -- " +descriptions[i].string + " -- " + pubdates[i].get_text() + " -- "+cvss2[i].get_text() + " -- "+cvss3[i].get_text() + " \n")
    """

for i in cveids:
    print(i.get_text())
print(len(cveids))