#!/usr/bin/env python3

# Solution:

def commonPrefix(string1, string2):

    """
    This function will take 2 strings as input parameters and compare for 
    matching characters. 
    Returns the matching chars
    """

    # initialize the var for matching strings
    match = ""
    len_str1 = len(string1)
    len_str2 = len(string2)
    i = 0
    j = 0
    while i <= len_str1 -1 and j <= len_str2 -1:
    
        if string1[i] != string2[i]:
            break

        # using f string print out the matching characters
        # print(f"{string1[i]} {string2[i]}")
        match += "".join(string1[i])
        i += 1
        j += 1

    return match


def longestPrefix(my_list):

    """
    This function takes the list of elements as input will compare the first word with the remaining words in the list.    
    Returns the count of prefix matched characters.
    """

    # initialize the counter for number of prefix characters
    number_of_prefix_chars = 0
    prefix_chars = ""

    # if length of list is 0 return
    if len(my_list) == 0:
        return ""

    # Get first element
    first_word = my_list[0]

    # iterate by comparing first element with all the remaining elements in the list
    for i in range(1, len(my_list)):
        prefix_chars = commonPrefix(first_word, my_list[i])

    print("The longest prefix is - %s" %prefix_chars)
    number_of_prefix_chars = len(prefix_chars)
    return number_of_prefix_chars
            


if __name__ == "__main__":
   
    # test case 1
    my_list = []
    print("\n1. List of elements - %s" %my_list)
    if len(my_list) == 0:
        print("The list should have a minimum of 1 element")

    # test case 2
    my_list = ["total", "totem", "tote"]
    print("\n2. List of elements - %s" %my_list)
    print("Number of characters in the longest prefix : ", longestPrefix(my_list))

    # test case 3
    my_list = ["total", "totem", "tote", "texas"]
    print("\n3. List of elements - %s" %my_list)
    print("Number of characters in the longest prefix : ", longestPrefix(my_list))

    # test case 4
    my_list = ["total", "totem", "tote", "texas", "cisco"]
    print("\n4. List of elements - %s" %my_list)
    print("Number of characters in the longest prefix : ", longestPrefix(my_list))


"""
Execution of Script:
====================

./prefix.py

1. List of elements - []
The list should have a minimum of 1 element

2. List of elements - ['total', 'totem', 'tote']
The longest prefix is - tot
Number of characters in the longest prefix :  3

3. List of elements - ['total', 'totem', 'tote', 'texas']
The longest prefix is - t
Number of characters in the longest prefix :  1

4. List of elements - ['total', 'totem', 'tote', 'texas', 'cisco']
The longest prefix is - 
Number of characters in the longest prefix :  0


"""
