import requests
from lxml import html

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath(['//span[@class="item-price"]/text()'])

print 'Buyers: ', buyers
print 'Prices: ', prices