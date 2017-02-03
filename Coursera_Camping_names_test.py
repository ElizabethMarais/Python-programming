#www.coursera.org: Python Data stuctures, course 1, last exercise (testing longest and shortest)

# Write a program that repeatedly prompts a user for the names people at the Meiringskloof camping with Holtzhausens, 
# until the user enters 'done'. Once 'done' is entered, print out the longest and shortest name.
# code works, it tests that user does not enter numbers
# code does not work 100% if user enters two names with same length

largest = None
smallest = None
larg_len = 0
small_len = 0
print 'FUNCTION: User enter names, the longest and shortest name is printed."
print "Enter the names of the parties that camped together at Meiringskloof at Fouriesburg, Eastern Free State. Enter 'done' when finished."

while True:
    inp = raw_input("Enter a name: ")

    if inp == "done" : break
    try:
	inp_fl = float(inp)
	print "Please enter characters only."
    except:
    	strlen = len(inp)
	if smallest is None:
	    small_len = strlen
	    smallest = inp 
	if strlen > larg_len:
	    larg_len = strlen
	    largest = inp
	elif strlen < small_len:
	    small_len = strlen
            smallest = inp

def done(largest,smallest):
    print "The longest name is", largest 
    print "The shortest name is", smallest

done(largest,smallest)     