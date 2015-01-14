#!/usr/local/bin/python3
# 2015-01-14 
# Joseph Urbanski
# MPCS 50101
# Week 2 homework
# Chapter 8, Question 10 solution.

import sys

# Set the filename variable to an empty string to avoid scope problems with the try block below
filename = ''

# Check to see if the filename has been provided as a command line argument, if it hasn't prompt for user input and check to see if that file actually exists
try:
	filename = sys.argv[1]
	infile = open(filename, 'r')
except OSError:
	print("File not found!")
except IndexError:
	while True:
		filename = input("Please enter an input filename:")
		try:
			infile = open(filename, 'r')
			break
		except OSError:
			print("File not found!")

# infile won't be set when the try block above finishes (out of scope), so set it here
infile = open(filename, 'r')

leg = 0
odometer_prev = 0
mpg_total = 0

for line in infile:
	currline = line.split()
	odometer_curr = int(currline[0])
	if leg == 0:
		odometer_prev = odometer_curr
		leg += 1
	else:
		gas_used = int(currline[1])
		mpg_curr = (odometer_curr - odometer_prev) / gas_used
		print("Leg", leg, "MPG:", round(mpg_curr, 2))
		mpg_total += mpg_curr
		leg += 1

print("Total MPG:", round(mpg_total, 2))
