# First Reverse
#
# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order.
# For example: if the input string is "Hello World and Coders" then your program should
# return the string sredoC dna dlroW olleH.

def FirstReverse(strParam):
  rev = ""
  for c in strParam[::-1]:
    rev += c
  return rev


print(FirstReverse(input()))