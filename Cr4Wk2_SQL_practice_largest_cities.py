#Coursera Python Course 4: Using Databases
#NB: test data file: DATA must contain no FLOAT numbers, only INTEGERs
print "PROGRAM reads a text file line by line, (it uses 'largest_cities.txt' as default), data was obtained from https://en.wikipedia.org/wiki/List_of_cities_proper_by_population; "
print "it parses the words, stores info in a list. It prints the table rows in the database; it asks user to enter a letter to check for all countries starting with it."
print "Please enter the 'largest_cities.txt' as data file."

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS LargestCities''')

cur.execute('''
CREATE TABLE LargestCities (rank INTEGER, city TEXT, population INTEGER, area INTEGER, country TEXT) ''')

import string
words = list()
i = 0
j = 0
print " "
fname = raw_input('Please enter text file name: ')
if ( len(fname) < 1 ) : fname = 'largest_cities.txt'
fh = open(fname)
for line in fh:
  if line > "/n":   #if it is not a blank line
    pieces = line.split()
    for i in range(len(pieces)):
      word = pieces[i].translate(string.maketrans("",""), string.punctuation)   #remove all punctuation marks e.g. '.'
      rankI = int(pieces[0])
      cityI = pieces[1]
      populationI = int(pieces[2])
      areaI = int(pieces[3])
      countryI = pieces[4]
      list_item = rankI, cityI, populationI, areaI, countryI
      words.append(list_item)
      position = j
      cur.execute('SELECT city FROM LargestCities WHERE rank = ?', (rankI, ))   
#1. ? place holder   2.(  , ) is a tuple (need comma, space), instead of WHERE...
      try:       #try: to test if there are rows
        pos = cur.fetchone()[0]   
#brings back one row into memory, gives back as a list
        cur.execute('UPDATE LargestCities SET city = city WHERE rank = ?', (rankI, )) 
      except:
#if no rows, write a row, start with index 1
        cur.execute('''INSERT INTO LargestCities (rank, city, population, area, country) VALUES (?,?,?,?,?)''', (rankI, cityI, populationI, areaI, countryI))
      j += 1   #increment word count, position
  conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#OUTPUT:
print " "
print "PRINTING rows stored in table, limited to 30 rows. "
sqlstr = 'SELECT * FROM LargestCities order by rank ASC LIMIT 30'   # if want to limit rows printed: LIMIT 100

for row in cur.execute(sqlstr):
     print row[0], row[1], row[2], row[3], row[4]
     if row == 20: break

print " "
print "PRINT all rows starting with letter supplied by user, first 20. "
string_build  = None
string_build = ""
x = raw_input("Please enter a letter to select and print all rows where country starts with it, like 'C' for China: ")
like_str = "'" + x + '%' + "'"
string_build1 = 'like ' + like_str + 'LIMIT 15'
string_build  = "SELECT * FROM LargestCities WHERE country " + string_build1
sqlstr = string_build

for row in cur.execute(sqlstr):
     print str(row[0]), row[1], row[4]
     if row == 30: break

cur.close()