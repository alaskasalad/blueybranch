class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minval = 0
        total = 0

        for num in nums:
            total += num
            minval = min(minval, total)

        return -minval +1