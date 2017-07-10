#Coursera Python Course 4: Using Databases
print "PROGRAM reads a Json text file about Dalene Matthee 'Kringe in n bos' translations (it uses 'Json DaleneMatthee Kringe data.txt')."

import sqlite3
conn = sqlite3.connect('Kringedb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS DM_Kringe ''')

cur.execute('''
DROP TABLE IF EXISTS DM_Fiela ''')

cur.execute('''
CREATE TABLE DM_Kringe (year INTEGER, name TEXT, language TEXT)''')

#cur.execute('''
#CREATE TABLE DM_Fiela (year INTEGER, name TEXT, language TEXT)''') 

print " "

import json
import urllib2

books_list = list()
books_dict = {}
i = 0
j = 0
file = 'Json DaleneMatthee Kringe data.txt' 
fh = open(file)
print "Retrieving books data from a Json data file: ", file

connection = open(file)
data = connection.read()
info_data = json.loads(data)
info = info_data["data"]
print 'Retrieved',len(info),'items in list'
print " "
print "Dalene Matthee book, Kringe in n bos, was published and translated in the following versions:"

for i in range(0, len(info)):
    print 'Year:', info[i]["year"]
    print 'Name:', info[i]["name"]
    print 'Language:', info[i]["language"]

    print " "

     

    #compile the individual items to build a nested list

    year = int(info[i]["year"])
    name = str(info[i]["name"])
    language = str(info[i]["language"])

    #build a dictionary of book names and year published:
    books_dict[name] = year  

    item = year, name, language
    books_list.append(item)
    position = j
    cur.execute('''INSERT INTO DM_Kringe (year, name, language) VALUES (?,?,?)''', (year, name, language))
    j += 1   #increment 
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#===============================================

print "SQL OUTPUT 1: Print 'Kringe in bos' translations from table:"
sqlstr = "SELECT * FROM DM_Kringe"
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2]

print " "

cur.close()