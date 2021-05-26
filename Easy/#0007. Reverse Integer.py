class Solution:
    def reverse(self, x):
        '''
        :type x: int
        :type sign: int
        :rtype result: int
        '''

        sign = int()
        result = int()

        # Determine if number is negative
        if x < 0:
            sign = -1
        else:
            sign = 1
        # end if

        result = abs(x)             # Get absolute value of x to elimnate leading 0s and negative sign
        result = str(result)[::-1]  # Convert to string and reverse order
        result = int(result)        # Convert back to integer
        result = sign * result      # Multipliy by 1 or -1 accordingly

        # Check if result is out of bounds
        if result < -pow(2, 31) or result > (pow(2, 31) -1):
            result = 0
        # end if

        return result
    # end def reverse
# end class Solution