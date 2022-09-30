import requests
import re

def extractLinkRegEx(txt):
    tgs = re.compile(r'<a[^<>]+?href=([\'\"])(.?*)\1', re.IGNORECASE)
    return [match[1] for match in tgs.findall(txt)]

# opensea.io
# edfreitas.me
# https://quotes.toscrape.com/

r = requests.get('https://quotes.toscrape.com/') 
print(extractLinkRegEx(r.text))
