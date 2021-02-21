import re
import urllib.request as ur
text = input('What do you want to search? : ')
search_string = text.split(' ')
search_string = '+'.join(search_string)
googlesearch = 'https://www.bing.com/search?q=' + search_string
source = ur.urlopen(googlesearch)
source = source.read()
source = str(source)
output = re.findall(r'''(?:http://|www.)[^"]+''', source)
for i in range(len(output)):
    print(output[i])
