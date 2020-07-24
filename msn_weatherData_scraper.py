import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.msn.com/en-us/weather/today/London,England,United-Kingdom/we-city?iso=GB&savedegree=true&weadegreetype=C&el=qapKpi0n0MFchvDijYHhpA%3D%3D')
soup = BeautifulSoup(page.content,'html.parser')
today_temp = soup.find('span',class_='current').get_text()
print(today_temp)
today_stat = soup.find(class_='weather-info')

today_weth = today_stat.find('span').get_text()
forcast_list = soup.find(class_='forecast-list')
day_blk = forcast_list.find_all('li',class_='')
weather_data = []

for days in day_blk:
    # print(days)
    day = days.find('span').get_text()
    high_temp = days.find('p').get_text()
    weather_type = days.find('img').get('alt')
    weather_data.append((day,high_temp,weather_type))

print(weather_data)

