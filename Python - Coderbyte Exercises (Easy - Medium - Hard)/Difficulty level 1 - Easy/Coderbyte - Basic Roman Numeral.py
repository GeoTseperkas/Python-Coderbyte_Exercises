# Basic Roman Numerals
#
# Have the function BasicRomanNumerals(str) read str which will be a string of Roman numerals.
# The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000.
# In Roman numerals, to create a number like 11 you simply add a 1 after the 10, so you get XI. But to create a number
# like 19, you use the subtraction notation which is to add an I before an X or V (or add an X before an L or C).
# So 19 in Roman numerals is XIX.
#
# The goal of your program is to return the decimal equivalent of the Roman numeral given. For example:
# if str is "XXIV" your program should return 24.

def BasicRomanNumerals(strParam):

  rd = {}
  rd["I"] = 1
  rd["V"] = 5
  rd["X"] = 10
  rd["L"] = 50
  rd["C"] = 100
  rd["D"] = 500
  rd["M"] = 1000

  prev_c = strParam[0]
  c = 0
  subd = False
  for r in strParam[1:]:
    if rd[prev_c] < rd[r]:
      c = c + (rd[r]- rd[prev_c])
      subd = True
    elif subd is not True:
      c += rd[prev_c]
      subd = False
    else:
      subd = False
    prev_c = r

  return c if subd else c + rd[r]


print(BasicRomanNumerals(input()))