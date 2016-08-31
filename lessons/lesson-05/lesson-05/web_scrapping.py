from bs4 import BeautifulSoup
import urllib
import pdb

url = 'http://www.generalassemb.ly'

#pdb.set_trace()
html_doc = urllib.urlopen(url).read()

my_soup = BeautifulSoup(html_doc)

#Example: Find all images in the home page

image_list = [image.get('src') for image in my_soup.find_all('img')]

for image in image_list:
	print '\n'
	print image

