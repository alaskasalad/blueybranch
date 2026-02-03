# input is not sorted 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hash = {}
        for i in range(len(nums)):
            # number currently on 
            num = nums[i]
            # the pair that would make the target 
            complement = target - num
            # check if its in hash map 
            if complement in my_hash:
                return[i, my_hash[complement]]
            # add the number we're on with its array location 
            my_hash[num] = i
            
        return [-1, -1]