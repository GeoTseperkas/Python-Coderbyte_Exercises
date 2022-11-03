# Chessboard Traveling
#
# Have the function ChessboardTraveling(str) read str which will be a string consisting of the location of a space on a
# standard 8x8 chess board with no pieces on the board along with another space on the chess board. The structure of
# str will be the following: "(x y)(a b)" where (x y) represents the position you are currently on with x and y ranging
# from 1 to 8 and (a b) represents some other space on the chess board with a and b also ranging from 1 to 8 where a > x
# and b > y. Your program should determine how many ways there are of traveling from (x y) on the board to (a b) moving
# only up and to the right. For example: if str is (1 1)(2 2) then your program should output 2 because there are only
# two possible ways to travel from space (1 1) on a chessboard to space (2 2) while making only moves
# up and to the right.


from math import factorial

def ChessboardTraveling(strParam):

  x = int(strParam.split(')(')[0].replace('(', '').split()[0])
  y = int(strParam.split(')(')[0].replace('(', '').split()[1])

  a = int(strParam.split(')(')[1].replace(')', '').split()[0])
  b = int(strParam.split(')(')[1].replace(')', '').split()[1])

  diff = (a-x) + (b-y)
  diff_a = a-x
  diff_b = b-y
  if diff == 2:
    return 2
  else:
    return int(factorial(diff_a+diff_b) / (factorial(diff_a)*factorial(diff_b)))


  return strParam


print(ChessboardTraveling(input()))