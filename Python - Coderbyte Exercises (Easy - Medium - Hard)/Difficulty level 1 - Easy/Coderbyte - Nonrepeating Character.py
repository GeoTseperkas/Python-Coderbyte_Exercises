# Nonrepeating Character
#
# Have the function NonrepeatingCharacter(str) take the str parameter being passed, which will contain only alphabetic
# characters and spaces, and return the first non-repeating character. For example: if str is "agettkgaeee"
# then your program should return k. The string will always contain at least one character and there will always
# be at least one non-repeating character.


from collections import OrderedDict


def NonrepeatingCharacter(strParam):
    chars = OrderedDict()

    for c in strParam:
        if c not in chars.keys():
            chars[c] = 1
        else:
            chars[c] += 1

    for k, v in chars.items():
        if v == 1:
            return k
    return None


print(NonrepeatingCharacter(input()))