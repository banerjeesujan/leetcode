import string

alphalist = [''] + [x for x in string.ascii_uppercase]
# alphalist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# print(alphalist)


class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber2(self, A):
        quo = A // 26
        rem = A % 26
        if quo == 0:
            return alphalist[rem]
        else:
            if rem == 0:
                quo = quo - 1
                rem = 26
                if quo == 0:
                    return alphalist[rem]
                else:
                    return alphalist[quo] + alphalist[rem]
            else:
                return alphalist[quo] + alphalist[rem]

    def titleToNumber(self, A):
        # @param A : string
        # @return an integer
        alphalist = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
        output = 0
        base = 26
        pwr = 0
        B = A[::-1]
        for character in B:
            output += alphalist.index(character) * (base ** pwr)
            pwr += 1

        return output


A = 'BZ'
s = Solution()
print(s.titleToNumber(A))
