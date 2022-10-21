# Letter Count
#
# Have the function LetterCount(str) take the str parameter being passed and return the first word with the
# greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest
# it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating
# letters return -1. Words will be separated by spaces.

def repeats(w):
    d = {}
    rep = 0
    for l in w:
        if l in d.keys():
            d[l] += 1
        else:
            d[l] = 1
    for n in d:
        if d[n] > 1:
            rep = rep + d[n]
    return rep


def LetterCount(strParam):
    lt = "-1"
    gc = 0

    for w in strParam.split():
        c = repeats(w)
        if c > gc:
            lt = w
            gc = c

    return lt


print(LetterCount(input()))