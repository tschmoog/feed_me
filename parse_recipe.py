# This file gets the data for a recipie from a website (starting with BBC food)
# and gets metadata

# Ingredients
# Timings
# Costs
# Calories


# Step one: Go to a given recipe link (BBC for now) 

# Step two: At the site, pull relevant information
# Get ingredients:


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import itertools


headers={'User-Agent': 'Mozilla/5.0'}
req = Request('https://www.bbcgoodfood.com/recipes/chocolate-fudge-sprinkle-crinkle-biscuits', headers=headers)
source=urlopen(req).read()

soup = BeautifulSoup(source, features='html.parser')
for ingredient_and_info in soup.find_all(itemprop="ingredients"):
    #for some ingredients BBC has a hyperlink which means you'll get the ingredients in 2 parts:
    # E.G: 
    # first part: 2 Large
    # second part: Eggs
    # The second part (eggs) is a hyperlink to more info about eggs
    # This aims to concat the two parts to get one consistent phrase of ingredient + quantity
   ingredient= list(ingredient_and_info.strings)[0:2]
   ingredient = "".join(ingredient)
   print(ingredient)

print("done")

print("Now to find the steps/ingredients")

# Two A: Pull Ingredient list

# Two B: Pull time taken

# Two C/D TO DO after MVP created as they are more complicated: Calories/Costs
# imports

