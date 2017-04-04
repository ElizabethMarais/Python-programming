print "COURSE: www.coursera.org: Course 3 - Using Python to access web data, Week 4."
print "FUNCTION: Program uses BeautifulSoup to read and parse a web file."
print "It prints lines with certain tags/words in."
print " "
print "Uses 'https://www.python.org' "

import urllib
from BeautifulSoup import *

url = 'https://www.python.org'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

print " "
print "OUTPUT 1: Find lines with 'link' in, print words after 'rel':"
tags = soup('link')
for tag in tags:
    print tag.get('rel', None)


print " "
print "OUTPUT 2: Find lines with 'li' in, print words after 'class' (first 8):"
tags = soup('li')
tags_part = tags[0:7]
print "Print original lines found: "
print tags_part
print " "
print "Print words after 'class':"
for tag in tags_part:
    print tag.get('class', None)



