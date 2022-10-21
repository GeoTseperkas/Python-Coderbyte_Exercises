# Largest Pair
#
# Have the function LargestPair(num) take the num parameter being passed and determine the largest double digit
# number within the whole number. For example: if num is 4759472 then your program should return 94 because that
# is the largest double digit number. The input will always contain at least two positive digits.


def LargestPair(num):
  n = str(num)
  lpair = "0"
  for idx, i in enumerate(n[1:]):
    if int(n[idx]+i) > int(lpair):
      lpair = n[idx]+i
  return num if lpair ==0 else lpair


print(LargestPair(input()))