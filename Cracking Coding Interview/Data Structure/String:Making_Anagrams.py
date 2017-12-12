#!/usr/bin/python

# stdin
# c d e         (a:string)
# a b c         (b:string)

# stdout
# 4     << correspond to the number of deletion needed to be done to both
            # string an anagram to each other

def number_needed(a, b):
    # initialize an array of 0 integer, with length 26, correspond to number of alphabets
    charcnt = [0] * 26
    # fill previous array by increments 1 for each elements of array a;
    # index for filling the array is a relative unicode code point to "a"; 
    for char in a:
        charcnt[ord(char) - ord('a')] += 1
    # followed by decreasing the value of previous array for each elements in array b by 1;
    for char in b:
        charcnt[ord(char) - ord('a')] -= 1
    total = 0
    # count the absolute value of the difference
    for value in charcnt:
        total += abs(value)
    return total

a = raw_input().replace(' ', '')
b = raw_input().replace(' ', '')

print number_needed(a, b)