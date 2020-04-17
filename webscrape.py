from bs4 import BeautifulSoup
import requests
import timsort
#Function to webscrape data
def scrape(content,cl):
    d=[]
    for i in content.find('div', {"class": cl}).select("td")[2:13:2]:
        d.append(i.getText())
    return timsort.timSort(d, len(d))
#For Rabi crops
url= 'https://farmers-portal.github.io/farmsite/rabi.html'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
base_price = {}
base_price['wheat'] = scrape(content,"first")
base_price['barley'] = scrape(content,"barl")
base_price['mustard'] = scrape(content,"must")
base_price['peas'] = scrape(content,"pea")
base_price['sesame'] = scrape(content,"bottom")

#For Kharif crops
urlk= 'https://farmers-portal.github.io/farmsite/kharif.html'
res = requests.get(urlk, timeout=5)
cont = BeautifulSoup(res.content , "html.parser")

base_price['millet'] = scrape(cont,"first")
base_price['paddy'] = scrape(cont,"pad")
base_price['maize'] = scrape(cont,"mai")
base_price['sugarcane'] = scrape(cont,"sugar")
base_price['soyabean'] = scrape(cont,"soy")
base_price['groundnut'] = scrape(cont,"gn")
base_price['cotton'] = scrape(cont,"cot")
base_price['cashew'] = scrape(cont,"bottom")
base_price['turmeric'] = scrape(cont,"tur")

print(base_price)



