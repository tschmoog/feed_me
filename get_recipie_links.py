# The purpose of this module is to crawl a homepage (BBC Good food) and 
# find urls leading to recipies

from bs4 import BeautifulSoup
import csv
import urllib.request

source = urllib.request.urlopen("bbcgoodfood.com/recipies")
