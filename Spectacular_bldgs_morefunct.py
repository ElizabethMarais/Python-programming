#www.coursera.org: Python Data structures, course 2 
#Used:  http://www.creativebloq.com/architecture/famous-buildings-around-world-10121105
print "FUNCTION: Reading a data file, list of buildings from 'http://www.creativebloq.com/architecture/famous-buildings-around-world-1012110'; other data added - build list and different ways of displaying data."

print "When prompted, please enter 'Spectacular buildings.txt' as data file."
 

name_file = raw_input("Enter the file name with the Spectacular buildings information: ")
if len(name_file) < 1: name_file = "Spectacular buildings.txt"
name_file = 'Spectacular buildings.txt'

print " "
build_list = list()
build_dict = {}

#05. One World Trade Center, 	New York,USA,	North-America,	2013,	Skidmore Owings & Merrill,

fh = open(name_file)
for line in fh:
        if line.find('.') > 0:
            pos_num = line.find('.')
            num = line[0:pos_num]  #find the building number, read from begin of line till point

                 #find the building name
            pos_name = line.find(',')
            name = line[pos_num+1:pos_name]  #find the building name, read from begin of line till comma 
            name = name.strip()

                 #find the city in rest of line:
            pos_city = line.find(',', pos_name+1)
            city = line[pos_name+1:pos_city]
            cityN = city.strip()    #strip all blank spaces before it

              #find the country in rest of line:
            pos_country = line.find(',', pos_city+1)
            country = line[pos_city+1:pos_country]
            countryN = country.strip()    #strip all blank spaces before it

              #find the continent in rest of line:
            pos_cont = line.find(',', pos_country+1)
            cont = line[pos_country+1:pos_cont]
            contN = cont.strip()    #strip all blank spaces before it

                #find the year completed in rest of line:
            pos_year = line.find(',', pos_cont+1)
            year = line[pos_cont+1:pos_year]
            yearN = year.strip()    #strip all blank spaces before it

                #find the architect(s) in rest of line:
            arch = line[pos_year +1:]
            archN = arch.strip()     #strip all blank spaces before it

            #compile the individual items to build a nested list
            item = num, name, cityN, countryN, contN, yearN, archN
            build_list.append(item)

print "LIST: Print Spectacular buildings names and info extracted from the file in sentences: "
for items in range(len(build_list)):
      print build_list[items][0], build_list[items][1], "in the city", build_list[items][2], ", in country", build_list[items][3], ", in continent", build_list[items][4], ", was completed in", build_list[items][5], "and designed by the architect(s)", build_list[items][6]

#Step 1- build_dictionary of buildings and continents to determine buildings listed in continent most
for items in range(len(build_list)):
     key = build_list[items][0]
     build_dict[key] =  build_list[items][4]

#05. One World Trade Center, 	New York,USA,	North-America,	2013,	Skidmore Owings & Merrill,

#step 2 - build a new dictionary: most_cont = dict() 
most_cont = dict()
for build, cont in build_dict.items():
     most_cont[cont] = most_cont.get(cont,0) + 1
bigcont = None 
bigcount = 0
for cont, count in most_cont.items():
    if bigcont is None or count > bigcount:
          bigcont = cont
          bigcount = count
print " "        
print "The continent in which the most spectacular buildings listed is situated, is:", bigcont, "namely ", bigcount, "times."


print " "
print "DATA FILE LIST: Print Spectacular buildings no.'s and names (to compare with data from web page):"
for items in range(len(build_list)):
       print build_list[items][0], build_list[items][1], ",", build_list[items][2]

print " "
print "RETRIEVING WEB PAGE FILE (url) of same data; reading and printing Buildings from page."
import urllib
from BeautifulSoup import *
import re

url = 'http://www.creativebloq.com/architecture/famous-buildings-around-world-10121105'
print "Retrieving: ", url
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# Retrieve a list of the anchor tags
print " "
tags = soup('h3')
for tag in tags:
    tagstr = str(tag)
    building_posS =  tagstr.find('<h3>')
    building_posE =  tagstr.find('</h3>')
    building = tagstr[building_posS+4:building_posE]
    print building
    if building == "27. Burj Khalifa, Dubai":
       break

#Use data file, 'Spectacular buildings.txt', again
#determine which building is oldest
print " "
bigyear = None
bigcount = 0
build_list_sortdt = list()  # list of building names and year completed
for items in range(len(build_list)):
    year_str = build_list[items][5]
    year_int = int(year_str)
    item_new = year_int, build_list[items][1]
    build_list_sortdt.append(item_new)
build_list_sortdt.sort()
print "DATA FILE - LIST: sorted ascending according to year: "
print "Building name  Year completed."
for items in range(len(build_list_sortdt)):
      print build_list_sortdt[items][1], " ", build_list_sortdt[items][0]
print " "
#print build_list_sortdt
print "RESULTS: "
print "The oldest building listed is", build_list_sortdt[0][1], "completed in the year", build_list_sortdt[0][0]
max = len(build_list_sortdt)
print "The newest building listed is", build_list_sortdt[max-1][1], "completed in the year", build_list_sortdt[max-1][0]
