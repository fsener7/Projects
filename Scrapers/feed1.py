import feedparser
from datetime import datetime
vulnerables = feedparser.parse(
    "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml")
vulnerable_list = []
for i in vulnerables.entries:
    published = datetime.strptime(i.updated, "%Y-%m-%dT%H:%M:%SZ")
    vulnerable = {
        'title': i.title,
        'link': i.link,
        'summary': i.summary,
        'published': published
    }
    vulnerable_list.append(vulnerable)
print('Finished scraping the vulnerables')
print(vulnerable_list[0])
