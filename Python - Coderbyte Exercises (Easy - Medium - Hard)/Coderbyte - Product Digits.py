# Product Digits
#
# Have the function ProductDigits(num) take the num parameter being passed which will be a positive integer,
# and determine the least amount of digits you need to multiply to produce it. For example:
# if num is 24 then you can multiply 8 by 3 which produces 24, so your program should return 2 because there
# is a total of only 2 digits that are needed. Another example: if num is 90, you can multiply 10 * 9, so
# in this case your program should output 3 because you cannot reach 90 without using a total of 3 digits
# in your multiplication.


def ProductDigits(num):
  pairs = []

  for i in range(1, num+1):
    if num%i == 0:
      d = int(num/i)
      pair = len(str(d)) + len(str(i))
      pairs.append(pair)
  return min(pairs)


print(ProductDigits(input()))