import requests
from pprint import pprint
from lxml import html

books_to_search = 'medicine' #example

#Kickass Torrent Search
def kickass_torrent(book):
    kickass_list= []

    kickass_request = requests.get("https://kickasstorrents.to/search/{}/category/other/".format(books_to_search))
    tree_kickass = html.fromstring(kickass_request.content)
    try:
        #Get the number of pages to search on all pages.
        number_of_pages = int(list(tree_kickass.xpath("*//div[contains(@class, 'mainpart')]//div[2]/a[last()]//text()"))[-1])

        for i in range(number_of_pages + 1):
            kickass_request = requests.get("https://kickasstorrents.to/search/{}/category/other/{}".format(books_to_search, str(i)))
            tree_kickass = html.fromstring(kickass_request.content)
            kickass_list += list(tree_kickass.xpath("*//table/tbody//div[contains(@class, 'iaconbox center floatright')]/a[contains(@title, 'Download torrent file')]/@href"))
    except:
        kickass_request = requests.get("https://kickasstorrents.to/search/{}/category/other/".format(books_to_search))
        tree_kickass = html.fromstring(kickass_request.content)
        kickass_list += list(tree_kickass.xpath("*//table/tbody//div[contains(@class, 'iaconbox center floatright')]/a[contains(@title, 'Download torrent file')]/@href"))

    return kickass_list

pprint(kickass_torrent(books_to_search))
