# https://www.reddit.com/r/dailyprogrammer/comments/67dxts/20170424_challenge_312_easy_l33tspeak_translator/
# Since 2 characters map to the 1 in l33tspeak I ended up removing one of them.

import sys, getopt

inputfile = ''

def printHelp():
	print 'easy.py -i <inputfile>'

characterMapping = {
	"A" : "4", 
	"B" : "6", 
	"E" : "3", 
	"I" : "1", 
	"M" : "(V)", 
	"N" : "(\)", 
	"O" : "0", 
	"S" : "5", 
	"T" : "7", 
	"V" : "\/", 
	"W" : "`//"
}

reverseCharacterMapping = {
	 "4" : "A",
	 "6" : "B",
	 "3" : "E",
	 "1" : "I",
	 "(V)" : "M",
	 "(\)" : "N",
	 "0" : "O",
	 "5" : "S",
	 "7" : "T",
	 "\/" : "V",
	 "`//" : "W"
}

def arrayFind(array, value):
	try:
		return array.index(value)
	except ValueError:
		return -1

def checkL33t(line):
	# Check each value in the character mapping, if it exists then we assume its l33t
	for l33t in characterMapping.values():
		if line.find(l33t) > -1:
			return True

	return False

def toL33t(line):
	newLine = ""
	for character in line:
		try:
			newLine = newLine + characterMapping[character.upper()]
		except Exception as e:
			newLine = newLine + character
	return newLine

def fromL33t(line):
	currentIndex = 0
	endIndex = len(line)
	newLine = ""
	while(currentIndex != endIndex):
		if(arrayFind(characterMapping.values(), line[currentIndex:currentIndex+1]) > -1):
			newLine = newLine + reverseCharacterMapping[line[currentIndex:currentIndex+1]]
			currentIndex = currentIndex + 1
		elif(arrayFind(characterMapping.values(), line[currentIndex:currentIndex+2]) > -1):
			newLine = newLine + reverseCharacterMapping[line[currentIndex:currentIndex+2]]
			currentIndex = currentIndex + 2
		elif(arrayFind(characterMapping.values(), line[currentIndex:currentIndex+3]) > -1):
			newLine = newLine + reverseCharacterMapping[line[currentIndex:currentIndex+3]]
			currentIndex = currentIndex + 3
		else:
			newLine = newLine + line[currentIndex:currentIndex+1]
			currentIndex = currentIndex + 1
	
	return newLine


try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:",["ifile="])
except getopt.GetoptError:
	printHelp()
	sys.exit()

for opt, arg in opts:
	if opt == '-h':
		printHelp()
		sys.exit()
	
	elif opt in ("-i", "--ifile"):
		inputfile = arg

with open(inputfile) as f:
    fileContent = [x.strip() for x in f] 


for line in fileContent:
	if(checkL33t(line)):
		print fromL33t(line).lower().capitalize()
	else:
		print toL33t(line)
	
