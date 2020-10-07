#A palindrome checker
#A palindrome is a word which has the same meaning even when reversed
# Examples are :
# level, racecar, civic, stats etc

# This program aims at checking it

def is_palindrome(word):
    return word == word[::-1]

#print('racecar'[::-1])

print(is_palindrome('civic'))