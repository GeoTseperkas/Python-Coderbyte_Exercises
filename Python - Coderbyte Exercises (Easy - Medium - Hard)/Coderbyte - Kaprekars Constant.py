# Kaprekars Constant
#
# Have the function KaprekarsConstant(num) take the num parameter being passed which will be a 4-digit number with
# at least two distinct digits. Your program should perform the following routine on the number:
# Arrange the digits in descending order and in ascending order (adding zeroes to fit it to a 4-digit number),
# and subtract the smaller number from the bigger number. Then repeat the previous step. Performing this routine will
# always cause you to reach a fixed number: 6174. Then performing the routine on 6174 will always give you
# 6174 (7641 - 1467 = 6174). Your program should return the number of times this routine must be performed until
# 6174 is reached. For example: if num is 3524 your program should return 3 because of the following steps:
# (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174.



def asc(n):
  m = ''.join(sorted(str(n), reverse = True))
  return int(m + (4-len(m))*'0')


def desc(n):
  m = ''.join(sorted(str(n)))
  return int(m + (4-len(m))*'0')


def kc(n, t):
  ds = str(asc(n) - desc(n))
  d = int(ds + (4-len(ds))*'0')
  if d== 6174:
    return t
  else:
    return kc(d, t+1)

def KaprekarsConstant(num):
  return kc(num, 1)

print(KaprekarsConstant(input()))