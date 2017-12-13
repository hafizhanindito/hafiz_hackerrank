#!/usr/bin/python

# stdin
# 6 4                           (a:int, b:int) a = the number of words in magazine; b for ransom 
# give me one grand today night (magazine:string)
# give one grand today          (ransom:string)

# stdout
# Yes   <<because there are enough words in the magazine to make ransom notes

def ransom_note(magazine, ransom):
    # init empty dictionary
    countermagz = {}
    # fill the dictionary with key=word in magazine and value to the number of that word occurences
    for available in magazine:
    # the dictionary.setdefault method return the value of key if it set; if not return 0
        countermagz[available] = countermagz.setdefault(available, 0) + 1    
    # the logic to determine if there are enough words in magazine to make ransom notes
    for key in countermagz.keys():
        for word in ransom:
            if key == word:
                countermagz[key] -= 1
                if countermagz[key] < 0:
                    return False
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"