#!/usr/bin/python3.6

# stdin
# 3             (:int) denoting the number of input tests
# {[()]}        (:string) << consisting of brackets only
# {[(])}        (:string)
# {{[[(())]]}}  (:string)

# stdout
# YES           << return YES if the brackets is balanced; else NO
# NO
# YES

def is_matched(expression):
    # init dict with keys of closing brackets (to be used for logical matching)
    pairs = {'}': '{', ']': '[', ')': '('}
    # init empty array to list unbalanced bracket
    stackarr = []
    # begin looping, adding to array if open bracket is found
    for c in expression:
        if c in pairs.values():
            stackarr.append(c)
    # if c is not open bracket, check if it could be used for balancing the most recent open bracket
        elif c in pairs:
            if not stackarr or pairs[c] != stackarr.pop():
                return False
    # if the stackarr is empty, than the brackets is properly balanced, and vice-versa
    return not stackarr

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")