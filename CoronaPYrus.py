from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

URL = 'https://bing.com/covid'
WHO = 'https://covid19.who.int/table'

response = requests.get(WHO)
soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)

#soup.find_all(class="sc-fzplgP bfDTAo th")

#top_row = soup.find(attrs={"class": "sc-fzplgP bfDTAo th"})
#top_row = filter(filter_tags, soup.find(attrs={'class': 'sc-fzplgP bfDTAo th'}).find_all(text=True))
top_row = soup.p['class']
print(top_row)
