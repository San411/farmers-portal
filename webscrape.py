from bs4 import BeautifulSoup
import requests

# Function to webscrape data
def scrape(content, cl, index):
    for i in content.find('div', {"class": cl}).select("td")[index]:
        return int(i)

def repeat(index):
    url = 'https://farmers-portal.github.io/farmsite/rabi.html'
    response = requests.get(url)
    content = BeautifulSoup(response.content, "html.parser")
    urlk = 'https://farmers-portal.github.io/farmsite/kharif.html'
    res = requests.get(urlk)
    cont = BeautifulSoup(res.content, "html.parser")

    b_prices = {}
    b_prices['wheat'] = scrape(content, "first", index)
    b_prices['barley'] = scrape(content, "barl", index)
    b_prices['mustard'] = scrape(content, "must", index)
    b_prices['peas'] = scrape(content, "pea", index)
    b_prices['sesame'] = scrape(content, "bottom", index)
    b_prices['millet'] = scrape(cont, "first", index)
    b_prices['paddy'] = scrape(cont, "pad", index)
    b_prices['maize'] = scrape(cont, "mai", index)
    b_prices['sugarcane'] = scrape(cont, "sugar", index)
    b_prices['soyabean'] = scrape(cont, "soy", index)
    b_prices['groundnut'] = scrape(cont, "gn", index)
    b_prices['cotton'] = scrape(cont, "cot", index)
    b_prices['cashew'] = scrape(cont, "bottom", index)
    b_prices['turmeric'] = scrape(cont, "tur", index)

    return b_prices

bij_price = {}
u_price = {}
bang_price = {}
bij_price = repeat(2)
u_price = repeat(4)
bang_price = repeat(6)