#Coursera Python Course 3, Chapter 1: Networked programs
#Using BeautifulSoup for easier string accessing


import urllib
from BeautifulSoup import *
url = raw_input('Enter file to open: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)


print " "
print "Accessing and printing whathour.py file from the PY4inf.com web page."
fhand = urllib.urlopen('http://www.py4inf.com/code/whathour.py')
for line in fhand:
    print line.strip()


print " "
print  "Print all lines from 'http://www.python.org': "
from BeautifulSoup import BeautifulSoup
import urllib2
import re

url = urllib2.urlopen("http://www.python.org")
content = url.read()
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True):
    if re.findall('python', a['href']):
        print "Found the URL:", a['href']

