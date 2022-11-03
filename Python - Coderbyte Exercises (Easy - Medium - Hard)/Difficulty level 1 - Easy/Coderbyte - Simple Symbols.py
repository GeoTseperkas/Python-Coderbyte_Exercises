# Simple Symbols
#
# Have the function SimpleSymbols(str) take the str parameter being passed and determine if it
# is an acceptable sequence by either returning the string true or false.
# The str parameter will be composed of + and = symbols with several characters between them (ie. ++d+===+c++==a)
# and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false.
# The string will not be empty and will have at least one letter.


def SimpleSymbols(strParam):
  prev_c = strParam[0]
  if prev_c.isalpha():
    return False
  if strParam[-1].isalpha():
    return False
  for c in strParam[1:]:
    if c.isalpha() and prev_c != "+":
      return False
    if prev_c.isalpha() and c != "+":
      return False
    prev_c = c
  return True


print(SimpleSymbols(input()))