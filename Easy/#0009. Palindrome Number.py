class Solution:
    def isPalindrome(self, x):
        '''
        type x:         int
        type rev_num:   int
        rtype result:   bool
        '''

        rev_num = int()
        result = bool()

        # Check edge cases
        if x < 0 or x % 10 == 0:
            result = False
        else:
            rev_num = self.getReverse(x)
        # end if

        if x == rev_num:
            result = True
        else:
            result = False
        # end if

        return result
    # end def isPalindrome

    def getReverse(self, x):
        '''
        type x:             int
        type num_to_add:    int
        rtype rev_num:      int
        '''

        rev_num = 0
        num_to_add = int()

        # While x > 0
        while x > 0:
            num_to_add = x % 10         # Isolate ones place

            # Update reversed number
            rev_num = rev_num * 10      # Create new ones place
            rev_num += num_to_add       # Add isolated number to ones place
            
            # Update original number
            x = x // 10                 # Remove current ones place
        # end while

        return rev_num
    # end def getReverse
# end class Solution
