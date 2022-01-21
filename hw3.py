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

