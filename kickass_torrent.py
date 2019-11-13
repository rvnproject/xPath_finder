import requests
from pprint import pprint
from lxml import html

books_to_search = 'medicine' # example

def get_page_number():
    kickass_request = requests.get("https://kickasstorrents.to/search/{}/category/other/".format(books_to_search))
    tree_kickass = html.fromstring(kickass_request.content)
    page_nav_items = list(tree_kickass.xpath("*//a[contains(@class, 'turnoverButton') and contains(@class, 'siteButton') and contains(@class, 'bigButton')]//text()"))

    if not page_nav_items:
        return 1
    if page_nav_items[-1] == ">>":
        return int(page_nav_items[-2])
    return int(page_nav_items[-1])

def get_torrent_url_list_from_page_number(page_number):
    kickass_request = requests.get("https://kickasstorrents.to/search/{}/category/other/{}".format(books_to_search, str(page_number)))
    tree_kickass = html.fromstring(kickass_request.content)
    return list(tree_kickass.xpath("*//table/tbody//div[contains(@class, 'iaconbox center floatright')]/a[contains(@title, 'Download torrent file')]/@href"))

# Kickass Torrent Search
def kickass_torrent(book):
    kickass_torrent_list= []

    for i in range(get_page_number()):
        kickass_torrent_list += get_torrent_url_list_from_page_number(i + 1)
    return list(map(lambda x: "https://kickasstorrents.to{}".format(x), kickass_torrent_list))

torrent_list = kickass_torrent(books_to_search)
pprint(torrent_list)
print(len(torrent_list))
