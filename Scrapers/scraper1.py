import requests
import re
import urllib
import csv
from bs4 import BeautifulSoup

print("Searching...")


def vulnerables(query, endindex, csvname):
    header_added = False
    for index in range(0, endindex, 20):
        query = query
        url = "https://nvd.nist.gov/vuln/search/results?query="+query + \
            "&results_type=overview&form_type=Basic&search_type=all&startIndex=" + \
            str(index)
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        vuln_table = soup.find("table", attrs={"class": "table"})
        vuln_table_data = vuln_table.tbody.find_all("tr")
        cveids = []
        descriptions = []
        pubdates = []
        cvss2 = []
        cvss3 = []

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
        headcount = 0
        with open(csvname, mode='a', newline='', encoding='utf-8') as csv_file:
            headers = ['CVEID', 'Description',
                       'Publish_Date', 'CVSS2', 'CVSS3']
            writer = csv.writer(csv_file, delimiter=',',
                                quoting=csv.QUOTE_ALL, quotechar='\"')
            if not header_added:
                writer.writerow(headers)
                header_added = True
            for i in range(len(cveids)):
                if descriptions[i] and cveids[i] and pubdates[i] and cvss2[i] and cvss3[i] is not None:
                    writer.writerow([cveids[i].get_text().strip(),
                                     descriptions[i].get_text().strip(), pubdates[i].get_text().strip(), cvss2[i].get_text().strip(),  cvss3[i].get_text().strip()])
                    print(cveids[i].get_text() + " -- " +
                          descriptions[i].string + " -- " + pubdates[i].get_text() + " -- "+cvss2[i].get_text() + " -- "+cvss3[i].get_text() + " \n")
            headcount = headcount+1


vulnerables("plc", 180, 'plcvulns.csv')
