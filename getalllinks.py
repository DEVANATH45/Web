import requests
from bs4 import BeautifulSoup
urls = []
def webscrap(site):

    url = requests.get(site)
    soup = BeautifulSoup(url.text,'html.parser')
    web = soup.find_all('a')
    for i in web:
        href = i.get('href')
        if href.startswith("/"):
            href=site+href
            urls.append(href)
        else:
            if href!='#':
                urls.append(href)

    for j in urls:
        print(j)


webscrap('https://docplus.online/')


