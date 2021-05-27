class Solution:
    def romanToInt(self, s):
        '''
        :type s:                str
        :type char:             str
        :type roman_val:        dict
        :type running_total:    int
        :rtype result:          int
        '''

        char = str()

        running_total = int()
        result = int()
        idx = int()

        roman_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        idx = 0
        while idx < len(s):
            char = s[idx]

            if idx == len(s) - 1:
                running_total += roman_val[char]
                idx += 1
            elif char == 'I' and s[idx + 1] == 'V': #--------- Start Subtraction Cases ---------# 
                running_total += 4
                idx += 2
            elif char == 'I' and s[idx + 1] == 'X':
                running_total += 9
                idx += 2
            elif char == 'X' and s[idx + 1] == 'L':
                running_total += 40
                idx += 2
            elif char == 'X' and s[idx + 1] == 'C':
                running_total += 90
                idx += 2
            elif char == 'C' and s[idx + 1] == 'D':
                running_total += 400
                idx += 2
            elif char == 'C' and s[idx + 1] == 'M':
                running_total += 900
                idx += 2                            #--------- End Subtraction Cases ---------#
            else:
                running_total += roman_val[char]
                idx += 1
            # end if
        # end while

        result = running_total
        return result
    # end def romanToInt
# end class Solution