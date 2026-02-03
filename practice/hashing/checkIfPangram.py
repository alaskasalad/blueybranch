class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        my_set = set(sentence)
        
        if len(my_set) == 26:
            return True
        
        return False