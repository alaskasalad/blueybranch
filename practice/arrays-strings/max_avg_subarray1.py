class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # len of array = k
        # find max average  
        
        cur = 0.00
        for i in range(k):
            cur += nums[i]
            
        res = float(cur/k)
        for i in range(k, len(nums)): 
            cur += nums[i] - nums[i - k]
            
            res = max(res, cur/k)
            
        return res 
            