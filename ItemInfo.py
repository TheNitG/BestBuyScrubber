# Import necessary packages
import requests
from bs4 import BeautifulSoup

# Declare the URL (Set to Dell S2721HGF for now)
URL = "https://www.bestbuy.com/site/dell-s2721hgf-27-gaming-led-curved-fhd-freesync-and-g-sync-compatible-monitor-displayport-hdmi-black/6425903.p?skuId=6425903"
# Declare Browser
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.27 Safari/537.36"
headers = {'User-Agent': user_agent}
# Get the page
page = requests.get(URL, headers=headers)
# Use BeautifulSoup package to parse as html
soup = BeautifulSoup(page.content, 'html.parser')
# Find the price field and refine the result
result = str(soup.find('div', class_='priceView-hero-price priceView-customer-price'))
target = result[result.find("$"):]
# Display the price
print(target[:target.find("<")])
