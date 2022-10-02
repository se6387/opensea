from pickle import TRUE
from bs4 import BeautifulSoup

def extractLinksBeautifulSoup(text):
    lists = []
    initBS = BeautifulSoup(text, 'lxml')

    for tag in initBS.find_all('a', href=True):
        lists.append(tag['href'])

    return lists
