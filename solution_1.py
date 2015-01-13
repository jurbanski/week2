#!/usr/local/bin/python3
# 2015-01-13 
# Joseph Urbanski
# MPCS 50101

index = eval(input("What Fibonacci number do you want to find:\n"))
numFib = 1
num1 = 1
num2 = 1

while index <= 0:
	index = eval(input("Please input a positive integer:\n"))

while index > 2:
	numFib = num1 + num2
	num1 = num2
	num2 = numFib
	index -= 1

print("Your Fibonnaci number is ", numFib, ".", sep="")

