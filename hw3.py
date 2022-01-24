# https://www.kite.com/python/answers/how-to-make-a-list-into-a-comma-separated-string-in-python
# https://docs.python.org/3/library/math.html
# https://stackoverflow.com/questions/35328953/how-to-compare-individual-characters-in-two-strings-in-python-3
# https://blog.finxter.com/python-list-of-lists/
# https://www.geeksforgeeks.org/writing-to-file-in-python/
# https://www.geeksforgeeks.org/find-path-to-the-given-file-using-python/
# https://stackoverflow.com/questions/14125781/new-folder-that-is-created-inside-the-current-directory

import math
import os
import csv

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

print("#####The answer to part 1 is: ")
if vowels("elephant") == True: # more vowels than consonants
	print("True \n")
if vowels("elephant") == False: # more consonants than vowels
	print("False \n")
if vowels("elephant") == None: # equal number of vowels and consonants
	print("None \n")

def volume(radius, height): # part 2
	volume = math.pi * height * math.pow(radius, 2) # pi x height x radius^2
	print("Volume calculated from radius", radius, "and height", height, "equals", volume, "\n")

print("#####The answer to part 2 is: ")
volume(5, 10)

def ToCSV(strings): # part 3
	combinedString = ",".join(strings) # joins together the elements in the list of strings and removes the quotations
	print(combinedString, "\n")

print("#####The answer to part 3 is ")
listOfStrings = ["pickle", "juice", "is", "sour"]
ToCSV(listOfStrings)

def listOfLists(lol): # part 4
	listComp = [x for l in lol for x in l] # using list comprehension to print list of lists as a single row
	FileOutput = open("hw3-listOfLists.txt", "w") # opening or creating file
	for element in listComp:
		FileOutput.write(element) # writing elements of the list into file
	FileOutput.close()
	actualFile = 'hw3-listOfLists.txt'
	print("Path of the file: ", os.path.abspath(actualFile), "\n") # grabbing path of file

a_list = [["I ","love "], ["eating ","medium "], ["rare ","steaks "]]
print("#####The answer to part 4 is: ")
listOfLists(a_list)

def ToList(fileName): # part 5
	with open(fileName) as file_a:
		readFile = csv.reader(file_a) # reading file data
		listOfRows = list(readFile) # converting CSV to list
		print(listOfRows, "\n")

file1 = open("hw3-part5.csv", "w") # creating CSV
file1.write("name,gpa,major\nPhong Vu,3.5,CS\nTina Martin,4.0,Biology\nJim Pain,2.8,History")
file1.close()
fileName = 'hw3-part5.csv'
print("#####The answer to part 5 is: ")
ToList(fileName)

def tryError(): # part 6
    while True:
        try:
            x = int(input("Please enter the first number: \n")) # taking in inputs from the user
            y = int(input("Please enter the second number: \n"))
            print(x/y, "\n") # prints the answer to the division
            break
        except ZeroDivisionError: # catches a ZeroDivisionError to throw warning
            print("Warning!!: This is a Zero Division Error!")

print("#####The answer to part 6 is: ")
tryError()

def noDup(intList): # part 7
    noDupList = [] # creating a second list to contain all elements without Dups
    for i in intList:
        if i not in noDupList: # checking if element is already in second list to ensure no dups
            noDupList.append(i)
    print("Original List: ", intList)
    print("List without duplicates: ", noDupList, "\n")

intList = [1,1,2,2,3,3,4,4,5,5] # original list with dups
print("#####The answer to part 7 is: ")
noDup(intList)

def newFolder(): # part 8
	currentDir = os.getcwd() # grabs the current working directory
	finalDir = os.path.join(currentDir, r'hw3-folder') # sets variable that creates a folder in current directory
	if not os.path.exists(finalDir): # checking if folder already exists
		os.makedirs(finalDir)
		print("has been completed \n")
	else:
		print("could not be created because it already exists \n")

print("#####The answer to part 8: ")
newFolder()