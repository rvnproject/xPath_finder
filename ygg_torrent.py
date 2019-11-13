import requests
from pprint import pprint
from lxml import html

books_to_search = 'medicine'

# yggTorrent Search
def yggtorrent(book):
    playload = {
        "name": book,
        "description": "",
        "file": "",
        "uploader": "",
        "category": "2140",
        "sub_category": "",
        "do": "search"
    }

    ygg_request = requests.get("https://www2.yggtorrent.pe/engine/search", params=playload)
    tree_yggtorrent = html.fromstring(ygg_request.content)
    ygg_list = list(tree_yggtorrent.xpath("*//section[contains(@id, '#torrent')]/div//tbody/tr/td[2]//@href"))
    return ygg_list

torrent_list = yggtorrent(books_to_search)
pprint(torrent_list)
print(len(torrent_list))
