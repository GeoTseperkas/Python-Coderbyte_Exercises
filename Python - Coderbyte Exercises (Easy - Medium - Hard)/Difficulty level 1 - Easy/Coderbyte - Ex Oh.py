# Ex Oh
#
# Have the function ExOh(str) take the str parameter being passed and return the string true if there is
# an equal number of x's and o's, otherwise return the string false. Only these two letters will be entered
# in the string, no punctuation or numbers. For example: if str is "xooxxxxooxo" then the output should
# return false because there are 6 x's and 5 o's.


def ExOh(strParam):
  x_count = 0
  o_count = 0

  for c in strParam:
    if c == "x":
      x_count += 1
    if c == "o":
      o_count += 1

  return x_count == o_count


print(ExOh(input()))