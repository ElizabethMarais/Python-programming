#www.coursera.org: Python Data stuctures, course 2.  OWN CODE

print "FUNCTION: Enter the names and year of birth dates of a few great opera men singers, determine which one is the youngest."
print "Possible entries are Carreras 1946, Pavarotti 1935, Domingo 1941, Watson 1966."

singers = dict()
bigword = None
bigcount = 0

print "Enter the names and birth dates of a few great opera men singers, enter 'done' when finished."
print "The program tests for integer input for year of birth date."
print " "

inp_nm = raw_input("Enter the name of a singer: ")

key = 0
while inp_nm != 'done':
    key = inp_nm
    inp_date = raw_input("Enter the singer's year of birth: ")
    singers[key] = inp_date
    try: 
       if int(singers[key]) > 0:
          if int(singers[key]) > bigcount:
              bigword = key
              bigcount = int(singers[key])
    except:
       print "Wrong input, this entry is ignored, enter only integers for birth year."
       continue
    inp_nm = raw_input("Enter a name of a singer: ")

print " "
print "Print DICTIONARY of Singers and birth dates stored."
print (singers)

print " "

print "The opera singer", bigword, "is the youngest, because he has the latest birth date namely", bigcount

print " "

print "FUNCTION: Print the different tuples (key, value) moves in synchronized way."
print "The keys in the dictionary are:", singers.keys()
print "The values in the dictionary are:", singers.values()
print "The items in the dictionary are:", singers.items()

print " "

for aa,bb in singers.items():
    print "The opera singer", aa, "has the birth date of", bb
