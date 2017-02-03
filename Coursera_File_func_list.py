#www.coursera.org:  Python Data stuctures, Course 2
#File and list handling: various functions exercises
# #www.coursera.org: Python Data stuctures, course 2
# file: open a file and check if line starts with a certain word, then split into a list and print the list
print "FUNCTION: Test if line start with a certain word, then split, and print the list."
xfile = open('EM_file_2.txt')

for line in xfile:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print words

print " "
print "THE END."
