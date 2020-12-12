#!/usr/bin/env python3
###############################################################################
#
#
# Name:
#   Final3.py
#
# Input:
#   The first line has single integers N which is the number of elements in array. 
#   Each of the n subsequent lines contains a single integer describing element buffer[i]
#   where 0 <= i < n
#
# Output:
#   Print the value of max Difference
#
# Purpose:
#   Given an array of integers, compute the maximum difference any item and lower 
#   indexed smaller item for all pairs
#
# Authors:
#   Pradeep Sampath
#   April 2018
###############################################################################
#7
#2
#3
#10
#2
#4
#8
#1

import os, sys


def maxDifference(buffer):
	counter = 0
	max = 0
	result = 0
	for n in range(0,N):
		
		m = n+1
		print(n,m)
		counter = 0
		while counter < m:
			try:
				a, b = buffer[counter],buffer[m]
			except IndexError:
				break
			print("element 0 - %d, element 1 - %d" %(a,b))
			if b > a:
				print("We need to compute the difference - %d" %(b-a))
				result = b - a
			counter += 1
			if max < result:
				max = result
	if max == 0:
		print("No lower indexed smaller items for all items, return -1")
		return(-1)
	else:
		return(max)


if __name__  == "__main__" :


	N = input("Enter the numbers of elements in array : ")
	N = int(N)
	print("\nN = %d" %(N))
	
	if (1 <= N <= 200000):
		print("\nN Constraint OK !")
	else:
		print("Usage: N should be between 1 to 200000")
		exit()
	buffer_array = []
	for i in range(0,N):
		buffer_array.append(int(input()))
		
	print(buffer_array)
	final_output = maxDifference(buffer_array)
	print("Final output : %d" %final_output)