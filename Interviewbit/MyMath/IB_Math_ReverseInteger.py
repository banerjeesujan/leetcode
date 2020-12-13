class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A < 0:
            B = int(str(A)[1::][::-1]) * (-1)
        elif A > 0:
            B = int(str(A)[::-1])
        else:
            return 0

        # signed integer range =  -2147483648 through 2147483647
        if B < (2 ** 31) * (-1)  or B > (2 ** 31) - 1:
            return 0
        else:
            return B


A = (2 ** 31) * (-1)
A = (2 ** 31) - 1
A = 7463847412
A = 8463847412
A = -8463847412
A = -9463847412
s = Solution()
print(s.reverse(A))


# -4294967296
#