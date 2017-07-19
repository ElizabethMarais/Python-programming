#Coursera Python Course 4: Using Json schema
print "PROGRAM reads a Json data file, 'Json_Gem_stones_data.json', and does a few queries on it."
print "Data obtained from 'http://beadage.net/gemstones/' "

import json
import urllib2
import sqlite3
conn = sqlite3.connect('Gemstonesdb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS GemStones''')

cur.execute('''
CREATE TABLE GemStones (name TEXT, qualities TEXT)''')

print " "
names_list = list()
file = 'Json_Gem_stones_data.json'
fh = open(file)
print "Retrieving Gem stones data from a Json data file: ", file
connection = open(file)
gemstones = connection.read()

with open("Json_Gem_stones_data.json", "r") as f:
	gemstones = json.load(f)

print 'Retrieved', len(gemstones),'items in list'

print " "
print "Gem stones names and healing qualities listed:" 

j = 0  
for gemstone, qualities in gemstones.items():
    print 'Gem stone:', gemstone
    print 'Qualities:', qualities 
    position = j
    cur.execute('''INSERT INTO GemStones (name, qualities) VALUES (?,?)''', (gemstone, qualities))
    j += 1   #increment 
    print " "
conn.commit()


print " "
print "SQL OUTPUT 1: Print 'Gem stones and their healing qualities' from table:"
sqlstr = "SELECT * FROM GemStones"
for row in cur.execute(sqlstr):
     print row[0], ":  ", row[1]

print " "
print "SQL OUTPUT 2: Print a selected gem stone and its healing qualities from table:"
stone = raw_input("What gem stone and qualities do you want to look up? ") 
sqlstr = "SELECT * FROM GemStones WHERE GemStones.name like '" + stone + "%'"
for row in cur.execute(sqlstr):
     print row[0], ":  ", row[1]

print " "
print "SQL OUTPUT 3: Print all gem stones and its healing qualities where it contains the user entered quality from table:"
srch_qual = raw_input("Please enter a healing quality, to display all gem stones having it: ")
sqlstr = "SELECT * FROM GemStones WHERE qualities like '" + srch_qual + "%'"
for row in cur.execute(sqlstr): 
     print row[0], ":  ", row[1]

cur.close()