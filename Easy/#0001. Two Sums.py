class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :type compliment: Dict{int: int}
        :rtype result: List[int]
        """

        compliment = dict()  # dictionary of possible complimentary numbers
        result = list() # variable to be returned

        # For every index and number in list nums
        for idx, num in enumerate(nums):
            # Check if complimetary number exists
            if num in compliment:                
                result = [compliment[num], idx]
            # else, record current number's compliment and index
            else:
                compliment[target - num] = idx
            #end if
        # end for

        return result
    # end def TwoSum
# end class Solution
