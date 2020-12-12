#!/usr/bin/env python3
###############################################################################
#
#
# Name:
#   Final2.py
#
# Input:
#   The first line has two space separated integers N and Q. 
#   The next N lines has source code with tags with zero or more attributes
#   The next Q lines contains queries
#
# Output:
#   Print the value of each query
#
# Purpose:
#   Write a program to process XML markup language as specified
#<tag1 value = "HelloWorld">
#<tag2 name = "Name1">
#</tag2>
#</tag1>
#tag1~value
#tag1.tag2~name
#
# Authors:
#   Pradeep Sampath
#   April 2018
###############################################################################


import os, sys
import json
import xml.etree.ElementTree as ET

if __name__  == "__main__" :
	N, Q = input("Enter 2 numbers : ").split(" ")
	N, Q = int(N), int(Q)
	print("\nN - %d, Q - %d" %(N,Q))
	
	if (N >= 1) and (N <= 20):
		print("\nN Constraint OK !")
	else:
		print("Usage: N should be between 1 to 20")
		exit()
		
	if (Q >= 1) and (Q <= 20):
		print("\nQ Constraint OK !")
	else:
		print("Usage: Q should be between 1 to 20")
		exit()
		
	bufferN = []
	while (N > 0):
		
		line = sys.stdin.readline().rstrip('\n')
		no_of_char = len(line)
		if no_of_char > 200:
			print("Usage: line exceeds 200 character limit")
			exit()
		line = line.replace("<", "")
		line = line.replace(">", "")
		bufferN.append(line)
		N -= 1
		
	print(bufferN)
	
	
	
	root = ET.Element(bufferN[0])
	root.set('value','HelloWorld')
	
	bufferN[1] = ET.Element(bufferN[1])
	root.append(bufferN[1])
	root[0].set('name','Name1')
	
	ET.dump(root)
	
	bufferQ = []
	while (Q > 0):
		no_of_char = len(line)
		if no_of_char > 200:
			print("Usage: line exceeds 200 character limit")
			exit()
		line = sys.stdin.readline().rstrip('\n')
		bufferQ.append(line)
		Q -= 1
		
	print(bufferQ)
	print("-------------")
	print(root.tag, root.attrib)
	print(root[0].tag, root[0].attrib)
	print("-------------")
	print("Output :")
	
	tgs, kys = bufferQ[1].split("~")
	#print(tgs, kys)
	if 'name' in root[0].attrib:
		print(root[0].attrib['name'])
	else:
		print("Not found!")
		
	if 'name' in root.attrib:
		print(root.attrib['name'])
	else:
		print("Not Found!")
			
			
	tgs, kys = bufferQ[2].split("~")
	#print(tgs, kys)
	if 'value' in root.attrib:
		print(root.attrib['value'])
	else:
		print("Not Found!")
