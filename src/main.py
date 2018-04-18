from bs4 import BeautifulSoup
import urllib.request as req

import pandas as pd
import numpy as np

url = "http://dengekibunko.jp/newreleases/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

book_table = pd.DataFrame(
	columns = ['title', 'author1', 'author2', 'value', 'date', 'isbn']
)
# #new-anchor-01 > ul > li:nth-child(1) > h3 > a
li_list = soup.select("#new-anchor-01 > ul > li")
for li in li_list:
	a = li.h3.a
	if a != None:
		title = a.string
		href = a.attrs["href"]
		res_href = req.urlopen(href)
		soup_href = BeautifulSoup(res_href, "html.parser")
		author_info = soup_href.select('#author-info > li')
		author1 = author_info[0].string
		author2 = author_info[1].string
		value = soup_href.select('#book-intro > li')[0].string
		book_intro_2 = soup_href.select('#book-intro-2 > li')
		date = book_intro_2[0].string
		isbn = book_intro_2[1].string
		tbl = pd.DataFrame(
			[[title, author1, author2, value, date, isbn]],
			columns = book_table.columns
		)
		book_table = book_table.append(tbl, ignore_index = True)
print(book_table)
book_table.to_csv("./log/dengeki-2018-04.csv")