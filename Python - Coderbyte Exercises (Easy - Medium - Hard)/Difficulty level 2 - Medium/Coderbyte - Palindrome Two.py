# Palindrome Two
#
# Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the
# parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false.
# The parameter entered may have punctuation and symbols but they should not affect whether the string
# is in fact a palindrome. For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.


def clean_up(strParam):
  return ''.join([s for s in strParam if s.isalpha()])

def PalindromeTwo(strParam):
  return clean_up(strParam).lower() == clean_up(strParam[::-1]).lower()


print(PalindromeTwo(input()))