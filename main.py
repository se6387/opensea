import web_response
import print_lists
import extract_links_regex
import extract_links_lxml
import html_parser


def main():
    # webs to crawl ..
    # opensea.io
    # edfreitas.me
    # quotes.toscrape.com

    webToCrawl = 'https://opensea.io'
    response = web_response.getWebResponse(webToCrawl)
    print('crawling : ', webToCrawl, ' ..', sep='')

    # regex
    print('')
    print('using regex ..')
    print_lists.printLists(extract_links_regex.extractLinksRegEx(response.text))

    # lxml
    print('')
    print('using lxml ..')
    print_lists.printLists(extract_links_lxml.extractLinksLxml(response.text))

    # html parser
    print('')
    print('using html ..')
    print_lists.printLists(html_parser.extractLinksHtmlParser(response.text))

main()
