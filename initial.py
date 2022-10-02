import extract_links_regex
import extract_links_lxml
import print_lists
import web_response

def main():
    # webs to crawl ..
    # opensea.io
    # edfreitas.me
    # quotes.toscrape.com

    response = web_response.getWebResponse('https://opensea.io')
    print_lists.printLists(extract_links_regex.extractLinksRegEx(response.text))

    #
    print('')
    print_lists.printLists(extract_links_lxml.extractLinksLxml(response.text))

main()
