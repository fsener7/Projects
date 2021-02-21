# import libraries
import requests
import pandas as pd
import csv
import urllib
from bs4 import BeautifulSoup

vendors=["Rockwell Automation"]
for query in vendors:
    url = "https://www.cvedetails.com/vendor-search.php?search="+query
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    vendor_table = soup.find("table", attrs={"class": "listtable"})
    vendor = []
    for a in vendor_table.find_all('a', href=True): 
        if a.text: 
            vendor.append(a['href'])
    print(vendor[0])
    url2 = "https://www.cvedetails.com/vendor-search.php?search="+vendor[0]
    html_content = requests.get(url2).text
    soup2 = BeautifulSoup(html_content, "lxml")
    pro_table = soup2.find("table", id="maintable")
    prolink = []
    for a in pro_table.find_all('a', href=True): 
        if a.text: 
            print(a['href'])
    print(prolink[0])
    