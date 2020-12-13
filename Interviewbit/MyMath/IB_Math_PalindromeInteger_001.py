class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        # Input: 12121; Output: True
        # Input: 123; Output: False
        B = str(A)
        n = len(B)
        if n % 2 == 0:
            m = n // 2
        else:
            m = n // 2 + 1

        for i in range(m):
            if B[i] != B[n - i - 1]:
                return 0
        else:
            return 1


A = 123443261
s = Solution()
print(s.isPalindrome(A))