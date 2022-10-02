from operator import truediv
from urllib import response
import requests
import beautiful_soup_parser


def printListWithFilter(list, filter):
    for l in list:
        if inFilter(l, filter):
            print('level : ', l)

def inFilter(l, filter):
    r = False
    for f in filter:
        if f in l:
            r = True
            break
    
    return r

# if we want the urls contained with in the pages referred
# by those filtering values then we need to get each of those
# individual urls and parse the content of those pages
def followList(list, filter, parse=False):
    for l in list:
        if inFilter(l, filter):
            print('level one : ', l)

            if parse == False:
                response = requests.get(l)
                filteredResponse = beautiful_soup_parser.extractLinksBeautifulSoup(response.text)

                i = 0
                for fl in filteredResponse:
                    print('level two .. ', fl)
                    i = i + 1

                    if i > 10:
                        print('')
                        break
