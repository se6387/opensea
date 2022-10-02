import lxml.html

def extractLinksLxml(text):
    lists = []
    dom = lxml.html.fromstring(text)
    for list in dom.xpath('//a/@href'):
        lists.append(list)
    
    return lists
