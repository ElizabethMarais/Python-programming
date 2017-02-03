#www.coursera.org: Python Data stuctures, course 2, week 5, chapter 9.
#video after Ass 9.4: read in a text file, check which word is repeated most, and print the count

#print "FUNCTION: Read in a text file, check which word is repeated most, and print the count."
counts = dict()	
name = raw_input("Enter file name: ")
handle = open(name)
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
#print counts
for word, count in counts.items():
    if bigcount == None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount 