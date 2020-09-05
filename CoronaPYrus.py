import time
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt

URL = 'https://bing.com/covid'
WHO = 'https://covid19.who.int/table'

driver = webdriver.Chrome()
driver.get(WHO)
time.sleep(3)
time.sleep(1)
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
total_cases = soup.find('div', attrs={'class':'sc-fzplgP bfDTAo th'}).get_text()
total_cases = total_cases.replace(",", "") # remove commas
total_cases = int(total_cases)
data = []
rows = soup.find_all('div', attrs={'role':'row'})
driver.quit()

for row in rows:
    country = row.find('span').get_text(strip=True)
    if country == 'Name': # skip the first row
        continue
    cases = row.find('div', attrs={'class':'sc-fznOgF fRrkWV'}).get_text()
    cases = cases.replace(",", "") # remove commas
    cases = int(cases)
    percentage = (cases/total_cases) * 100
    percentage = "%.2f" % round(percentage, 2)
    print(country + " - " + str(cases) + " " + str(percentage))


print('Total cases - ' + str(total_cases))
