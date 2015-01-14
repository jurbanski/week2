#!/usr/local/bin/python3
# 2015-01-13 
# Joseph Urbanski
# MPCS 50101
# Week 2 homework
# Chapter 8, Question 5 solution.

# We'll need the math module to get a square root and the sys module to immediately quit the script if the number is found to be not prime.
import math
import sys

# Initialize the variable that will hold our input, setting to zero so the while loop executes below.
num = 0

# Prompt for input, looping until we get a positive integer...
while num <= 2:
	try:
		num = int(input("Please enter a positive integer greater than two:\n"))
		# ... while testing for integers less than or equal to two...
		if num <= 2:
			print("INVALID INPUT!")
	# ... and any string input.
	except ValueError:
		print("INVALID INPUT!")

# Set the divisor to be the upper bound of our number range, namely the square root of the number input above.
divisor = int(math.sqrt(num))

# Loop through our test until our divisor is equal to two...
while divisor >= 2:
	#... checking to see if it divides into our input number with no remainder...
	if num % divisor == 0:
		#... if it is, output that it is not prime and exit immediately...
		print("That number is *not* prime!")
		sys.exit(0)
	#... otherwise, decrement the divisor by one and loop through the test again.
	else:
		divisor -= 1

# If we hit the end of the while loop not having found an divisor that divides with no remainder, the number is prime.  Output that!
print("That number is prime!")
