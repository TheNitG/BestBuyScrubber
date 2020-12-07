# Import necessary packages
import requests
from bs4 import BeautifulSoup

# Ask for the item to be queried
searchTerm = input('What product? ')
# Declare the URL from the input
URL = 'https://www.bestbuy.com/site/searchpage.jsp?st=' + searchTerm + '&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071' \
    '&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n' \
    '&af=true&iht=y&usc=All+Categories&ks=960&keys=keys '
# Declare Browser
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.27 ' \
    'Safari/537.36 '
headers = {'User-Agent': user_agent}
# Get the page
page = requests.get(URL, headers=headers)
# Use BeautifulSoup package to parse as html
soup = BeautifulSoup(page.content, 'html.parser')
# Find all elements containing product names on the page
names = soup.find_all('h4', class_='sku-header')
# Clean the elements to only get the names
cleanedNames = []
for name in names:
    name = str(name)
    name = name[name.find('>', name.find('skuId=')) + 1:]
    cleanedNames.append(name.strip('</a></h4>'))
# Find all elements containing prices for the products named on the page
prices = soup.find_all('div', class_='priceView-hero-price priceView-customer-price')
# Clean the elements to only get the prices
cleanedPrices = []
for price in prices:
    price = str(price)
    price = "$" + price[price.find("-->")+3:].strip("</span></div>")
    cleanedPrices.append(price)
# Display the product names and their respective prices
for x in range(len(cleanedNames)):
    print(cleanedNames[x] + ":\n" + cleanedPrices[x])
