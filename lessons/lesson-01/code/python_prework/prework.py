#This file contains basic part-time data science prework examples
#It covers basic data types in python -- Numerics, Sequences, Maps
#--------------------



#Part 1: Basic Data Types
# Numerics: The data type you will most likely use is the integer, float, and boolean
#  integers and floats

print 'Numerics:\n'   
a = 3 #a refers to an integer of value 3
b = 7

print a+b
print type(a+b) #type is a built-in function that gives us the type of an object

c = 3.14159 #c is now a float (basically a decimal number)
print a + c
print type(a + c) #Note that the result of adding an integer and a float is a float

#  boolean

print '\nBooleans:\n'
loveWins = True  #Can take on values True or False. The basic conditional variable
print type(loveWins)
print int(loveWins) #This is the integer equivalent of True
print loveWins + 4.5  #Booleans are automatically cast to integers or floats in arithmetic

# Part 2: Sequences -- Basic built-in data types that are a collection of objects with explicit ordering
#  Strings

print '\nStrings:\n'
#  Strings are ordered sequences of characters and are considered IMMUTABLE - meaning can't change 'em
a = "hello"   #The ordering: element 0 = "h", element 1 = "e",....
print a

#You will get to exceptions pretty soon here
try:
	a[2] = "f"  #A no-no
except TypeError as e:
	print str(e) + '. This error means that strings cannot be assigned to --> IMMUTABLE'

#  String objects implement generic sequence operations (can be invoked on any sequence type) such as:
#  Slicing, length, min/max, concatenation, testing membership...

print min(a)
print len(a)  #The string has a length of 5
print a[0]    #Slicing: The element at index 0 is "h"
print a[4]    #The 4th element is "o"
print a[1:3]  #Return the elements at index 1 through 2 -- "el"
print a[2:]   #Return all elements from index 2 to last -- "llo"

b = "world"
print a + b   #Addition of strings = concatenation. This means smash them together "helloworld"
print 'rld' in a + b #'in' keyword tests for membership of substring 'rld' in concatenation a+b

#  String objects also implement string-only methods
#  find, split, replace, etc..

print a.find("l") #This function returns first occurence of letter "l" --> 2
print a.split("l") #Splits the string on specified character --> Can you explain what happened?

print a.replace("l","z")   #Replaces any "l" character with "z".
#The astute reader will ask why this happens if strings are immutable. Turns out that these functions return a NEW string object:
print a   #Still the same 'ole a

#  Lists
print '\nLists:\n'

#  Lists are MUTABLE sequences. We can change their values using assignment. Also, they can hold any object
#  If you know C or Java, these are your array equivalents.
#  Internally, lists are nothing but arrays of references to their objects

a = [1,2,3,4]
print a
a[2] = 1000  #Assign 1000 to index 2. Allowed since lists are mutable

#  Lists have mutable sequence methods such as assignment that we saw above as well as list-only methods
#  reverse, remove, pop, etc..

a.reverse()   #Reverse elements of a list --> [4,1000,2,1]
a.remove(1)  #Search for element 1 (not index 1!!) and remove it --> [4,1000,2]
a.pop()      #Remove the last element of the list --> [4,1000]
print a

#  Lists are heterogeneous. They can hold different types of objects including other lists
c = [1,"hello",a]

#  ADVANCED (skip it if confused): Lists can hold ANY object including other lists,strings,functions,classes,modules!!
import pandas

weirdList = [1,a,"hello",str,a.append,pandas]  #Note how we imported pandas earlier. Pandas is bound to a Module object 
print weirdList

#Part 3) Mapping Structure
# Dictionary

# The most basic map structure that we will use is called the dictionary. 
# It holds values in key-value pairs.
# Order doesn't matter! That's the difference with say, lists

print '\nDictionary:\n'
dic = {'state': 'Colorado','population': 5800000, 'per capita income': 45983.56}
print dic   #note how 

#Accessing dictionary values
try:
	print dic['state']
except KeyError:
	print 'Your key doesn\'t exist'

try:
	print dic['avg age']
except KeyError:
	print 'Your key doesn\'t exist'

dic['avg age'] = 46.8   #To add a key-value pair, just make an assignment
print dic

#Keys can only be immutable objects. This has to do with a concept called hashing.
myList = [1,2,3]
try:
	dic[myList] = 'a list'    #This doesn't work because list is mutable and hence unhashable
except TypeError as e:
	print e	

keys = dic.keys()   #Use the keys() function to get a list of the dict Keys
print keys

print keys[2] in dic      #Boolean test if a key is in a dictionary









