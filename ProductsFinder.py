# Import necessary packages
import requests
from bs4 import BeautifulSoup
import tkinter as tk


# Function to find the products and their respective prices from the search term
def find_products_from_term(search_term):
    # Turn spaces into + to work in URL
    search_term = str(search_term).replace(' ', '+')
    # Declare the URL from the input
    url = 'https://www.bestbuy.com/site/searchpage.jsp?st=' + search_term + '&_dyncharset=UTF-8&_dynSessConf=&id=pcat' \
        '17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys '
    # Declare Browser
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.2' \
                 '7 Safari/537.36 '
    headers = {'User-Agent': user_agent}
    # Get the page
    page = requests.get(url, headers=headers)
    # Use BeautifulSoup package to parse as html
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find all elements containing product names on the page
    names = soup.find_all('h4', class_='sku-header')
    # Clean the elements to only get the names
    cleaned_names = []
    for name in names:
        name = str(name)
        name = name[name.find('>', name.find('skuId=')) + 1:]
        cleaned_names.append(name.strip('</a></h4>'))
    # Find all elements containing prices for the products named on the page
    prices = soup.find_all('div', class_='priceView-hero-price priceView-customer-price')
    # Clean the elements to only get the prices
    cleaned_prices = []
    for price in prices:
        price = str(price)
        price = "$" + price[price.find("-->") + 3:].strip("</span></div>")
        cleaned_prices.append(price)
    # Some sites contain miscellaneous products at the top, so we remove them here
    cleaned_prices = cleaned_prices[len(cleaned_prices) - len(cleaned_names):]
    # Return the names and prices as a tuple
    return cleaned_names, cleaned_prices


# Method to display the product names and their respective prices in the window
def find_products():
    # Get the names and prices
    n, p = find_products_from_term(entry.get())
    # Get the length of the labels array
    length = len(labels)
    # Use the length to go through and remove all labels from the array and window
    for x in range(length):
        labels.pop().destroy()
    # Go through the new product names and their respective prices and display them on the window
    for x in range(len(n)):
        name_label = tk.Label(text=n[x])
        price_label = tk.Label(text=p[x])
        name_label.pack()
        price_label.pack()
        labels.append(name_label)
        labels.append(price_label)


# Create the window
window = tk.Tk()
# Add a label that says Product
tk.Label(text='Product').pack()
# Add a text box to type your search keyword(s)
entry = tk.Entry()
entry.pack()
# Create array to contain all product name and price labels
labels = []
# Create button to submit search
submit = tk.Button(text='Search', command=find_products)
submit.pack()
# Run the window
window.mainloop()
