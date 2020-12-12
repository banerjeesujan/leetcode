class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        if B == A:
            if C == D:
                return 1

        if C == A:
            if D == B:
                return 1

        if D == A:
            if B == C:
                return 1

        return 0


A = 3
B = 2
C = 3
D = 2
s = Solution()
print(s.solve(A, B, C, D))
