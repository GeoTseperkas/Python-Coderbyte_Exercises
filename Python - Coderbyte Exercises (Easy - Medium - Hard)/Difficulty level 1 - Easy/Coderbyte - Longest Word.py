# Longest Word
#
# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word
# in the string. If there are two or more words that are the same length, return the first word from the string
# with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers,
# for example "Hello world123 567"

def LongestWord(sen):
  max_word = ""
  for word in sen.split():
    w = ""
    for c in word:
      if c.isalpha() or c.isnumeric():
        w += c
    if len(max_word) < len(w):
      max_word = w
  return max_word


print(LongestWord(input()))