##www.coursera.org: Python Data stuctures, course 2 
print "FUNCTION: Reading a data file, lists, sorting reverse order, determine which country bridges mostly built in," 
print "different ways of displaying data. Data includes Name, Span in meters, Date completed, Country."
print "When prompted, please enter 'long bridges.txt' as data file."

print " "
print "Bridges and relevant information extracted from file and printed in complete sentences: "
bridge_list = list()
country_dict = {}
most_country = {}
fh = open('long bridges.txt')
for line in fh:
        if line.find(',') > 0:
            pos_name = line.find(',')
            name = line[0:pos_name]  #find the bridge name, read from begin of line till comma 
            #find the span in rest of line:
            pos_span = line.find(',', pos_name+1)
            span = line[pos_name+1:pos_span]
            span_num = int(span.strip())       #strip all blank spaces before it, make integer
            #find the date in rest of line:
            pos_date = line.find(',', pos_span+1)
            date = line[pos_span+1:pos_date]
            date_num = date.strip()    #strip all blank spaces before it
            date_item = int(date_num)     #assign span to item in list
            #find the country in rest of line:
            pos_country = line.find(',', pos_date+1)
            country = line[pos_date+1:]
            country_nm = country.strip()      #strip all blank spaces before it

            print "The", name, "has a span of", span_num, "meters, was completed in",date_item,"in the country",country_nm

            #build a dictionary of bridge name and country:
            country_dict[name] = country_nm   

            #compile the individual items to build a nested list
            item = name,span_num,date_item,country_nm
            bridge_list.append(item)

print " "
print "LIST: Print bridge names and other information extracted from the file in list form: "
print bridge_list
            
#determine in which country most bridges have been built in this file
print " "
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
print "LIST: Sorted according to bridge names (ascending):"
bridge_list.sort()
print bridge_list

print " "
print "Print list items individually in a certain arrangement, using 'bridge span' in meters as sort item, in descending order."
print "Span (m)   Date   Country   Name"
bridge_country = {}
fh = open('long bridges.txt')
for line in fh:
        if line.find(',') > 0:
            pos_name = line.find(',')
            name = line[0:pos_name]  #find the bridge name, read from begin of line till comma 
            #find the span in rest of line:
            pos_span = line.find(',', pos_name+1)
            span = line[pos_name+1:pos_span]
            span_num = int(span.strip())       #strip all blank spaces before it, make integer
            #find the date in rest of line:
            pos_date = line.find(',', pos_span+1)
            date = line[pos_span+1:pos_date]
            date_num = date.strip()    #strip all blank spaces before it
            date_item = int(date_num)     #assign span to item in list
            #find the country in rest of line:
            pos_country = line.find(',', pos_date+1)
            country = line[pos_date+1:]
            country_nm = country.strip()      #strip all blank spaces before it
      
            #compile the individual items to build a nested list
            item = span_num,date_item,country_nm,name
            print span_num, date_item, country_nm, "  ", name
            bridge_list.append(item)

print " "

#print first item in list, thus highest span
print "The highest span is", bridge_list[0][1], "meters. It is", bridge_list[0][-2],"date completed",bridge_list[0][2], "in the country", bridge_list[0][3]    

i = 0
print " "
#print last item in list, thus lowest span
for i in range(len(bridge_list)):
      if i == len(bridge_list)-1:
        print "The smallest span is", bridge_list[i][0], "meters. It is", bridge_list[i][3],"date completed",bridge_list[i][1], "in the country", bridge_list[i][2]    


