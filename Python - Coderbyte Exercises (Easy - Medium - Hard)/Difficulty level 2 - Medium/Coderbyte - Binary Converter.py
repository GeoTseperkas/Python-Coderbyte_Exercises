# Binary Converter
#
# Have the function BinaryConverter(str) return the decimal form of the binary value. For example:
# if 101 is passed return 5, or if 1000 is passed return 8.


def BinaryConverter(strParam):

  bin = 0
  for i, b in enumerate(strParam[::-1]):
    if b == "1":
      bin += 2**i

  return bin


print(BinaryConverter(input()))