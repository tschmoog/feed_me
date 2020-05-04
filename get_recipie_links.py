# The purpose of this module is to crawl a homepage (BBC Good food) and # find urls leading to recipies
import re
from bs4 import BeautifulSoup
import csv
from urllib.request import Request, urlopen

headers = {'User-Agent': 'Mozilla/5.0'}
req = Request("https://bbcgoodfood.com/recipes",headers=headers)
source= urlopen(req).read()

# Put in a soup object so it can be parsed:
soup = BeautifulSoup(source, features='html.parser') 

#print(soup.prettify())

# Trial output

# Get all recipie links on a page

print(soup.find_all(href=re.compile("recipes")))
# Now we must parse the above list to get links that lead to recipies.
# Problem 1: Determine if a link is a recipie or not.
# Problem 2: Given a link that DOESN'T lead to a recipie - should it be
#            parsed in the hope that it may contain more recipie links?

def is_link_a_recipie():
    pass
