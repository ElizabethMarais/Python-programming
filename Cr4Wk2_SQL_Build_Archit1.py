#Coursera Python Course 4: Using Databases
print "PROGRAM reads text files of Buildings by night, architects, and details (it uses 'BuildArchList.txt', 'BuildArchARCHList.txt' as default), it parses the words, stores info in a list. It prints the table rows in the database."

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
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

import string
build_lst = list()
i = 0
j = 0
fname = 'BuildArchList.txt'
fh = open(fname)
for line in fh:
# BuildArch     name TEXT, city TEXT, country TEXT, architect_id INTEGER, year INTEGER 
  if line > "/n" :   #if it is not a blank line
            pos_name = line.find(';')
            name = line[0:pos_name]  #find the number, read from begin of line till comma 
            nameI = name.lstrip()
#            print nameI
 
            pos_city = line.find(';', pos_name +1)
            city = line[pos_name+1:pos_city]  #find the country, read after name till comma 
            cityI = city.lstrip()  
#            print cityI 

            pos_country = line.find(';', pos_city +1)
            country = line[pos_city +1:pos_country]  #find the country, read after name till comma 
            countryI = country.lstrip()  
#            print countryI

            #find the architect in rest of line:
            pos_arch_id = line.find(';', pos_country+1)
            arch_id = line[pos_country+1:pos_arch_id]
            arch_idI = int(arch_id.lstrip())
#            print arch_idI
  
            #find the year in rest of line:
            pos_year = line.find(';', pos_arch_id+1)   #line 50
            year = line[pos_arch_id+1:pos_year]
            year = year.lstrip()    #strip all blank spaces before it
            yearI = int(year)
#            print yearI

            item_list = nameI, cityI, countryI, arch_idI, yearI
            build_lst.append(item_list)      
            position = j
            cur.execute('''INSERT INTO BuildArch (name, city, country, architect_id, year) VALUES (?,?,?,?,?)''', (nameI, cityI, countryI, arch_idI, yearI))
            j += 1   #increment word count, position
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#print build_lst

import string
BArch = list()
i = 0
j = 0
fname = 'BuildArchARCHList.txt' 
fh = open(fname)
for line in fh:
   if line > "/n":   #if it is not a blank line
#find the Architect_Id, read from begin of line till comma 
         pos_Architect_Id = line.find(';')
         Architect_Id = line[0:pos_Architect_Id]              
         Architect_IdI = int(Architect_Id.lstrip())
#         print Architect_IdI 

#find the Architect, read after Architect_Id till comma 
         pos_Architect = line.find(';', pos_Architect_Id+1)
         Architect = line[pos_Architect_Id+1:pos_Architect] 
         ArchitectI = Architect.lstrip()
#         print ArchitectI 

 
#find Address, read after Architect till comma 
         pos_Address = line.find(';', pos_Architect+1)
         Address = line[pos_Architect+1:pos_Address] 
         AddressI = Address.lstrip()
#         print AddressI 
  
 #find the continent in rest of line:
         pos_Continent = line.find(';', pos_Address+1)
         Continent = line[pos_Address+1:pos_Continent]
         ContinentI = Continent.lstrip()    #strip all blank spaces before it
#         print ContinentI       

         item_list = Architect_IdI, ArchitectI, AddressI, ContinentI
         BArch.append(item_list)      
         cur.execute('''INSERT INTO BuildArchARCH (Architect_Id, Architect, Address, Continent) VALUES(?,?,?,?)''', (Architect_IdI, ArchitectI, AddressI, ContinentI))
conn.commit()
#NB: commit: all stuff done in memory, write back to disk

#OUTPUT
country_in = ""
print "OUTPUT 1: User enters a country to list buildings and architect info."
country_in = raw_input("Please enter the country from you wish to see the buildings: ")
str_country = "'" + country_in + "%'"
sqlstr = "SELECT BuildArch.Country, BuildArch.Name, BuildArch.Year, BuildArchARCH.Architect, BuildArchARCH.Address FROM BuildArch JOIN BuildArchARCH ON BuildArch.Country like " + str_country + " AND BuildArchARCH.Architect_Id = BuildArch.Architect_Id"
print "Country	Building     Year  Architect  ArchAddress  "
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "   ", row[4]   

print " "
print "OUTPUT 2: User enters an arthitect to list buildings designed by arthitect."
arch_in = raw_input("Please enter the Arthitect name you wish to see the buildings designed by. If you enter nothing, all rows will be displayed: ")   #('done' to end)
print "Architect  Building   Country    Year "
if arch_in <> "" or arch_in != 'done':
#  try:
    str_arch = "'" + arch_in + "%'"
    sqlstr = "SELECT BuildArchARCH.Architect, BuildArch.Name, BuildArch.Country, BuildArch.Year FROM BuildArch JOIN BuildArchARCH ON BuildArchARCH.Architect like " + str_arch + " AND BuildArchARCH.Architect_Id = BuildArch.Architect_Id"
    for row in cur.execute(sqlstr):
       print row[0], " ", row[1], "  ", row[2], "  ",  row[3]
#  except:
#      print "Wrong input, please enter an arthitect name."
#      continue
#  arch_in = raw_input("Please enter the arthitect you wish to see the buildings designed by: ")

cur.close()

