# Bitwise Two
#
# Have the function BitwiseTwo(strArr) take the array of strings stored in strArr, which will only contain two
# strings of equal length that represent binary numbers, and return a final binary string that performed the
# bitwise AND operation on both strings. A bitwise AND operation places a 1 in the new string where there is a 1 in
# both locations in the binary strings, otherwise it places a 0 in that spot. For example:
# if strArr is ["10111", "01101"] then your program should return the string "00101"

def BitwiseTwo(strArr):
  b = ""
  for b1, b2 in zip(strArr[0], strArr[1]):
    if b1 == "1" and b2 == "1":
      b += "1"
    else:
      b += "0"

  return b

print(BitwiseTwo(input()))