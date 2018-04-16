from bs4 import BeautifulSoup
import urllib.request as req

url = "http://dengekibunko.jp/newreleases/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

# #new-anchor-01 > ul > li:nth-child(1) > h3 > a
li_list = soup.select("#new-anchor-01 > ul > li")
for li in li_list:
	a = li.h3.a
	if a != None:
		title = a.string
		href = a.attrs["href"]
		print(title + " (" + href + ")")