from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

URL = 'https://bing.com/covid'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title.string)
