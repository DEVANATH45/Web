import requests
from bs4 import BeautifulSoup
lists = []

def checklist(site):
    for i in site:
        check_url = requests.get(i,timeout=10)
        print(check_url.status_code)
        if check_url.status_code!=500:
            print(i+" is down.")
        else:
            print(i+" website is active.")


def Scrap(site):
    url = requests.get(site)
    soup = BeautifulSoup(url.text, 'html.parser')
    sites = soup.find_all('a', href=True)
    for link in sites:
        l = link['href']
        if l.startswith('#'):
            continue
        if l.startswith('/'):
            l = site+l
            lists.append(l)
        else:
            lists.append(l)

    # for i in set(lists):
    #     print(i)
    return list(dict.fromkeys(lists))

urls='https://contentmarketinginstitute.com/'
value = Scrap(urls)
checklist(value)