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
rows = soup.find_all('div', attrs={'role':'row'})
driver.quit()

rest_of_world = total_cases
countries = [] # list of top 10 countries
case_counts = [] # list of cases
for row in rows[1:10]: #rows 1-10 rows are top 10 countries (first row is arbitrary)
    country = row.find('span').get_text(strip=True)
    countries.append(country)
    cases = row.find('div', attrs={'class':'sc-fznOgF fRrkWV'}).get_text()
    cases = cases.replace(",", "") # remove commas
    cases = int(cases)
    case_counts.append(cases)
    rest_of_world = rest_of_world - cases
    #percent = (cases/total_cases) * 100
    #percent = "%.2f" % round(percentage, 2)
    print(country + " - " + str(cases)) #+ " " + str(percent))

print('Rest of world - ' + str(rest_of_world))
countries.append("Rest of World")
case_counts.append(rest_of_world)
print('Total cases - ' + str(total_cases))
print(str(len(countries)) + " " + str(len(case_counts)))

plt.pie(case_counts, labels=countries, autopct="%1.2f%%")
plt.title('COVID-19 Case Distribution by Country')
plt.axis('equal')
plt.show()