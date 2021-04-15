import requests
from bs4 import BeautifulSoup

source = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.42132653400006&lon=-106.10840384499994#.YHGm3azitEY')
soup = BeautifulSoup(source.content, 'html.parser')
#print(soup.find_all('a'))
week = soup.find(id='seven-day-forecast')
place = week.find(class_='panel-heading')
print(place.get_text())
print("\n")
item = week.find(class_='panel-body')
period_names = item.find_all(class_='tombstone-container')
for i in range(0,9):
    print(period_names[i].get_text())

#aims to print weather forcast of the given particular area