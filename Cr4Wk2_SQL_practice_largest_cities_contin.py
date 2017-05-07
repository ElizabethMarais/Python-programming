#Coursera Python Course 4: Using Databases
#NB: test data file: DATA must contain no FLOAT numbers, only INTEGERs
print "PROGRAM reads a text file line by line, (it uses 'largest_cities.txt' as default), data was obtained from https://en.wikipedia.org/wiki/List_of_cities_proper_by_population; it parses the words, stores info in a list. It prints the table rows in the database; it asks user to enter a letter to check for all countries starting with it."
print "It creates another table, cities and continents, reading the data from text tile, 'CountryContinent.txt'. Enter 'largest_cities.txt' as data file when asked."

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS LargestCities''')

cur.execute('''
DROP TABLE IF EXISTS CountryContinent''')


cur.execute('''
CREATE TABLE LargestCities (rank INTEGER, city TEXT, population INTEGER, area INTEGER, country TEXT)''')

cur.execute(''' 
CREATE TABLE CountryContinent (countryC TEXT, continent TEXT) ''')

#read cities and continents from text file, 'CountryContinent.txt'
import string
cont_list = list()
i = 0
j = 0
print " "
fname = 'CountryContinent.txt'
fh = open(fname)
for line in fh:
#  if line > "/n":   #if it is not a blank line
      pos_country = line.find(',')
      country = line[0:pos_country]  #find the number, read from begin of line till comma 
      countryI = country.lstrip()
      
      pos_cont = line.find(',', pos_country+1)
      continent = line[pos_country+1:pos_cont]  #find the country, read after name till comma 
      continentI = continent.lstrip() 
 
      list_item = countryI, continentI
      cont_list.append(list_item)
      position = j
      cur.execute('SELECT continent FROM CountryContinent WHERE countryC = ?', (countryI, ))   
#1. ? place holder   2.(  , ) is a tuple (need comma, space), instead of WHERE...
      try:       #try: to test if there are rows
        pos = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
        cur.execute('UPDATE CountryContinent SET continent = continent WHERE countryC = ?', (countryI, )) 
      except:
#if no rows, write a row, start with index 1
        cur.execute('''INSERT INTO CountryContinent (countryC, continent) VALUES (?,?)''', (countryI, continentI))
conn.commit()
#NB: commit: all stuff done in memory, write back to disk



import string    #to use in string.punctuation
cities = list()
i = 0
j = 0
fname = raw_input('Please enter text file name of largest cities: ')
if ( len(fname) < 1 ) : fname = 'largest_cities.txt'
fh = open(fname)
for line in fh:
#  if line > "/n":   #if it is not a blank line
    pieces = line.split()
    for i in range(len(pieces)):
#      pieces[i] = pieces[i].translate(string.maketrans("",""), string.punctuation)   #remove all punctuation marks e.g. '.'
      rankI = int(pieces[0])
      cityI = pieces[1]
      populationI = int(pieces[2])
      areaI = int(pieces[3])
      countryI = pieces[4]
      list_item = rankI, cityI, populationI, areaI, countryI
    cities.append(list_item)
#   position = j
    cur.execute('SELECT city FROM LargestCities WHERE rank = ?', (rankI, ))   
#1. ? place holder   2.(  , ) is a tuple (need comma, space), instead of WHERE...
    try:       #try: to test if there are rows
        pos = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
        cur.execute('UPDATE LargestCities SET city = city WHERE rank = ?', (rankI, )) 
    except:
#if no rows, write a row, start with index 1
        cur.execute('''INSERT INTO LargestCities (rank, city, population, area, country) VALUES (?,?,?,?,?)''', (rankI, cityI, populationI, areaI, countryI))
#      j += 1   #increment word count, position
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#OUTPUT:
print " "
print "OUTPUT 1: PRINTING rows stored in table, displaying limited to 30 rows, showing from largest city (rank), including the continent (as last column), looked up from the CountryContinent table."
print "Rank City    Population  Area(/m2)  Country Continent"
#cities.sort(reverse=True)  #sort cities list, descending in rank 
sqlstr = 'SELECT * FROM LargestCities'   # if want to limit rows printed: LIMIT 100
for i in range(len(cities)):
    item0 = cities[i][0]
    item1 = cities[i][1]
    item2 = cities[i][2]
    item3 = cities[i][3]
    item4 = cities[i][4]
    item_cont = cities[i][4] 
    sqlstr = "SELECT continent FROM CountryContinent WHERE countryC = '" + item_cont + "'"
    for row in cur.execute(sqlstr):
        print item0, "",item1, "  ",item2, "  ", item3,  "  ", item4,  "  ",row[0]


print " "
print "OUTPUT 2: PRINT rows containing country starting with letter supplied by user, first 15. "
string_build  = None
string_build = ""
x = raw_input("Please enter a letter to select and print rows where country starts with letter, like 'C' for China: ")
like_str = "'" + x + '%' + "'"
string_build1 = 'like ' + like_str + 'LIMIT 15'
string_build  = "SELECT * FROM LargestCities WHERE country " + string_build1
sqlstr = string_build

for row in cur.execute(sqlstr):
     print str(row[0]), " ", row[1], " ", row[4]


cur.close()
