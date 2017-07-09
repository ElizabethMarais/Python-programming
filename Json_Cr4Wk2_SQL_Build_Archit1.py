#Coursera Python Course 4: Using Databases
print "PROGRAM reads Json text files of Buildings, architects, and details (it uses 'BuildArchList.txt', 'BuildArchARCHList.txt' as default), it parses the words, stores info in a list. It prints the table rows in the database."

import sqlite3
conn = sqlite3.connect('Builddb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS BuildArch ''')

cur.execute('''
DROP TABLE IF EXISTS BuildArchARCH ''')

cur.execute('''
CREATE TABLE BuildArch (name TEXT, city TEXT, country TEXT, architect_id INTEGER, year INTEGER)''')

cur.execute('''
CREATE TABLE BuildArchARCH (Architect_Id INTEGER, Architect TEXT, Address TEXT, Continent TEXT)''') 

print " "

import json
import urllib2

build_list = list()
i = 0
j = 0
file = 'Json BuildArchList data.txt'
fh = open(file)
print "Retrieving BUILDINGS info from a Json data file: ", file

connection = open(file)
data = connection.read()
info_data = json.loads(data)
info = info_data["data"]
print 'Retrieved',len(info),'items in list'
print " "

for i in range(0, len(info)):
    print 'Name:', info[i]["name"]
    print 'City:', info[i]["city"]
    print 'Country:', info[i]["country"]
    print 'Architect id:', info[i]["arch_id"]
    print 'Year completed:', info[i]["year"]

    print " "

    #build a dictionary of bridge name and country:
    #country_dict[name] = country_nm   

    #compile the individual items to build a nested list

    name = str(info[i]["name"])
    city = str(info[i]["city"])
    country = str(info[i]["country"])
    architect_id = int(info[i]["arch_id"])
    year = int(info[i]["year"])

    item = name, city, country, architect_id, year
    build_list.append(item)
    position = j
    cur.execute('''INSERT INTO BuildArch (name, city, country, architect_id, year) VALUES (?,?,?,?,?)''', (name, city, country, architect_id, year))
    j += 1   #increment word count, position
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#===============================================
#Architects
BArch = list()
i = 0
j = 0
file = 'Json data BuildArchARCHList.txt' 
print "Retrieving ARCHITECTS from a Json data file: ", file

connection = open(file)
data = connection.read()
info_data = json.loads(data)
info = info_data["data"]
print 'Retrieved',len(info),'items in list'

for i in range(0, len(info)):
    print 'Architect id:', info[i]["arch_id"]
    print 'Name:', info[i]["name"]
    print 'Address:', info[i]["address"]
    print 'Continent:', info[i]["continent"]

    print " "

    #compile the individual items to build a nested list

    architect_id = int(info[i]["arch_id"])
    name = str(info[i]["name"])
    address = str(info[i]["address"])
    continent = str(info[i]["continent"])

    item = architect_id, name, address , continent
    BArch.append(item)
    position = j         
    cur.execute('''INSERT INTO BuildArchARCH (Architect_Id, Architect, Address, Continent) VALUES(?,?,?,?)''', (architect_id, name, address, continent))
    j += 1   #increment word count, position
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

print "SQL OUTPUT 1: Print Buildings from table:"
sqlstr = "SELECT * FROM BuildArch"
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "   ", row[4] 

print " "

print "SQL OUTPUT 2: Print Architects from table:"
sqlstr = "SELECT * FROM BuildArchARCH"
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3]

print " "
country_in = ""
print "SQL OUTPUT 3: User enters a country to list buildings and architect info."
country_in = raw_input("Please enter the country from you wish to see the buildings: ")
str_country = "'" + country_in + "%'"
sqlstr = "SELECT BuildArch.Country, BuildArch.Name, BuildArch.Year, BuildArchARCH.Architect, BuildArchARCH.Address FROM BuildArch JOIN BuildArchARCH ON BuildArch.Country like " + str_country + " AND BuildArchARCH.Architect_Id = BuildArch.Architect_Id"
print "Country	Building     Year  Architect  ArchAddress  "
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "   ", row[4]   

cur.close()


  

