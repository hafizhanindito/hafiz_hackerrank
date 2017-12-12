#!/usr/bin/python

# stdin
# 5 4           (n:int, k:int); n denotes the length of input array, k denotes the number of left rotation
# 1 2 3 4 5     (a:array); a correspong to the input array

# stdout
# 5 1 2 3 4     <<expected output

def array_left_rotation(a, n, k):
    # initialize counter and a new array
    ct = 0
    newarr = []
    # fill the new array starting from right part of input array first
    while k < n:
        newarr.append(a[k])
        k += 1
        ct += 1
    k = 0
    # fill the rest of the array from the rest of the input array
    while n - ct > k:
        newarr.append(a[k])
        k += 1
    return newarr

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))