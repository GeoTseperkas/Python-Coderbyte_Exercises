# Three Numbers
#
# Have the function ThreeNumbers(str) take the str parameter being passed and determine if exactly three unique,
# single-digit integers occur within each word in the string. The integers can appear anywhere in the word,
# but they cannot be all adjacent to each other. If every word contains exactly 3 unique integers somewhere within it,
# then return the string true, otherwise return the string false. For example: if str is "2hell6o3 wor6l7d2" then your
# program should return "true" but if the string is "hell268o w6or2l4d" then your program should return "false"
# because all the integers are adjacent to each other in the first word.


def three_nums(strParam):
  nums = []
  c = 0
  prev_s = ""
  cont = 1
  for s in strParam:
    if c == 0:
      prev_s = s
      c = 1
      continue
    if prev_s.isnumeric():
      if s.isnumeric():
        cont += 1
      if cont >= 3:
        return False
      if s.isalpha():
        cont = 1
      if prev_s not in nums:
        nums.append(prev_s)
    prev_s = s
  if prev_s.isnumeric():
    if prev_s not in nums:
      nums.append(prev_s)

  return len(nums) >= 3

def ThreeNumbers(strParam):
  for s in strParam.split():
    if three_nums(s) is False:
      return False
  return True


print(ThreeNumbers(input()))