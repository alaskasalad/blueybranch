# what is the longest substring that contains at most one "0"
# cur keeps track of how many 0s we have 
# 11101110011
def find_length(s):
    left = res = cur = 0

    for right in range(len(s)):
        if s[right] == 0:
            cur += 1

        while cur > 1:
            if s[left] == 0: 
                cur -= 1
            left += 1

        res = max(res, right - left + 1)
