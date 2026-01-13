class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        right = count = ans = 0
        
        while right < len(nums): 
            if nums[right] == 1: 
                count += 1
                right += 1
            else: 
                ans = max(ans, count)
                right += 1
                count = 0

        ans = max(ans, count)
        return ans