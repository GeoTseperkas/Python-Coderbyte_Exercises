# LCS
#
# Have the function LCS(strArr) take the strArr parameter being passed which will be an array of two strings containing
# only the characters {a,b,c} and have your program return the length of the longest common subsequence common to
# both strings. A common subsequence for two strings does not require each character to occupy consecutive positions
# within the original strings. For example: if strArr is ["abcabb","bacb"] then your program should return 3 because
# one longest common subsequence for these two strings is "bab" and there are also other 3-length subsequences
# such as "acb" and "bcb" but 3 is the longest common subsequence for these two strings.


def subs(x, y, i, j, dp={}):
  if i == 0 or j == 0:
    return 0
  k = (i, j)
  if k not in dp:
    if x[i-1] == y[j-1]:
      dp[k] = subs(x, y, i-1, j-1, dp) +1
    else:
      dp[k] = max(subs(x, y, i, j-1, dp), subs(x, y, i-1, j, dp))
  return dp[k]