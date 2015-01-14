#!/usr/local/bin/python3
# 2015-01-13 
# Joseph Urbanski
# MPCS 50101
# Week 2 homework
# Chapter 8, Question 4 solution.

num = 0

# Prompt for input.
while num <= 0:
	try:
		num = int(input("Please enter a positive integer:\n"))
		if num <= 0:
			print("That's not a POSITIVE INTEGER!  ", end="")
	except ValueError:
		print("That's not even a number!  ", end="")


# Screen input for strings and reprompt if necessary.
#while isinstance(num, str):
#	num = input("Please input a POSITIVE integer:\n")

# Screen input for non-positive integers and re-prompt for input if necessary.
#while num <= 0:
#	num = int(input("Please input a POSITIVE integer:\n"))

# Output the start of our final output...
print("Your Syracuse sequence starting with ", num, " is: ", num, sep="", end="")

# ..then calculate the sequence, outputting the number at each iteration.
while num != 1:
	print(", ", end="")  # Output the sequence separator text first.
	# If even, divide by two...
	if num % 2 == 0:
		num = int(num / 2)
	# ...if odd, multiply by three and add one.
	else:
		num = int(3 * num + 1)
	# Output the number in the sequence.
	print(num, end="")

# Output some final text to make it look pretty.
print(".")
