from bs4 import BeautifulSoup
import requests

#Function to webscrape data
def scrape(content,cl):
    d={}
    b=2
    for i in content.find('div', {"class": cl}).select("td")[1:14:2]:
        y = content.find('div', {"class": cl}).select("td")[b]
        d[i.getText()] = y.getText()
        b += 2
    return d
    print(d)

#For Rabi crops
url= 'https://farmers-portal.github.io/farmsite/rabi.html'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
#Declaring dictionaries
wheat = {}
barley = {}
peas = {}
sesame = {}
mustard = {}
wheat = scrape(content,"first")
barley = scrape(content,"barl")
mustard = scrape(content,"must")
peas = scrape(content,"pea")
sesame = scrape(content,"bottom")
print("Rabi")
print(wheat)
print(barley)
print(mustard)
print(peas)
print(sesame)

#For Kharif crops
urlk= 'https://farmers-portal.github.io/farmsite/kharif.html'
res = requests.get(urlk, timeout=5)
cont = BeautifulSoup(res.content , "html.parser")
millet = {}
paddy = {}
maize = {}
sugarcane = {}
soyabean = {}
cashew = {}
groundnut = {}
cotton = {}
turmeric = {}
millet = scrape(cont,"first")
paddy = scrape(cont,"pad")
maize = scrape(cont,"mai")
sugarcane = scrape(cont,"sugar")
soyabean = scrape(cont,"soy")
groundnut = scrape(cont,"gn")
cotton = scrape(cont,"cot")
cashew = scrape(cont,"bottom")
turmeric = scrape(cont,"tur")
print("Kharif")
print(millet)
print(paddy)
print(maize)
print(sugarcane)
print(soyabean)
print(groundnut)
print(cotton)
print(cashew)
print(turmeric)

