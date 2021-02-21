from datetime import datetime
from numpy.lib.function_base import append
import requests
from bs4 import BeautifulSoup
import pandas as pd
from dateutil import parser
import csv
cveids = []
descriptions = []
pubdates = []
cvss2 = []
cvss3 = []

def checkIndex(url,Index):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    rows = soup.find("div", attrs={"class": "col-sm-12 col-lg-3"})
    strongs = rows.find("strong")
    results=int(strongs.get_text()) 
    if results>20:
        Index=Index+20
    else:
        return   
    return Index

def Get_Vulns(query,Index):
    url = "https://nvd.nist.gov/vuln/search/results?query="+query+"&results_type=overview&form_type=Basic&search_type=all&startIndex="+str(Index)
    Index=checkIndex(url,Index)
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    vuln_table = soup.find("table", attrs={"class": "table"})
    vuln_table_data = vuln_table.tbody.find_all("tr")

    for i in vuln_table_data:
        cveids.append(i.find('th').text.strip())
        descriptions.append(i.find('p').text.strip())
        pubdates.append(parser.parse(i.find('span').text.strip()))
    cvss3list = ["cvss3-link", "Cvss3NAText"]
    for cv3 in cvss3list:
        for x in vuln_table.find_all("span", id=cv3):
            cv3_words=(x.text.strip()).split()
            cvss3.append(cv3_words[1])
    cvss2list = ["cvss2-link", "Cvss2NAText"]
    for cv2 in cvss2list:
        for x in vuln_table.find_all("span", id=cv2):
            cv2_words=(x.text.strip()).split()
            cvss2.append(cv2_words[1])
    if Index == 20:
        Get_Vulns(query,Index)
    print("Veriler çekiliyor..")

    
def List_Vulns():
    print("Searching...")
    Index=0
    df = pd.read_excel('Products.xlsx')
    product_list = df['Product_Name'].tolist()
    for query in product_list:
        print(query)
        Get_Vulns(query,Index)
    #cveid ye göre aynı olanları silmem lazım
    """vulns=[]
    for cveid,desc,pub,cv2,cv3 in zip(cveids,descriptions,pubdates,cvss2,cvss3):
        vuln={'cveid':cveid, 'desc':desc,'pub':str(pub),'cv2':cv2,'cv3':cv3}
        vulns.append(vuln)"""
    header_added = False
    print(len(cveids))
    print(len(cvss3))
    with open("Vulnerabilitys.csv", mode='a', newline='', encoding='utf-8') as csv_file:
        headers = ['CVEID', 'Description','Publish_Date', 'CVSS2', 'CVSS3']
        writer = csv.writer(csv_file, delimiter='|',quoting=csv.QUOTE_NONE,escapechar='"')
        if not header_added:
            writer.writerow(headers)
            header_added = True
        for i in range(len(cveids)):
            if descriptions[i] and cveids[i] and pubdates[i] and cvss2[i] and cvss3[i] is not None:
                writer.writerow([cveids[i], descriptions[i], pubdates[i], cvss2[i],  cvss3[i]])
                print(cveids[i]+" \n")
List_Vulns()