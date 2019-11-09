import requests
from lxml import html


isbn_request = requests.post(
	"http://wokinfo.com/cgi-bin/bkci/search.cgi", 
	data={"search": "elsevier", "searchtype": "and"}, 
	headers={
		"Content-Type": "application/x-www-form-urlencoded"
	})



wokinfo_tree = html.fromstring(isbn_request.content)
isbn_list = list(map(lambda x: x[0:-1], wokinfo_tree.xpath("*//table[contains(@class, 'datatable')]//tbody//tr//td[2]//text()")))

libgen_request = requests.post(
	"http://libgen.lc/batchsearchindex.php?lgtopic=libgen", 
	data={"Content-Disposition": "form-data", "dsk": "\n".join(isbn_list[0:4900]), "isbn": "1"}
)

libgen_tree = html.fromstring(libgen_request.content)
libgen_missing_isbn_list = list(libgen_tree.xpath("//table[last()]/tr[ td[3]/text() = 0]/td[1]//text()"))
