from urllib2 import urlopen

url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
page = urlopen(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page)

print soup.prettify()