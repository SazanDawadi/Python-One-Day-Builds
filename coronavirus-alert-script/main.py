import requests
from bs4 import BeautifulSoup
from send_sms import send_sms

page = requests.get('https://www.worldometers.info/coronavirus/country/nepal/')
soup = BeautifulSoup(page.content,'html.parser')
total_cases_div = soup.find_all(class_="maincounter-number")

# brief_update is a list which have 
# 1st element gives total no. of cased till date
# 2nd gives total deaths
# 3rd gives total patients recovered

brief_update = [items.find('span').get_text() for items in total_cases_div]
# print(brief_update)

new_update = soup.find('li',class_="news_li")
new_cases = new_update.find('strong').get_text()
new_cases_splitted = new_cases.split(" ", 1)
new_cases_num = int(new_cases_splitted[0])

msg_one = "Hey buds " +"\n\nNew " + str(new_cases_num) + " cases added today. \nPlease stay at home and take care. \n\n "
msg_two = "Todays update:\n New cases: " + brief_update[0] + " \n Deaths : " + brief_update[1] + "\n Recovered : " + brief_update[2]
msg = msg_one + msg_two

# sends msg if new cases is greater then 100
if new_cases_num > 100:
    send_sms(msg)
