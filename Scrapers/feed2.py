import feedparser
from datetime import datetime
vulnerables = feedparser.parse(
    "https://us-cert.cisa.gov/ics/alerts/alerts.xml")
vulnerable_list = []
for i in vulnerables.entries:
    vulnerable = {
        'title': i.title,
        'link': i.link,
        'summary': i.summary,
        'published': i.updated
    }
    vulnerable_list.append(vulnerable)
print('Finished scraping the vulnerables')
print(vulnerable_list[0])
