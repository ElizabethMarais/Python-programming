print "Coursera Python course 3, week 4 Assignment 2"
print "The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, "
print " scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat "
print "the process a number of times and report the last name you find.
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
# Own file name: Course3_Wk4_Ass2_Jubin.py


#Enter URL: http://python-data.dr-chuck.net/known_by_Jubin.html

import urllib
from BeautifulSoup import *

url = raw_input("Enter URL: ")
count = raw_input("Enter count: ")
position = raw_input("Enter position: ")
times = 0
count_int = int(count)
print "Retrieving:", url
while times <= count_int:
     html = urllib.urlopen(url).read()
     soup = BeautifulSoup(html)
     # Retrieve all of the anchor tags
     tags = soup('a')
     pos_int = int(position)
     print "Retrieving:", tags[pos_int-1].get('href', None)
     url = tags[pos_int-1].get('href', None)
     times = times + 1
     if times == count_int:
             pos_name_start = url.find('by_')
             pos_name_end = url.find('.html')
             name = url[pos_name_start+3:pos_name_end]
             print name
             break