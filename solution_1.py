#!/usr/local/bin/python3
# 2015-01-13 
# Joseph Urbanski
# MPCS 50101
# Week 2 homework
# Chapter 8, Question 1 solution.

# Prompt for input.
index = eval(input("What Fibonacci number do you want to find:\n"))

# Initialize variables.  
# numFib will be used as a place holder in the calculation, but will also hold 
# the final output.  Setting this to one allows us to skip the calculation loop
# for any number less than 3.
numFib = 1
# The first two Fibonacci numbers.  Will also be used in the calculation.
num1 = 1
num2 = 1

# Screen input for non-positive integers and re-prompt for input if necessary.
while index <= 0:
	index = eval(input("Please input a positive integer:\n"))

# Calculate the Fibonacci number.  Any number less than 3 will be '1', so only 
# loop for numbers greater than that.
while index > 2: 
	numFib = num1 + num2
	num1 = num2
	num2 = numFib
	index -= 1

# Output the Fibonacci number.
print("Your Fibonacci number is ", numFib, ".", sep="")

