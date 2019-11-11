import requests
from pprint import pprint
from lxml import html


books_to_search = 'medicine' #example

#yggTorrent Search
def yggtorrent(book):
	playload = {"name": book, "description": "", "file": "", "uploader": "", "category": "2140", "sub_category": "", "do": "search"}
	ygg_request = requests.get("https://www2.yggtorrent.pe/engine/search", params=playload)
	tree_yggtorrent = html.fromstring(ygg_request.content)
	ygg_list = list(tree_yggtorrent.xpath("*//section[contains(@id, '#torrent')]/div//tbody/tr/td[2]//@href"))
	return ygg_list

#Kickass Torrent Search
def kickass_torrent(book):
	kickass_list= []

	kickass_request = requests.get("https://kickasstorrents.to/search/"+ books_to_search +"/category/other/")
	tree_kickass = html.fromstring(kickass_request.content)

	try:
		#Get the number of pages to search on all pages.
		number_of_pages = int(list(tree_kickass.xpath("*//div[contains(@class, 'mainpart')]//div[2]/a[last()]//text()"))[-1])

		for i in range(number_of_pages+1):
			kickass_request = requests.get("https://kickasstorrents.to/search/"+ books_to_search +"/category/other/"+ str(i))
			tree_kickass = html.fromstring(kickass_request.content)
			kickass_list += list(tree_kickass.xpath(
				"*//table/tbody//div[contains(@class, 'iaconbox center floatright')]/a[contains(@title, 'Download torrent file')]/@href"))
	except:
		kickass_request = requests.get("https://kickasstorrents.to/search/"+ books_to_search +"/category/other/")
		tree_kickass = html.fromstring(kickass_request.content)
		kickass_list += list(tree_kickass.xpath(
			"*//table/tbody//div[contains(@class, 'iaconbox center floatright')]/a[contains(@title, 'Download torrent file')]/@href"))

	return kickass_list


pprint(yggtorrent(books_to_search))