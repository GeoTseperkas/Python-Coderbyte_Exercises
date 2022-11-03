# Letter Capitalize
#
# Have the function LetterCapitalize(str) take the str parameter being passed
# and capitalize the first letter of each word.
# Words will be separated by only one space.

def LetterCapitalize(strParam):
  return " ".join(s[0].upper() + s[1:] for s in strParam.split())


print(LetterCapitalize(input()))