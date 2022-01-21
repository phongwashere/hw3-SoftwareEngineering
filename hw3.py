# https://www.kite.com/python/answers/how-to-make-a-list-into-a-comma-separated-string-in-python
# https://docs.python.org/3/library/math.html
# https://stackoverflow.com/questions/35328953/how-to-compare-individual-characters-in-two-strings-in-python-3

import math

def vowels(input): # part 1
	vowels = 0
	consonants = 0
	for i in range(len(input)):
		if(input[i] == "a" or input[i] == "e" or input[i] == "i" or input[i] == "o" or input[i] == "u"):
			vowels += 1
		else:
			consonants += 1
	if(vowels > consonants):
		return True
	if(consonants > vowels):
		return False
	if(vowels == consonants):
		return None

print("The answer to part 1 is: ")
if vowels("elephant") == True: # more vowels than consonants
	print("True")
if vowels("elephant") == False: # more consonants than vowels
	print("False")
if vowels("elephant") == None: # equal number of vowels and consonants
	print("None")

def volume(radius, height): # part 2
	volume = math.pi * height * math.pow(radius, 2) # pi x height x radius^2
	print("Volume calculated from radius", radius, "and height", height, "equals", volume)

print("The answer to part 2 is: ")
volume(5, 10)

def csv(strings): # part 3
	combinedString = ",".join(strings) # joins together the elements in the list of strings and removes the quotations
	print(combinedString)

print("The answer to part 3 is ")
listOfStrings = ["pickle", "juice", "is", "sour"]
csv(listOfStrings)

