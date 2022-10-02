from selectolax.parser import HTMLParser

#text represent the html mark-up
def extractLinksHtmlParser(text):
    lists = []
    dom = HTMLParser(text)
    
    for tag in dom.tags('a'):
        attrs = tag.attributes

        if 'href' in attrs:
            lists.append(attrs['href'])

    return lists
