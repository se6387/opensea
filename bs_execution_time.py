from pickle import TRUE
from bs4 import BeautifulSoup
import timeit

def executionTime():
    tcode = '''
def extractLinksBeautifulSoup(text):
    lists = []
    initBS = BeautifulSoup(text, 'lxml')

    for tag in initBS.find_all('a', href=True):
        lists.append(tag['href'])

    return lists
    '''

    tsetup = 'from bs4 import BeautifulSoup'
    print(timeit.timeit(setup = tsetup,
                        stmt = tcode,
                        number = 10000))
