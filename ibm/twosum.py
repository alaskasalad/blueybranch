class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range (len(nums)):
            res = target - nums[i]
            if res in hashmap: 
                return [i, hashmap[res]]
            hashmap[nums[i]] = i

        return []
