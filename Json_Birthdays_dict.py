#print "PROGRAM reads a Json data file, 'Json birthdays data_dict.json', and does a few calculations on it."

import json
import urllib2

names_list = list()
file = 'Json birthdays data_dict.json'
fh = open(file)
print "Retrieving birthdays data from a Json data file: ", file
connection = open(file)
data = connection.read()

print("Welcome to the Birthday game! We have the birthdays to:")

with open("Json birthdays data_dict.json", "r") as f:
	birthdays = json.load(f)

print 'Retrieved', len(birthdays),'items in list'

for name, birthday_string in birthdays.items():
    print 'Name:', name
    print 'Birthday:', birthday_string
    print " "
 
choice = raw_input("\nWho's birthday do you want to look up? ")
birthday_ch = None

for name, birthday_string in birthdays.items():
   if choice in name:    #test if person enters part of a name as well (substring)
      birthday_ch = birthday_string
      name_ch = name

print "The birthday of", name_ch, "is", birthday_ch 


#determine which person is the oldest
print " "
small_year = birthday_ch  #set small_year to an initial value to start comparing
oldest = None

for name, birthday_string in birthdays.items():
    year = int(birthday_string[6:])   #slice last 4 digits, convert to integer
    if year <= small_year: 
        small_year = year 
        oldest  = name
     
print "The oldest person listed here is", oldest, "and was born in", small_year 

#create a list of the month number, month name, and count of 0 initially
month_list = [[1,"January",0], [2,"February",0], [3,"March",0], [4,"April",0], [5,"May",0], [6,"June",0], [7,"July",0], [8,"August",0], [9,"September",0], [10,"October",0], [11,"November",0], [12,"December",0]]

for name, birthday_string in birthdays.items():
    month = birthday_string[3:5]
    incr_mt = int(month)
    month_list[incr_mt-1][2] = month_list[incr_mt-1][2] + 1

print " "
print "The total birthdays in each month are:"
for i in range(0, len(month_list)):
  print month_list[i][1], ":", month_list[i][2]

#user enter a year, displays all people born in that year
print " "
year_list = list()
year_in = raw_input("Please enter the year of birth to test for (e.g. 1955): ")
for name, birthday_string in birthdays.items():
     year = birthday_string[6:]
     name_display = name
     birthdate = birthday_string
     if year_in == year:
        item_list = name_display, birthdate
        year_list.append(item_list)

print "The following person(s) were born in this year:"
for i in range(0, len(year_list)):
   print year_list [i][0],  " ",   year_list [i][1]
