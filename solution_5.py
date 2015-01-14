#!/usr/local/bin/python3
# 2015-01-13 
# Joseph Urbanski
# MPCS 50101
# Week 2 homework
# Chapter 8, Question 5 solution.

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


