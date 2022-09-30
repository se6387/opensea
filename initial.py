import requests
import re
import lxml.html

def extractLinkRegEx(txt):
    tgs = re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1', re.IGNORECASE)
    return [match[1] for match in tgs.findall(txt)]

# use lxml parser
def extractLinkslLxml(text):
    lists = []
    dom = lxml.html.fromstring(text)
    for list in dom.xpath('//a/@href'):
        lists.append(list)
    
    return lists

# print line by line
def printList(lists):
    for list in lists:
        print ('Level 1 -> ' + list)

# opensea.io
# edfreitas.me
# https://quotes.toscrape.com/

r = requests.get('https://opensea.io') 
printList(extractLinkRegEx(r.text))

#
print('')
printList(extractLinkslLxml(r.text))
