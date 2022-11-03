# Arith Geo II
# HIDE QUESTION
# Have the function ArithGeoII(arr) take the array of numbers stored in arr and return the string "Arithmetic"
# if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern.
# If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference
# between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied
# by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54].
# Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.


def ArithGeoII(arr):
    arith = True
    geo = True

    for n in range(1, len(arr) - 1):
        if arr[n + 1] - arr[n] != arr[n] - arr[n - 1]:
            arith = False
        if arr[n + 1] / arr[n] != arr[n] / arr[n - 1]:
            geo = False

    return "Arithmetic" if arith else "Geometric" if geo else -1


print(ArithGeoII(input()))