#Coursera Python Course 4: Using Databases
print "PROGRAM reads a text file of buildings that look spectacular by night, line by line, (it uses 'build_night.txt' as default), "
print "it parses the words, stores info in a list. It prints the table rows in the database."
print "It creates another table, cities and continents, reading the data from text tile, 'country_continent.txt'."
print "Please enter the 'Build_night.txt' when prompted as data file."

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS BuildNight''')

cur.execute('''
DROP TABLE IF EXISTS CountryContinent''')


cur.execute('''
CREATE TABLE BuildNight (name TEXT, country TEXT, architect TEXT, year INTEGER) ''')

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
  if line > "/n":   #if it is not a blank line
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

#print cont_list


import string
build_night_lst = list()
i = 0
j = 0
print " "
fname = raw_input('Please enter text file name of buildings by night: ')
if ( len(fname) < 1 ) : fname = 'build_night.txt'
fh = open(fname)
for line in fh:
# BuildNight (name TEXT, country TEXT, architect TEXT, year INTEGER,),
  if line > "/n":   #if it is not a blank line
            pos_name = line.find(',')
            name = line[0:pos_name]  #find the number, read from begin of line till comma 
            nameI = name.lstrip()
 
            pos_country = line.find(',', pos_name +1)
            country = line[pos_name+1:pos_country]  #find the country, read after name till comma 
            countryI = country.lstrip()  

            #find the architect in rest of line:
            pos_arch = line.find(',', pos_country+1)
            arch = line[pos_country+1:pos_arch]
            archI = arch.lstrip()   
  
            #find the language in rest of line:
            pos_year = line.find(',', pos_arch+1)
            year = line[pos_arch +1:pos_year]
            year = year.lstrip()    #strip all blank spaces before it
            yearI = int(year)
  
            item_list = nameI, countryI, archI, yearI
            build_night_lst.append(item_list)      
            position = j
            cur.execute('SELECT name FROM BuildNight WHERE architect = ?', (archI, ))   
#1. ? place holder   2.(  , ) is a tuple (need comma, space), instead of WHERE...
            try:       #try: to test if there are rows
               pos = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
               cur.execute('UPDATE BuildNight SET country = countryI WHERE name = ?', (nameI, )) 
            except:
#if no rows, write a row, start with index 1
               cur.execute('''INSERT INTO BuildNight (name, country, architect, year) VALUES (?,?,?,?)''', (nameI, countryI, archI, yearI))
            j += 1   #increment word count, position
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#print build_night_lst

#NEW PART: print ascending, thus from oldest to newest building
print " "
print "PRINT rows in year completed ascending (thus from oldest to newest building)."
print "Year  Name            Country    Architect"
sqlstr = 'SELECT * FROM BuildNight order by year ASC'
for row in cur.execute(sqlstr):
     print row[3], "", row[0], " ", row[1], "  ", row[2]


#OUTPUT: 
print " "
print "PRINT rows including the continent (as last column), looked up from the CountryContinent."
print "Year  Name            Country    Architect      Continent"
for i in range(len(build_night_lst)):
    item3 = build_night_lst[i][3]
    item0 = build_night_lst[i][0]
    item1 = build_night_lst[i][1]
    item2 = build_night_lst[i][2]
    item_cont = item1
    sqlstr = "SELECT continent FROM CountryContinent WHERE countryC = '" + item_cont + "'"
    for row in cur.execute(sqlstr):
       print  item3, "",item0, "  ",item1, "  ",item2, "  ",row[0]

cur.close()
