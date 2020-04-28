# The purpose of this module is to crawl a homepage (BBC Good food) and 
# find urls leading to recipies

from bs4 import BeautifulSoup
import csv
from urllib.request import Request, urlopen

req = Request("https://bbcgoodfood.com/recipes", headers={'user-agent': 'mozilla/5.0'})

source = urlopen(req).read()
soup = BeautifulSoup(source,'lxml')

# parse page and print 'a' tags.
for link in soup.findAll('a'):
	print(link)


# What does the webpage give us?

