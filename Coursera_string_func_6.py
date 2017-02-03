#www.coursera.org: Python Data stuctures, course 2
#string functions exercises

# obtain and print the host name from a line 
print "FUNCTION: obtain and print the host name from a line" 
text = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2016"
pos_st = text.find("@")
print pos_st
pos_end = text.find(" ",pos_st+1)  #find the first space, start to look after the @
print pos_end
domain = text[pos_st+1:pos_end]    #begin slice after the @ sign
print "The name of the domain is",domain

print " " 

print "FUNCTION: String functions testing
#isalnum()   # test if all char in string is alphanumeric  -letters and digits
#isdigit()  # test if all char in string is digits
def test_int():
    text = raw_input("Type in a number, containing only digits: ")
#print text ,"is", type(text)
    if text.isdigit(): 
       print "Yes, they are all numbers."
    else:
        print "Wrong input."
        test_int()

test_int()

print " "  #print open line

#test if string starts with "x"- NB case is important

line = raw_input("Please enter a string: ")
let = raw_input("Please enter the letter to see if the word starts with it: ")
if line.startswith(let): #answer is true, then execute next line
    print "Yes, the line starts with", let
else:
    print "No, the line does not start with the letter",let


print " "  #print open line
print "THE END"