#This file contains basic part-time data science prework examples
#It covers basic control flow in python -- If/Else, For, While, Exceptions, List Comprehensions, Iterators

#Part 1) If-Else

print 'The Python interpreter executes'
print 'code line by line\n'
print 'Sometimes decisions have to be made depending on certain conditions'

fileExists = True

#An 'if' statement is followed by an expression that evaluates to a Boolean.
#Note how the line following it only executes if expression evaluates to True. 
if fileExists:
	print 'file contents'

age = 18
if age < 18:
	print 'You are a child legally'

#An else clause is used whenever a mutually exclusive alternative exists.
#Execution then continues at the code in the else clause

#Age is NOT less than 18, so the 'else' clause gets executed instead.
if age < 18:
	print 'You are a child'
else:
	print 'You are an adult'

#Sometimes you may have multiple mutual exclusive outcomes. In that case, use an elif.
#Think of these as cascaded if-statements. If the first condition fails, go to the-
#first elif and see if that condition passes. If it does, execute the code, otherwise-
#go to the next one.
if age >= 65:
	print 'You are a senior'
elif age >= 18 and age < 65:
	print 'You are an adult'
elif age > 12 and age <18:
	print 'You are a teen'
else:
	print 'You are a child'					

#Part 2) For loops

#Sometimes you need to do the same thing over and over 
#For instance. Perhaps we need to convert a National Weather Service
#Warning from capital letters to lower case (Google this!!)

message = ['SMALL','CRAFT','ADVISORY']

#Bad way to do this
message[0] = message[0].lower()
message[1] = message[1].lower()
message[2] = message[2].lower()

print message

#Good way to do this
lowerMessage = []
for word in message:
	lowerMessage.append(word.lower())

print lowerMessage

#How does a for-loop like that work? What is the meaning of 'for word in message'
#A sequence object such as a list has a function __iter__() that returns an-
#iterator object for the list. A for loop calls that method.

it = message.__iter__()

#'it' is now an iterator object for the list. This object has a next() method
#that is used to get the next item in the list. A for loop will keep calling
#it until an exception is raised

print it.next()
print it.next()
print it.next()

try:
	it.next()
except StopIteration:
	print 'Looping ended'

#Note how in the above example, we had to define another list.
#We can also do this in place

for idx, word in enumerate(message): 
	message[idx] = word.lower()

print message	

#enumerate() returns an iterator for a sequence that looks like [(1,'SMALL'),(2,'CRAFT'),(3,'ADVISORY')]
#This is a list of tuples that then gets unpacked by the variables idx and word and then
#can be used in the loop body

#For-looping a set number of times.

#say we want to loop 5 times and print the word 'hello' 5 times
for i in xrange(5):    #Creates an xrange object which is iterable and contains values 0-4
	print 'hello'

#Part 3) While loops

#While loops are great when you need to run a loop until a condition is met

a_sorted = [2,16,46,78]
b_sorted = [1,4,54,63,93,108]   #Note how this list is bigger
merged = []

i = 0
j = 0

while i < len(a_sorted) and j < len(b_sorted):
	if a_sorted[i] <= b_sorted[j]:
		minimum = a_sorted[i]
		i += 1
	else:
		minimum = b_sorted[j]
		j += 1

	print minimum
	merged.append(minimum)

merged = merged + a_sorted[i:] + b_sorted[j:]
print merged

#Anyone recognize that routine?!?!

#Of course in Python things can be much easier...

merged = a_sorted + b_sorted
merged.sort()
print merged

#Part 4) Exceptions

#Sometimes things break in your code. Statements can raise errors in such instances

import sys
a = 5

sys.stdout.write("Enter an integer:")
b = int(sys.stdin.readline())
print a/b

#We can get (at least) two types of errors.

try:
	sys.stdout.write("Enter an integer:")
	b = int(sys.stdin.readline())
	print a/b
except ZeroDivisionError as e:
	print e
	print "Please enter a non-zero integer:"
except ValueError as e:
	print e
	print "Please enter an integer:"
finally:
	b = int(sys.stdin.readline())
	print a/b
	

#Part 5) List comprehensions

#Say we want a list of the perfect squares from 0 to 1000
import math
import pdb
a = range(1001)
perfect_squares = []

for integer in a:
	if math.sqrt(integer).is_integer():
		perfect_squares.append(integer)
print perfect_squares	

#This is perfect for a one-liner list comprehension

perfect_squares = [x for x in range(1001) if math.sqrt(x).is_integer()]
print perfect_squares











