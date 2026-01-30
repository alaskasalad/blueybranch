# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t): 
            if s[i] == s[t]:
                i += 1 
            j += 1 

        return i == len(s)