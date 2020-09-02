import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt

URL = 'https://bing.com/covid'
WHO = 'https://covid19.who.int/table'


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get(URL)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')
container = soup.find('div', attrs={
    'class':'confirmed'})
print(container)

#response = requests.get(URL)
#soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)

#soup.find_all(class="sc-fzplgP bfDTAo th")

#top_row = soup.find(attrs={"class": "sc-fzplgP bfDTAo th"})
#top_row = filter(filter_tags, soup.find(attrs={'class': 'sc-fzplgP bfDTAo th'}).find_all(text=True))
#for div in soup.findAll('div', {'class': 'sc-fzplgP bfDTAo th'}):
#    print(div.contents[0])
#print(soup.findAll('div', {'class': 'confirmed'}))
#print(soup.findAll(class_ = 'areaName'))
print(soup.title)