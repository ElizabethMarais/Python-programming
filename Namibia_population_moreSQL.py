#www.coursera.org: Python Data structures, course 3, week 1 
print "PROGRAM FUNCTION: Program read data Namibia: for each region, the capital, population sensus counts in years 1991, 2001, 2011 and 2016. The percentage in growth between the different counts are calculated."
print "(Data obtained from https://www.citypopulation.de/Namibia.html; https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_Namibia)"

print " "
import sqlite3
conn = sqlite3.connect('namibiadb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Namibia_regions ''')

cur.execute('''
DROP TABLE IF EXISTS Namibia_cities ''')

cur.execute('''
CREATE TABLE Namibia_regions (Region TEXT, Capital TEXT, Area INTEGER, Pop_1991 INTEGER, Pop_2001 INTEGER,  Pop_2011 INTEGER,  Pop_2016 INTEGER, Perc_chng1 REAL, Perc_chng2 REAL, Perc_chng3 REAL)''')   

cur.execute('''
CREATE TABLE Namibia_cities (City TEXT, Region TEXT, Census_2001 INTEGER, Census_2011 INTEGER, Perc_chng REAL)''')    


region_list = list()
#City	Region	Census_2001	Census_2011	
handle = open('Namibian_population_data.txt')
print "PRINT EACH REGION AND ITS DETAILS"
for line in handle:
      line = line.lstrip()

#find the region
      pos_region = line.find(";")
      region = line[0:pos_region]
      region = region.lstrip()   #strip all blank spaces before it
#      print region

#find the capital
      pos_capital = line.find(';', pos_region +1)
      capital = line[pos_region +1:pos_capital]
      capital = capital.lstrip()          #strip all blank spaces before it
#      print capital

#find the area size
      pos_area = line.find(';', pos_capital +1)
      area = line[pos_capital+1:pos_area]
      area = int(area.lstrip())                #strip all blank spaces before it
#      print area 

#find the pop1991   
      pos_pop1991 = line.find(';', pos_area+1)
      pop1991 = line[pos_area+1:pos_pop1991]
      pop1991 = int(pop1991.lstrip())              #strip all blank spaces before it
#      print pop1991 

#find the pop2001      
      pos_pop2001 = line.find(';', pos_pop1991 +1)
      pop2001 = line[pos_pop1991+1:pos_pop2001]
      pop2001 = int(pop2001.lstrip())                #strip all blank spaces before it
#      print pop2001 

#find the pop2011   
      pos_pop2011 = line.find(';', pos_pop2001+1)
      pop2011 = line[pos_pop2001+1:pos_pop2011]
      pop2011 = int(pop2011.lstrip())              #strip all blank spaces before it
#      print pop2011 

#find the pop2016   
      pos_pop2016 = line.find(';', pos_pop2011+1)
      pop2016 = line[pos_pop2011+1:pos_pop2016]
      pop2016 = int(pop2016.lstrip())   
#      print pop2016 

      print "Region:", region, "  Capital:", capital, "  Area (square meter):", area, "m2" 
      print "Population 1991:", pop1991, "  Population 2001:", pop2001
      print "Population 2011:", pop2011, "  Population 2016:", pop2016

#calculate % going up no 1: population 2001 vs 1991
      diff1 = pop2001- pop1991
      perc_chng1 = round(float((float(diff1)/float(pop1991))*100),2)
      print "Percentage change 2001 vs 1991:", perc_chng1, '%'

#calculate % going up no 2: population 2011 vs 2001 
      diff2 = pop2011- pop2001
      perc_chng2 = round(((float(pop2011)-float(pop2001))/float(pop2001)*100),2)
      print "Percentage change 2011 vs 2001:", perc_chng2, '%'

#calculate % going up no 3: population 2016 vs 2011 
      perc_chng3 = round(((float(pop2016)-float(pop2011))/float(pop2011)*100),2)   #note first convert all numbers to float
      print "Percentage change 2016 vs 2011: ", perc_chng3, '%'
      print " "

      itemL = region, capital, area, pop1991, pop2001, pop2011, pop2016, perc_chng1, perc_chng2, perc_chng3
      region_list.append(itemL)

#region_list.sort    #if regions sorted descending: (reverse=True)
#print region_list

#      cur.execute('''INSERT INTO Namibia_regions (Region, Capital, Area, Pop_1991, Pop_2001, Pop_2011 , Pop_2016, Perc_chng1, Perc_chng2, Perc_chng3 ) VALUES (?,?,?,?,?,?,?,?,?,?)''', (region, capital, area, pop1991, pop2001, pop2011, pop2016, perc_chng1, perc_chng2, perc_chng3))
      cur.execute('''INSERT INTO Namibia_regions VALUES (?,?,?,?,?,?,?,?,?,?)''', (region, capital, area, pop1991, pop2001, pop2011, pop2016, perc_chng1, perc_chng2, perc_chng3))
conn.commit()


city_list  = list()
handle = open('Namibia_cities.txt')
print "PRINT THE CITIES, REGION AND CITY INHABITANTS SENSUS COUNTS OF 2001 & 2011"
for line in handle:
      line = line.lstrip()

#find the capital
      pos_city =  line.find(";")
      city = line[0:pos_city]
      city = city.lstrip()          #strip all blank spaces before it
#      print city

#find the region
      pos_region = line.find(';', pos_city +1)
      region = line[pos_city +1:pos_region]  
      region = region.lstrip()   #strip all blank spaces before it
#      print region

#find the city pop2001      
      pos_pop2001 = line.find(';', pos_region +1)
      pop2001 = line[pos_region +1:pos_pop2001]
      pop2001 = int(pop2001.lstrip())                #strip all blank spaces before it
#      print pop2001 

#find the city pop2011   
      pos_pop2011 = line.find(';', pos_pop2001+1)
      pop2011 = line[pos_pop2001+1:pos_pop2011]
      pop2011 = int(pop2011.lstrip())              #strip all blank spaces before it
#      print pop2011

#calculate % going up no 1: population 2011 vs 2001 
      diff = pop2011 - pop2001
      perc_chng = round(((float(pop2011)-float(pop2001))/float(pop2001)*100),2)
      print "Percentage change", city, "inhabitants 2011 vs 2001:", perc_chng, '%'

      itemC = city, region, pop2001, pop2011, perc_chng
      city_list.append(itemC)

      cur.execute('''INSERT INTO Namibia_cities (city, region, Census_2001, Census_2011, Perc_chng) VALUES (?,?,?,?,?)''', (city, region, pop2001, pop2011, perc_chng))
conn.commit()


print " "
print "OUTPUT 1: PRINT rows in Namibia regions info table."
print "Region  Capital  Area (m2)  Pop_1991  Pop_2001 Pop_2011   Pop_2016  Latest per_change"
sqlstr = 'SELECT * FROM Namibia_regions'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2], "  ",  row[3], "  ",  row[4], "  ", row[5], "  ", row[6], row[9], "%  "

print " "
print "OUTPUT 2: PRINT rows of a couple of Namibian cities info table, ordered by biggest growth in population descending."
print "City Region  City_pop2001 City_pop2011  Perc_chng"
sqlstr = 'SELECT * FROM Namibia_cities ORDER BY Perc_chng DESC'
for row in cur.execute(sqlstr):
     print row[0], " ", row[1], "  ", row[2],  "  ",  row[3], "  ",  row[4], "%  "

print " "
#COMBINED SQL STATEMENTS
print "OUTPUT 3: Print some information using COMBINED SQL STATEMENTS. "
print "City   Region  Area(m2)   Per_ch_city   Per_ch_area"
sqlstr = "SELECT Namibia_cities.City, Namibia_cities.Region, Namibia_regions.area, Namibia_regions.Perc_chng3, Namibia_cities.Perc_chng  FROM Namibia_cities JOIN Namibia_regions ON Namibia_cities.City = Namibia_regions.Capital"
for row in cur.execute(sqlstr):
    print row[0], " ", row[1], " ", row[2], "(m2) ",  row[3], "%  ", row[4], "%  "

print " "
#COMBINED SQL STATEMENTS
print "OUTPUT 4: User enter a region, and its info is displayed. "
print "City   Region  Area (m2)   Per_ch3   Per_ch"
string_build = ""
x = raw_input("Please enter a city name to search for: ")
like_str = "'" + x + '%' + "'"
string_build1 = 'like ' + like_str
string_build  = "SELECT * FROM Namibia_regions WHERE Namibia_regions.Capital " + string_build1
sqlstr = string_build
for row in cur.execute(sqlstr):
    print row[0], " ", row[1], " ", row[2], " ",  row[3], " ", row[4]

cur.close()
