#www.coursera.org: Python Data stuctures, course 3, week 1 
print "NETWORKED PROGRAMS exercises"

print " "
print "ROMEO: Accessing and printing 'romeo.txt' file from the PY4inf.com web page."
#PYTHON HTTP built in function
import urllib

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    print line.strip()

print " "
print "CLOWN: Accessing and printing the 'clown.txt' file from the PY4inf.com web page."
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/clown.txt')
for line in fhand:
   print line.strip()

print " "
print "Going from one to another web page."
import urllib
fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print line.strip()

print " "
print "Web page functions: count length of contents, read first 20 characters of page of www.dr-chuck.com."
import urllib
f = urllib.urlopen('http://www.dr-chuck.com')
contents = f.read()
f.close()
print len(contents)
print contents[0:20]


print " "
print "Web page functions: count length of contents of Linkedin.com page of Elizabeth Marais, and print first 100 characters."
f = urllib.urlopen('https://www.linkedin.com/in/elizabeth-marais-77717218/')
contents = f.read()
f.close()
print len(contents)
print contents[0:100]


