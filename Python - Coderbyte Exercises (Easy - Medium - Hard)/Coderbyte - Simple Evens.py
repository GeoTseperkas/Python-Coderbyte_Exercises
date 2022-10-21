# Simple Evens
#
# Have the function SimpleEvens(num) check whether every single number in the passed in parameter is even.
# If so, return the string true, otherwise return the string false. For example: if num is 4602225 your program should
# return the string false because 5 is not an even number.



def SimpleEvens(num):
  for n in str(num):
    if int(n)%2 !=0:
      return False
  return True


print(SimpleEvens(input()))