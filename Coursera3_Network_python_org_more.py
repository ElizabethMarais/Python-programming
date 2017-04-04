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
print "OUTPUT 1: Find lines with 'a' in, print value of 'href' (href=) (first 6):"
tags = soup('a')
tags_part = tags[0:6]
for tag in tags_part:
    print tag.get('href', None)   



print " "
print "OUTPUT 2: Find lines with 'meta' in, print value of 'name' (first 6):"
tags = soup('meta')
tags_part = tags[0:6]
print "Print original lines found: "
print tags_part
print " "
print "Print value of 'name', will display 'None' if 'name' not found:"
for tag in tags_part:
    print tag.get('name', None)

print " "
print " "
print "OUTPUT 3: Find lines with 'meta' in, print value of 'http-equiv':"
tags = soup('meta')
print "Print original lines found (first 18 lines printed): "
print tags[0:18]
print " "
print "Print value of 'http-equiv', only if found in above lines:"
for tag in tags:
    found_value = tag.get('http-equiv', None)
    if found_value <> None:
        print found_value




