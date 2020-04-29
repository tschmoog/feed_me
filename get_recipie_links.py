# The purpose of this module is to crawl a homepage (BBC Good food) and 
# find urls leading to recipies

from bs4 import BeautifulSoup
import csv
from urllib.request import Request, urlopen

headers = {'User-Agent': 'Mozilla/5.0'}
req = Request("https://bbcgoodfood.com/recipes",headers=headers)
source= urlopen(req).read()

# Put in a soup object so it can be parsed:
soup = BeautifulSoup(source, features='html.parser') 

# Trial output
# Get all links on initial page
for link in soup.find_all('a'):
	print(link.get('href'))

