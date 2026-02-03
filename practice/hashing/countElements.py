import collections
# why would they say count separately if they only wanted it once 
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        
        my_set = set(arr)
        
        for num in arr:
            if num + 1 in my_set:
                count += 1
                
        return count