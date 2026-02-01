class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # create the prefix array 
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        # find the valid sections
        ans = 0
        for i in range(n - 1): 
            left = prefix[i]
            right = prefix[n-1] - prefix[i]

            if left >= right:
                ans += 1

        return ans