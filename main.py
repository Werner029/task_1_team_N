import requests
from bs4 import BeautifulSoup

url = "https://sportmail.ru/?utm_source=portal&utm_medium=new_portal_navigation_all&utm_campaign=sport.mail.ru&mt_click_id=mt-h3p427-1713632344-2949026145&mt_sub1=deti.mail.ru"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

news_items = soup.find_all("a", class_="list__text")

for item in news_items:
    href = item.get("href")
    print(href)