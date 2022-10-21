# Snake Case
#
# Have the function SnakeCase(str) take the str parameter being passed and return it in proper snake case format where
# each word is lowercased and separated from adjacent words via an underscore. The string will only contain letters
# and some combination of delimiter punctuation characters separating each word.
# For example: if str is "BOB loves-coding" then your program should return the string bob_loves_coding.


def SnakeCase(strParam):
  strParam = strParam.replace("}", " ").replace("{", " ").replace("'", " ").replace("\"", " ").replace("]", " ")\
      .replace("[", " ").replace(")", " ").replace("(", " ").replace("@", " ").replace("%", " ").replace("!", " ")\
      .replace("*", " ").replace("-", " ").replace("_", " ").replace("%", " ").replace("^", " ").replace("$", " ")\
      .replace("#", " ")
  return '_'.join(strParam.lower().split())

print(SnakeCase(input()))