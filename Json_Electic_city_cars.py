print "PROGRAM reads a Json data file, 'Json Electric city cars data.json' about the latest electrical car models of the  world, it does a few queries on it."
print "Data obtained from 'https://en.wikipedia.org/wiki/List_of_electric_cars_currently_available' "

import json
import urllib2

print " "
top_speedL = list()
range_list = list()
file = 'Json Electric cars data.json'
fh = open(file)
print "Retrieving Electric city car models, data from a Json data file: ", file
connection = open(file)
data = connection.read()
info_data = json.loads(data)
print 'Retrieved', len(info_data),'items in list'

print " "
print "Current available Electric city car models and information:" 
  
info = info_data["data"]
print 'Retrieved', len(info),'items in list'

for i in range(0, len(info)):
    print 'Car Name:', info[i]["Car Name"]
    print 'Country:', info[i]["Country"]
    print 'Top speed:', info[i]["Top speed"]
    print 'Capacity:', info[i]["Capacity"]
    print 'Nominal Range:', info[i]["Nominal Range"]

    name = str(info[i]["Car Name"])
    country = str(info[i]["Country"])
    top_speed = int(info[i]["Top speed"])
    capacity = int(info[i]["Capacity"])
    nominal_range = int(info[i]["Nominal Range"])
 
    itemTS = top_speed, name, country, capacity, nominal_range
    top_speedL.append(itemTS)

    item_range = nominal_range, name, country,  top_speed, capacity
    range_list.append(item_range)

    print " "

#check in which country the most electric city cars have been listed
print " "
print "Count in each country the city electrical cars listed: "
countries = {}     #create an empty dict
for i in range(0, len(top_speedL)):
    country = top_speedL[i][2]
    countries[country] = countries.get(country, 0) + 1 
for country, count in countries.items():
   print country, ":", countries[country]

#test for one car's details
choice = raw_input("\nWhat electric car\'s information do you want to look up? ")
for i in range(0, len(top_speedL)):
  if choice in top_speedL[i][1]:
    print 'Car Name:', top_speedL[i][1]
    print 'Country:', top_speedL[i][2]
    print 'Top speed:', top_speedL[i][0]
    print 'Capacity:', top_speedL[i][3]
    print 'Nominal Range:', top_speedL[i][4]
    print " "
    continue

#list of top speeds
top_speedL.sort(reverse=True)
print " "
print "The city car with the highest speed: "
print 'Car Name:', top_speedL[0][1]
print 'Country:', top_speedL[0][2]
print 'Top speed:', top_speedL[0][0]
print 'Capacity:', top_speedL[0][3]
print 'Nominal Range:', top_speedL[0][4]

print " "
print "The city car with the lowest speed: "
max = len(top_speedL)
print 'Car Name:', top_speedL[max-1][1]
print 'Country:', top_speedL[max-1][2]
print 'Top speed:', top_speedL[max-1][0]
print 'Capacity:', top_speedL[max-1][3]
print 'Nominal Range:', top_speedL[max-1][4]


#determine highest and lowest Nominal Range
print " "
range_list.sort(reverse=True)

print "The city car with the highest Nominal range: "
print 'Car Name:', range_list[0][1]
print 'Country:', range_list[0][2]
print 'Top speed:', range_list[0][3]
print 'Capacity:', range_list[0][4]
print 'Nominal Range:', range_list[0][0]

print " "
print "The city car with the lowest Nominal range: "
max = len(range_list)
print 'Car Name:', range_list[max-1][1]
print 'Country:', range_list[max-1][2]
print 'Top speed:', range_list[max-1][3]
print 'Capacity:', range_list[max-1][4]
print 'Nominal Range:', range_list[max-1][0]
