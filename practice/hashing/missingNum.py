class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        my_set = set(nums)
        
        for i in range(size):
            if i not in my_set:
                return i
            
        return size