#!/usr/bin/env python3
###############################################################################
#
#
# Name:
#   Final1.py
#
# Input:
#   Takes a string as input that is used to search the database - spiderman
#
# Output:
#   return the value of total field in the returned JSON object
#
# Purpose:
#   Write an HTTP GET method to retrieve informration from a movie database. 
#
# Authors:
#   Pradeep Sampath
#   April 2018
###############################################################################

import sys
import os
import requests
import json


# Generic calls
def generic_get (url, header):
	r = requests.get(url, headers=header )
	return (r)

	
def getNumberOfMovies(substr):
	data_model_string = '/api/movies/search/?Title='
	url = "jsonmock.hackerrank.com"
	host = 'https://' + url + data_model_string + str(substr)
	print(host)
	headers = {'Content-Type': 'application/json'}
	r = generic_get(host, headers )
	status2 = r.status_code
	params = json.loads(r.text)
	parsed = json.dumps(params, indent=4)
	print(parsed)
	return params['total']
	
def getNameOfMovies(substr):
	data_model_string = '/api/movies/search/?Title='
	url = "jsonmock.hackerrank.com"	
	headers = {'Content-Type': 'application/json'}

	host = 'https://' + url + data_model_string + str(substr)
	r = generic_get(host, headers )
	params = json.loads(r.text)
	
	for page in range(params['total_pages']):
		print("\nPage - %d" %(page+1))
		host = 'https://' + url + data_model_string + str(substr) + '&page=' + str(page+1)
		print(host)
		
		r = generic_get(host, headers )
		params = json.loads(r.text)
		
		for n in range(len(params['data'])):
			print("%d - %s" %(n+1, params['data'][n]['Title']))
		
	

if __name__ == '__main__':
	movie_string = input("Enter the string to search: ")
	print("\nString length: ", len(movie_string))
	if (len(movie_string) > 0) and (len(movie_string) < 21):
		print("\nLength Constraint OK !")
	else:
		print("Usage: String should be 1 to 20 chars long")
		exit()
		
		
	total_no = getNumberOfMovies(movie_string)
	print("\nTotal number of movies having the title '%s' in their title: %d" %(movie_string,total_no))
	
	print(getNameOfMovies(movie_string))
	
	
	
	