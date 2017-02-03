#www.coursera.org: Python Data stuctures, course 2, week 5, chapter 9.

print "FUNCTION: Dictionaries: Enter hiking trails and distances, check for integer input, store in dictionary, "
print "and print name & distance of longest trail."

trails = dict()
bigword = None
bigcount = 0

print "Please enter the names of the hiking trails and each one's distance, enter 'done' when finished."
inp_tr = raw_input("Enter a name of a hiking trail: ")

key = 0
while inp_tr != 'done':
    key = inp_tr
    inp_dist = raw_input("Enter the trails's distance: ")
    trails[key] = inp_dist
    try: 
       if int(trails[key]) > 0:
          if trails[key] > bigcount:
              bigword = key
              bigcount = trails[key]
    except:
       print "Wrong input, this entry is ignored, enter only integers for distance."
       continue
    inp_tr = raw_input("Enter a name of a hiking trail: ")

print " "
print (trails)

print "The longest hiking trail is", bigword, "and it is", bigcount, "km long."

print " "

print "FUNCTION: Print the different tuples (key, value) moves in synchronized way."
print "The keys in the dictionary are:", trails.keys()
print "The values in the dictionary are:", trails.values()
print "The items in the dictionary are:", trails.items()

print " "

for aa,bb in trails.items():
    print aa, ":", bb, "km"
