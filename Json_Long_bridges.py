#Coursera Python Course 3, JSON schema
print "PROGRAM reads data text file of the world's longest bridges, determine which country bridges mostly built in," 
print "different ways of displaying data. Data includes Name, Span in meters, Date completed, Country."
print "When prompted, please enter 'Json long bridges.txt' as data file."

print " "

import json
import urllib2

file = raw_input("Enter text file with data: ")
#if file_input <> 'Json long bridges.txt': file_input == 'Json long bridges.txt'
print "Retrieving: ", file

connection = open(file)
data = connection.read()
info_data = json.loads(data)
info = info_data["data"]
print 'Retrieved',len(info),'items in list'

print " "
print "Bridges and relevant information extracted from Json data file and printed: "

country_dict = {}
bridge_list = list()
bridge_span = list()
most_country = {}
print " "
print "JSON OUTPUT:" 
for i in range(0, len(info)):
    print 'Name:',info[i]["name"]
    print 'Bridge span:',info[i]["span"]
    print 'Date completed:',info[i]["date"]
    print 'Country:',info[i]["country"]
    print " "

    name = str(info[i]["name"])
    span_num = int(info[i]["span"])
    date_item = int(info[i]["date"])
    country_nm = str(info[i]["country"])

    #build a dictionary of bridge name and country:
    country_dict[name] = country_nm   

    #compile the individual items to build a nested list
    item = name, span_num, date_item, country_nm
    bridge_list.append(item)

    item = span_num, name, date_item, country_nm
    bridge_span.append(item)


#determine in which country most bridges have been built in this file
for name, country in country_dict.items():
    most_country[country] = most_country.get(country,0) + 1   #determine how many times a country appear in the dictionary

bigcountry = None
bigcount = 0
for country, count in most_country.items():
       if bigcount is None or count > bigcount:
          bigcountry = country
          bigcount = count
print "The country in which the most bridges in this list have been built, is", bigcountry, "and it is", bigcount, "times."

print " "  
print "Bridges with highest and lowest spans and their details:"

print "Highest span: ", bridge_span[0][0], "meters"
print "Bridge name:", bridge_span[0][1]
print "Completed in: ", bridge_span[0][2]
print "Country: ", bridge_span[0][3]    

i = 0
print " "
#print last item in list, thus lowest span
for i in range(len(bridge_span)):
      if i == len(bridge_span)-1:
         print "Lowest span: ", bridge_span[0][0], "meters"
         print "Bridge name:", bridge_span[0][1]
         print "Completed in: ", bridge_span[0][2]
         print "Country: ", bridge_span[0][3]    




