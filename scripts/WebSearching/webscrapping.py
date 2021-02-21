import requests
import bs4
import sys
import webbrowser
userinput = input("What do you want to search? : ")
print("Googling...")
response = requests.get(
    "https://www.google.com/search?q=" + userinput)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'lxml')


def isAnchorTagWithLargeText(tag):
    return True if tag.name == 'a' and len(tag.get_text()) > 50 else False


tags = soup.find_all(isAnchorTagWithLargeText, limit=10)
for tag in tags:
    print(tag.get_text(separator=" "))
