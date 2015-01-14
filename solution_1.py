#!/usr/local/bin/python3
# 2015-01-13 
# Joseph Urbanski
# MPCS 50101
# Week 2 homework
# Chapter 8, Question 1 solution.

# Initialize the variable that will hold our input, setting to zero so the while loop executes below.
index = 0

# Prompt for input, looping until we get a positive integer...
while index <= 0:
        try:
                index = int(input("What Fibonacci number do you want to find:\n"))
                # ... while testing for non-positive integers...
                if index <= 0:
                        print("That's not a POSITIVE INTEGER!  ", end="")
        # ... and any string input.
        except ValueError: 
                print("That's not even a number!  ", end="")

# Initialize variables.  
# numFib will be used as a place holder in the calculation, but will also hold 
# the final output.  Setting this to one allows us to skip the calculation loop
# for any number less than 3.
numFib = 1
# The first two Fibonacci numbers.  Will also be used in the calculation.
num1 = 1
num2 = 1

# Calculate the Fibonacci number.  Any number less than 3 will be '1', so only 
# loop for numbers greater than that.
while index > 2: 
	numFib = num1 + num2
	num1 = num2
	num2 = numFib
	index -= 1

# Output the Fibonacci number.
print("Your Fibonacci number is ", numFib, ".", sep="")

