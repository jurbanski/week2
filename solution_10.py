#!/usr/local/bin/python3
# 2015-01-14 
# Joseph Urbanski
# MPCS 50101
# Week 2 homework
# Chapter 8, Question 10 solution.

# Import the sys module to allow us to read the input filename from command line arguments
import sys

# This function will prompt the user for a filename, then check to see if the file exists.  If the file does not exist, it prompts again.  If the file does exist, it returns the name of the file.
def prompt_for_filename():
        while True:
                filename = input("Please enter an input filename: ")
                try:
                        infile = open(filename, 'r')
                        return filename
                except OSError:
                        print("File not found!")

# Check to see if the filename has been provided as a command line argument, if it hasn't, prompt for user input with the prompt_for_filename() function.
try:
	filename = sys.argv[1]
	infile = open(filename, 'r')
	# CASE: File not found.
except OSError:
	print("File not found!")
	filename = prompt_for_filename()
	# CASE: No filename provided on the command line.
except IndexError:
	filename = prompt_for_filename()

# infile may not be set when the try block above finishes (out of scope if we have to prompt for a filename with prompt_for_filename()), so set it here.
infile = open(filename, 'r')

# Initialize some working variables.
leg = 0
odometer_prev = 0
miles_total = 0
gas_total = 0

# Loop over every line in the file.
for line in infile:
	# Split the current line into an array of strings.
	currline = line.split()
	# Set the current odometer to the first value in the current line.
	odometer_curr = float(currline[0])
	# Test to see if this is the first line in the file.
	if leg == 0:
		# If so, then:
		# Set the previous odometer to be the current odometer.
		odometer_prev = odometer_curr
		# Increment the leg counter.
		leg += 1
	else:
		# If not the first line, then:
		# Set the gas used to the second item in the current line.
		gas_used = float(currline[1])
		# Determine the miles traveled from the two odometer values.
		miles_traveled = odometer_curr - odometer_prev
		# Add the miles traveled on the current leg to the total.
		miles_total += miles_traveled
		# Add the gas used to the total.
		gas_total += gas_used
		# Calculate the MPG for this leg of the trip.
		mpg_curr = miles_traveled / gas_used
		# Output the MPG for this leg.
		print("Leg", leg, "MPG:", round(mpg_curr, 2))
		# Set the previous odometer to the current odometer for the next loop
		odometer_prev = odometer_curr
		# Increment the leg counter.
		leg += 1

# Finally, calculate the total average MPG for the trip and output that value.
print("Total MPG:", round(miles_total / gas_total, 2))
