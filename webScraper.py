import requests
import bs4

url = "http://quotes.toscrape.com/page/{}/"
authors = []
authorsLink = []
while True:
	for i in range(1,500):
		url2 = url.format(i)
		res = requests.get(url2)
		soup = bs4.BeautifulSoup(res.text,'lxml')
		quotes = soup.select('small.author')
		Link = soup.select('.author + a')
		if(quotes != []):
			for el in quotes:
				authors.append(el.getText())
		if(Link != []):
			for el1 in Link:
				authorsLink.append(el1['href'])
			continue
		break
	break

authors = authors
authorsLink = authorsLink
authorAndLinks = dict(zip(authors,authorsLink))
print(authorAndLinks)
with open("file.txt",'w') as myfile:
	for key,el in authorAndLinks.items():
		myfile.write(key)
		myfile.write(' : ')
		myfile.write(el)
		myfile.write(' ')
