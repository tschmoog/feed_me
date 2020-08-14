# The purpose of this module is to crawl a homepage (BBC Good food) and # find urls leading to recipies
import re
import lxml
from bs4 import BeautifulSoup
import csv
from urllib.request import Request, urlopen

headers = {'User-Agent': 'Mozilla/5.0'}
req = Request("https://bbcgoodfood.com/sitemap.xml",headers=headers)
source= urlopen(req).read()

# Put in a soup object so it can be parsed:
soup = BeautifulSoup(source, 'lxml')
# Look at the sitemap and return all sites which reference a recipe:

# Find all links on the sitemap:
links = soup.find_all("loc", text=True)

# Parse links for potential recipes:
recipe_list = []
for link in links:
    if link.find(text=re.compile('recipes')):
        recipe_list.append(link.string)

# Add recipes to a csv for other modules to operate on
# TO DO: Save these to a more sustainable format (SQL Database?)
with open("bbc_recipe_links.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(recipe_list)

# Trial output
hungry = input("Hungry? Y/N")
if hungry == 'y':
    for recipe in recipe_list:
        print(recipe)
else:
    print('kk maybe later')
# Get all recipie links on a page
# Then parse those links for more
# Only go down to a certain depth to stop a potential infinite loop


# Now we must parse the above list to get links that lead to recipies.
# Problem 1: Determine if a link is a recipie or not.
# Problem 2: Given a link that DOESN'T lead to a recipie - should it be
#            parsed in the hope that it may contain more recipie links?

def is_link_a_recipie():
    pass
