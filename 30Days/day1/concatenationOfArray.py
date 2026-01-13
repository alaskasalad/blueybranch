class Solution(object):
    def getConcatenation(self, nums):
        length = len(nums)
        ans = [0] * (2* length)
        for i in range(2* length):
            ans[i] = nums[i % length]
        
        return ans 