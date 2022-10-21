# Vowel Count
#
# Have the function VowelCount(str) take the str string parameter being passed and return
# the number of vowels the string contains (ie. "All cows eat grass and moo" would return 8).
# Do not count y as a vowel for this challenge.

def VowelCount(strParam):
  vowels = ['a','e','o','u','i']
  count = 0
  for c in strParam:
    if c in vowels:
      count += 1
  return count


print(VowelCount(input()))