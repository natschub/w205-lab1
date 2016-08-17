#This file contains basic part-time data science prework examples
#It covers basic control flow in python -- Functions and Classes

#Part 1) Functions

#Functions allow you to modularize code by placing it in a named-block.
#You can then call these functions over and over.

def merge(a_sorted,b_sorted):

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
		merged.append(minimum)
	

	merged = merged + a_sorted[i:] + b_sorted[j:]

	return merged   #Functions end in a return statement.

#Here is how to call the function

a = [4,5,7,23,69,86,456,7892]
b = [1,65,78,567,1456]

sortedList = merge(a,b)
print sortedList

c = [45,67,78,456,678,1456]
d = [1,2,56,98,453,637]

sortedList = merge(c,d)
print sortedList

#Default Params

def power(base,power = 2):
	return base ** power

print power(4,5)
print power(4)

#Weird stuff could happen when using default mutables
def add_name(name,roster = []):
	roster.append(name)
	return roster

print add_name('John')
print add_name('Bob')
print dir(add_name)   #Let's see the object attributes

print add_name.__defaults__

#Note that we've used functions forever now
a = "hi"

print a.upper()   #Each object has functions defined on it. What would this look like without functions

#Part 2) Classes

#Classes allow us to define our own objects. They serve as blueprints for objects

class LinearRegression(object):        #All classes inherit from object
	
	def __init__(self,name):
		self.name = name
		self.coefficients = {}
		self.fit_results = {}

	def fit(self,x,y):
		print 'fitting coefficients...'
		self.coefficients = {'beta_0':3,'beta_1':5}

	def predict(self,x):
		return self.coefficients['beta_0'] + self.coefficients['beta_1']*x

	def get_name(self):
		return self.name

lin_reg = LinearRegression("Regression of housing values vs. socioeconomic status")
lin_reg.fit(4,5)  #Ignore the 4 and 5 for now. We will see what this will look like later
print lin_reg.get_name()
print lin_reg.predict(4)
print lin_reg.predict(2)	

lin_reg2 = LinearRegression("Regression of temperature vs. time")
lin_reg2.fit(6,8)  #Ignore the 6 and 8 for now. We will see what this will look like later
print lin_reg2.get_name()
print lin_reg2.predict(7)
print lin_reg2.predict(8)
