#!/usr/local/bin/python3
# 2015-01-13 
# Joseph Urbanski
# MPCS 50101
# Week 2 homework
# Chapter 8, Question 4 solution.

# Initialize the variable that will hold our input, setting to zero so the while loop executes below.
num = 0

# Prompt for input, looping until we get a positive integer...
while num <= 0:
	try:
		num = int(input("Please enter a positive integer:\n"))
		# ... while testing for non-positive integers...
		if num <= 0:
			print("That's not a POSITIVE INTEGER!  ", end="")
	# ... and any string input.
	except ValueError:
		print("That's not even a number!  ", end="")

# Output the start of our final output...
print("Your Syracuse sequence starting with ", num, " is: ", num, sep="", end="")

# ... then calculate the sequence, outputting the number at each iteration.
while num != 1:
	print(", ", end="")  # Output the sequence separator text first.
	# If even, divide by two...
	if num % 2 == 0:
		num = int(num / 2)
	# ... if odd, multiply by three and add one.
	else:
		num = int(3 * num + 1)
	# Output the number in the sequence.
	print(num, end="")

# Output some final text to make it look pretty.
print(".")
