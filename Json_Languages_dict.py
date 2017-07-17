print "PROGRAM reads a Json data file, 'Json_Languages_dict.json' about Languages of South-Africa and percentages spoken, and does a few queries on it."
print "Data obtained from 'https://en.wikipedia.org/wiki/Languages_of_South_Africa' "

import json
import urllib2

print " "
names_list = list()
file = 'Json_Languages_dict.json'
fh = open(file)
print "Retrieving languages data from a Json data file: ", file
connection = open(file)
data = connection.read()

with open("Json_Languages_dict.json", "r") as f:
	languages = json.load(f)

print 'Retrieved', len(languages),'items in list'

print " "
print "Languages of South-Africa and percentages spoken:" 
  
for language, percentage in languages.items():
    print 'Language:', language
    print 'Percentage:', percentage
    print " "
    
choice = raw_input("\nWhat language\'s percentage do you want to look up? ")
#choice = "Afri"
percentage_ch = None
for language, percentage in languages.items():
   language_ch = language
   if choice == language_ch:    #  (choice in language_ch) or (   test, as well as substring
      percent_ch = percentage

print "The percentage of", language_ch, "is", percent_ch , "%"

#determine which percentage is smallest
print " "
lang_list = list()
for language, percentage in languages.items():
    item_list = float(percentage), str(language)
    lang_list.append(item_list)

lang_list.sort()  
max = len(lang_list)
print "The language least spoken is", lang_list[0][1], "with percentage", lang_list[0][0], "%"
print "The language most spoken is", lang_list[max-1][1], "with percentage", lang_list[max-1][0], "%"
