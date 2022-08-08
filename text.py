import requests
import bs4


link1 = []

while True:
	for i in range(1,500):
		url = "http://quotes.toscrape.com/page/{}/"
		url2 = url.format(i)
		res = requests.get(url2)
		soup = bs4.BeautifulSoup(res.text,'lxml')
		Link = soup.select('.author + a')
		
		break
	print(len(link1))
	break

