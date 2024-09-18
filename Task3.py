# Task 3: Develop a Python program to scrape data from a website using BeautifulSoup.

#Installing libraries
#pip install requests
#pip install html5lib
#pip install bs4


import requests
from bs4 import BeautifulSoup 
import csv

#Accessing the HTML content
URL = 'https://www.elmundo.es/quijote/capitulo.html?cual=1'
r = requests.get(URL)

data = r.text

# Parsing the HTML content
soup = BeautifulSoup(data, 'html.parser')
#print(soup.prettify())

# Analyzing content (examples)
#Getting the title
#print(soup.title.text)
# Extracting specific elements
# By ID
#results = soup.find(id="contenido")
#print(results.prettify())
# By HTML Class Name
#titles = soup.find_all('h1')
#for title in titles:
#   print(title.text)