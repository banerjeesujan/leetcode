class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        alphalist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        outputstring = ''
        base = 26

        while A != 0:
            quo = A // base
            rem = A % base
            if rem == 0:
                outputstring += 'Z'
                A = quo - 1
            else:
                outputstring += alphalist[rem - 1]
                A = quo

        returnstring = outputstring[::-1]

        return returnstring


A = 943566
# A = 28 * 26
s = Solution()
print(s.convertToTitle(A))
