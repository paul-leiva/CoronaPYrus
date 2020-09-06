# Created by Paul Leiva | paul-leiva.github.io
# Florida International University (FIU), Miami, FL, USA

import time
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt

WHO = 'https://covid19.who.int/table' # the URL we will be using for this program

driver = webdriver.Chrome()
driver.get(WHO)
time.sleep(3)
time.sleep(1)
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
total_cases = soup.find('div', attrs={'class':'sc-fzplgP bfDTAo th'}).get_text()
with_commas = total_cases
total_cases = total_cases.replace(",", "") # remove commas
total_cases = int(total_cases)
rows = soup.find_all('div', attrs={'role':'row'})
driver.quit()

rest_of_world = total_cases
countries = [] # list of top 10 countries
case_counts = [] # list of cases
for row in rows[1:11]: #rows 1-10 rows are top 10 countries (first row is arbitrary)
    country = row.find('span').get_text(strip=True)
    cases = row.find('div', attrs={'class':'sc-fznOgF fRrkWV'}).get_text()
    countries.append(country + " - " + str(cases) + " cases")
    cases = cases.replace(",", "") # remove commas
    cases = int(cases)
    case_counts.append(cases)
    rest_of_world = rest_of_world - cases

countries.append("Rest of World - " + str(rest_of_world) + " cases")
case_counts.append(rest_of_world)
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1) # detach the Rest of World slice of the pie

wedges = { 'linewidth' : 1.5, 'edgecolor' : 'black'}
slice_colors = {"red", "lime", "orange", "blue", "magenta", "cyan", # pie slice colors
          "darkviolet", "springgreen", "yellow", "dodgerblue", "darkgray"}

plt.pie(case_counts,
        labels=countries,
        labeldistance=1.05,
        autopct= "%.2f%%",
        explode=explode,
        textprops={'fontsize': '14'},
        wedgeprops = wedges,
        startangle=90,
        colors=slice_colors,
        radius=2)
plt.title('COVID-19 Case Distribution by Country\nThere have been ' + with_commas +
          ' global cases as of ' + time.strftime("%m/%d/%Y", time.localtime()))
plt.axis('equal')
plt.show()