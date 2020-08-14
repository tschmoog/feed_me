# This file gets the data for a recipie from a website (starting with BBC food)
# and gets metadata

# Ingredients
# Timings
# Costs
# Calories


# Step one: go to a site (BBC) 

# Step two: At the site, pull relevant information

# Two A: Pull Ingredient list

# Two B: Pull time taken

# Two C/D TO DO after MVP created as they are more complicated: Calories/Costs
# imports

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

headers={'User-Agent': 'Mozilla/5.0'}
req = Request('https://www.bbcgoodfood.com/recipes/chocolate-fudge-sprinkle-crinkle-biscuits', headers=headers)
source=urlopen(req).read()

soup = BeautifulSoup(source)
for ingredient in soup.find_all(class_="ingredients-list__item"):
    print(ingredient)

