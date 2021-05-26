class Solution:
    def isPalindrome(self, x):
        '''
        type x: int
        type rev_num: int
        rtype result: bool
        '''

        rev_num = int()
        result = bool()

        # Check edge cases
        if x < 0 or x % 10 == 0:
            result = False
            rev_num = -1
        else:
            rev_num = self.getReverse(x)
        # end if

        # Check if reveresed num = original
        if x == rev_num:
            result = True
        else:
            result = False
        # end if

        return result
    # end def isPalindrome

    def getReverse(self, x):
        '''
        type x: int
        rtype rev_num: int
        '''

        rev_num = 0

        # While x > 0
        # Isolate last number
        # Create ones place
        # Add last number to ones place
        # Reduce original number by ones place

        return rev_num
    # end def getReverse
# end class Solution
