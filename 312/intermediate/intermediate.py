# https://www.reddit.com/r/dailyprogrammer/comments/67q3s6/20170426_challenge_312_intermediate_next_largest/

inputValues = [1234, 1243, 234765, 19000]

def findNextLargest(number):
	# Convert the number to a string and then an array of characters
	number = list(str(number))

	swapIndex = None
	for index, val in enumerate(number):
		if index < len(number) - 1:
			if(val < number[index+1]):
				swapIndex = index

	if swapIndex is None:
		# this is the largest possible number
		return ''.join(number)
	
	swapWithIndex = number.index(sorted([x for x in number[swapIndex+1:] if x > number[swapIndex]])[0])

	temp = number[swapIndex]
	number[swapIndex] = number[swapWithIndex]
	number[swapWithIndex] = temp

	# order the remaining digits in descending order

	sortedRemainingDigits = sorted(number[swapIndex+1:])
	number = number[:swapIndex+1] + sortedRemainingDigits

	return ''.join(number)

for value in inputValues:
	print findNextLargest(value)