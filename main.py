import requests
from lxml import html


isbn_request = requests.post(
	"http://wokinfo.com/cgi-bin/bkci/search.cgi", 
	data={"search": "elsevier", "searchtype": "and"}, 
	headers={
		"Content-Type": "application/x-www-form-urlencoded"
	})


tree = html.fromstring(isbn_request.content)
isbn_list = list(map(lambda x: x[0:-1], tree.xpath("*//table[contains(@class, 'datatable')]//tbody//tr//td[2]//text()")))

