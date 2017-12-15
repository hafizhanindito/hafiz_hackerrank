#!/usr/bin/python3.6

# stdin

# 10        (:int) denotes the number of stdinput to be expected

# (a:int, [b:int]);   a = 1 >>> queue b to the end of queue, 
# a = 2 >>> dequeue the front part of queue,
# a = 3 >>> print element at the front of queue.
# 1 42      
# 2
# 1 14
# 3
# 1 28
# 3
# 1 60
# 1 78
# 2
# 2

# stdout
# 14        << after receives stdin "3"
# 14

# create object with methods that enables proper queing by first-come first-serve basis
# as well as the print method as required by the challenge
class MyQueue(object):
    def __init__(self):
        self.arr = []                
    
    def peek(self):
        return self.arr[0]
        
    def pop(self):
        del self.arr[0]
        
    def put(self, value):
        self.arr.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
