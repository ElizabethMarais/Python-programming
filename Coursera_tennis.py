#www.coursera.org: Python Data stuctures, course 2.  OWN CODE
print "FUNCTION: Enter the names and birth dates of a few great tennis stars, determine which one is the oldest."
print "Possible entries are: Roger Federer, 1982; Serena Williams, 1982; Andy Murray, 1988; Rafael Nadal, 1987; Maria Sharapova, 1988."

#print "The program tests for integer birth date input."

tennis = dict()
smallword = None
smallcount = 0

print "Enter the names and birth dates of a few great tennis stars, enter 'done' when finished."
print " "
    
inp_nm = raw_input("Enter the name of a tennis star: ")
key = 0
while inp_nm != 'done':
    key = inp_nm
    inp_date = raw_input("Enter the tennis star's birth year (only integers): ")
    tennis[key] = inp_date
    try: 
        if int(tennis[key]) > 0:
           if smallcount == 0:
              smallcount = int(tennis[key])
              smallword = key
           if int(tennis[key]) < smallcount:
              smallword = key
              smallcount = int(tennis[key])
    except:
       print "Wrong input, this entry is ignored, enter only integers for birth date."
       continue
    inp_nm = raw_input("Enter a name of a tennis star: ")

print " "
print (tennis)

print " "
print "Printing data in sentences."
for aa,bb in tennis.items():
    print "The tennis star", aa, "has the birth date of", bb

print " "
print "The tennis star", smallword, "is the oldest, because he has the earliest birth date namely", smallcount

print " "

print "FUNCTION: Print the different tuples (key, value), it moves in synchronized way."
print "The keys in the dictionary are:", tennis.keys()
print "The values in the dictionary are:", tennis.values()
print "The items in the dictionary are:", tennis.items()
