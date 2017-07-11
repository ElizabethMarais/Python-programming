#Coursera Python Course 4: Using Json schema
print "PROGRAM reads a Json text file about Summer Olympic games, it uses 'Json Olympic games data.txt')."

import sqlite3
conn = sqlite3.connect('Olympicdb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS OlympicSummer ''')

cur.execute('''
CREATE TABLE OlympicSummer (year INTEGER, name TEXT, venues INTEGER)''')

print " "

import json
import urllib2

city_list = list()
city_dict = {}
most_city = {}
most_list = list()
city_list_ven = list() 
i = 0
j = 0
file = 'Json Olympic games data.txt'
fh = open(file)
print "Retrieving books data from a Json data file: ", file

connection = open(file)
data = connection.read()
info_data = json.loads(data)
info = info_data["data"]
print 'Retrieved', len(info),'items in list'
print " "
print "The Summer Olympic games were held:"

for i in range(0, len(info)):
    print 'Year:', info[i]["year"]
    print 'Name:', info[i]["name"]
    print 'Venues used:', info[i]["venues"]

    print " "

    #compile the individual items to build a nested list

    year = int(info[i]["year"])
    name = str(info[i]["name"])
    venues = int(info[i]["venues"])

    item = year, name, venues
    city_list_ven.append(item)
    #build a dictionary of city and year:
    city_dict[year] = name 

    position = j
    cur.execute('''INSERT INTO OlympicSummer (year, name, venues) VALUES (?,?,?)''', (year, name, venues))
    j += 1   #increment 

conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#determine in which city the most games have been held in this file
print " "
for year, city in city_dict.iteritems():
    most_city[city] = most_city.get(city,0) + 1   #determine how many times a city appear in the dictionary

bigcity = None
bigcount = 0
for city, count in most_city.items():
       if bigcount is None or count > bigcount:
          bigcity = city
          bigcount = count
print "The city in which the most Summer Olympic games were held, is", bigcity, "and it was", bigcount, "times." 

print " "
print "From a list, the number of venues used, year, city of Summer Olympic games; venues used descending: "
print "Venues Year City"
city_list_ven.sort(reverse=True)
for i in range(len(city_list_ven)):
    print city_list_ven[i][2], city_list_ven[i][0], city_list_ven[i][1]

print " "
print "The number of most venues used in a Summer Olympic Game is", city_list_ven[0][0],"in the city", city_list_ven[0][2], "in the year", city_list_ven[0][1]

i = 0

for i in range(len(city_list_ven)):
    if i == len(city_list)-1:
        print "The least number of venues used in a Summer Olympic Game is", city_list_ven[i][0],"in the city", city_list_ven[i][2], "in the year", city_list_ven[i][1]


print " "
#build a list of cities and times they appear
for city, count in most_city.items():
    itemlist =  count, city
    most_list.append(itemlist)
most_list.sort(reverse=True)
print "TABLE rows: number of times games held in a specific city, displaying descending: "
i = 0
while i < 5:
     print most_list[i][0], most_list[i][1]
     i += 1

#=============================================== SQL =============================
print " "
print "SQL OUTPUT 1: Print 'Summer Olympic games' from table:"
print "Year  City name   AmountVenues"
sqlstr = "SELECT * FROM OlympicSummer"
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2]

print " "

print "SQL OUTPUT 2: Print from table Summer Olympic games held in a city entered by the user :"
print "Year Venues City name"
cityIN = raw_input("Please enter a city to determine how many Summer Olympic games were held there: ")
citytest = "'" + cityIN + "%'"
sqlstr = "SELECT * FROM OlympicSummer WHERE name like " + citytest
for row in cur.execute(sqlstr):
     print row[0], " ", row[2], "  ", row[1]

print " "

print "SQL OUTPUT 3: From the table, the of number of venues used, year, city of Summer Olympic games; venues used descending: "
print "Year  AmountVenues City name   "
sqlstr = "SELECT * FROM OlympicSummer ORDER BY venues DESC"
for row in cur.execute(sqlstr):
     print row[0], " ", row[2], "  ", row[1]

print " "
bigcity = None
bigvenue = 0
sqlstr = "SELECT * FROM OlympicSummer"
for row in cur.execute(sqlstr):
      city = row[1] 
      venue = row[2]
      if bigvenue is None or venue > bigvenue:
          bigcity = city
          bigvenue = venue
print "The Summer Olympic game where the most venues were used, is", bigcity, "and it was", bigvenue, "times."



cur.close()
