import requests
import bs4


url = "http://quotes.toscrape.com/page/{}/"
authors = []
while True:
	for i in range(1,500):
		url2 = url.format(i)
		res = requests.get(url2)
		soup = bs4.BeautifulSoup(res.text,'lxml')
		quotes = soup.select('.author')
		if(quotes != []):
			for el in quotes:
				authors.append(el.getText())
			continue
		break
	print(set(authors))
	break

	

