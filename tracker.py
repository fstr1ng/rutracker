import requests
from bs4 import BeautifulSoup as BS

login_url = 'http://rutracker.org/forum/login.php'
login_data = {
        'login_username': 'username',
        'login_password': 'pass',
        'redirect': 'index.php',
        'login': 'Вход'
        }

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 5.2; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
        }


session = requests.Session()
session.post(login_url, data=login_data, headers=headers)

search_string = 'Веном'
search_url = f'https://rutracker.org/forum/tracker.php?nm={search_string}'
search_request = session.post(search_url, headers=headers)

soup = BS(search_request.text, 'html.parser')

print(soup.find_all('tr', class_='tCenter')[2])
