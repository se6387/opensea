import web_response
import print_lists
import extract_links_regex
import extract_links_lxml
import html_parser
import beautiful_soup_parser
import bs_execution_time
import filter_crawling

def main():
    # webs to crawl ..
    # opensea.io
    # edfreitas.me
    # quotes.toscrape.com

    webToCrawl = 'https://edfreitas.me'
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
    print_lists.printLists(html_parser.extractLinksHtml(response.text))

    #beautiful soup parser
    print('')
    print('using beautiful soup parser ..')
    print_lists.printLists(beautiful_soup_parser.extractLinksBeautifulSoup(response.text))

    # filter crawling from beautiful soup
    print('')
    print('filtered crawling with beautiful soup ..')
    filter_crawling.printListWithFilter(beautiful_soup_parser.extractLinksBeautifulSoup(response.text), ['pluralsight.'])

    # follow list
    print('')
    print('follow list ..')
    filter_crawling.followList(beautiful_soup_parser.extractLinksBeautifulSoup(response.text), ['pluralsight.'], False)

main()

# check the time it takes to execute bs
print('\n')
print('checking the execution time of beautiful soap ..')
bs_execution_time.executionTime()
