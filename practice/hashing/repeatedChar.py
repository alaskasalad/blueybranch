# Given a string s, return the first character to appear twice. 
# It is guaranteed that the input will have a duplicate character.
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        my_hash = {}

        for i in range(len(s)): 
            if s[i] in my_hash: 
                return s[i]

            my_hash[s[i]] = i

# _______________________________________________
# using a set because its more memory efficient 
# and i dont really even use the values
# space complexity could be Om where m is the num of allowable chars in the input 

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()

        for char in s: 
            if char in seen: 
                return char
            seen.add(char)

        return " "