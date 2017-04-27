# https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/
import sys, getopt
from fractions import Fraction

inputfile = ''

def printHelp():
	print 'easy.py -i <inputfile>'

try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:",["ifile="])
except getopt.GetoptError:
	printHelp()
	exit()

for opt, arg in opts:
	if opt == '-h':
		printHelp()
		sys.exit()
	
	elif opt in ("-i", "--ifile"):
		inputfile = arg

with open(inputfile) as f:
    content = [x.strip() for x in f] 

for line in content:
	fractionContent = line.split(' ')
	fraction = Fraction(int(fractionContent[0]), int(fractionContent[1]))
	print "%d %d" % (fraction.numerator, fraction.denominator)