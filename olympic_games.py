print "FUNCTION: Reading a data file, lists, sorting reverse order, determine in which city the most Summer Olympic games were held." 
print "Some output are: City where most venues were used, is Barcelona with 43 venues; city where most games were held is London, 3 times."

print " "
print "When prompted, please enter 'olympic_games.txt' as data file."
name = raw_input("Enter file to find the Summer Olympic games information: ")
if len(name) < 1: name = "olympic_games.txt"
name = "olympic_games.txt"

print " "
print "Information extracted from file and printed in complete sentences: "
city_list = list()
city_dict = {}
most_city = {}
most_list = list()
city_list_ven = list()
fh = open(name)
for line in fh:
            #find the year in line:
            year = line[0:4]  #find the year, read from begin of line for first four characters in file
            #find the city name in rest of line:
            pos_city = line.find(',',5)
            city = line[5:pos_city]
            city_name = city.strip()      #strip all blank spaces before it
            #find the number of venues in rest of line:
            venues = line[pos_city+1:]
            venues_num = venues.strip()    #strip all blank spaces before it

            print "In the year", year, "a Summer Olympic game were held in the city", city, "with", venues_num, "venues used."

            #build a dictionary of city and year:
            city_dict[year] = city_name 

            #compile the individual items to build a nested list
            item = year,city_name,venues_num
            city_list.append(item)

            #compile the individual items to build a nested list of Number of venues used, Year, city
            item = int(venues_num), year,city_name
            city_list_ven.append(item)

print " "
print "PRINT DICTIONARY of Year and City:"
print city_dict

print " "
print "TABLE of year, city and number of venues used, of Summer Olympic games: "
for i in range(len(city_list)):
    print city_list[i][0], city_list[i][1], "  ", city_list[i][2]
            
#determine in which city the most games have been held in this file
print " "
for year, city in city_dict.iteritems():
    most_city[city] = most_city.get(city,0) + 1   #determine how many times a city appear in the dictionary


print " "
print "TABLE of number of venues used, year, city of Summer Olympic games; venues used descending: "
print "Venues Year City"
city_list_ven.sort(reverse=True)
for i in range(len(city_list_ven)):
    print city_list_ven[i][0], city_list_ven[i][1], city_list_ven[i][2]

print "The most number of venues used in a Summer Olympic Game is", city_list_ven[0][0],"in the city", city_list_ven[0][2], "in the year", city_list_ven[0][1]

i = 0

for i in range(len(city_list_ven)):
    if i == len(city_list)-1:
        print "The least number of venues used in a Summer Olympic Game is", city_list_ven[i][0],"in the city", city_list_ven[i][2], "in the year", city_list_ven[i][1]


print " "
#build a list of cities and times they appear
for city, count in most_city.items():
    itemlist =  count, city
    most_list.append(itemlist)
most_list.sort(reverse=True)
print "TABLE of first five items in the list: number of times games held in that city, displaying descending: "
i = 0
while i < 5:
     print most_list[i][0], most_list[i][1]
     i += 1

bigcity = None
bigcount = 0
for city, count in most_city.items():
       if bigcount is None or count > bigcount:
          bigcity = city
          bigcount = count
print "The city in which the most Summer Olympic games where held, is", bigcity, "and it was", bigcount, "times."
