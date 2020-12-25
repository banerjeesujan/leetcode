class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A: list, B: int):
        # Return 1 if any such pair exists else return 0.
        A.sort()
        C = abs(B)
        i = 0
        for i in range(len(A)):
            j = len(A) - 1
            while j > i:
                # print(i, j, A[i], A[j])
                if A[j] - A[i] < C:
                    break
                elif A[j] - A[i] == C:
                    return 1
                else:
                    j -= 1

        return 0

    def solve2(self, A: list, B):
        # Fundoo solution from Interviewbit
        # Return 1 if any such pair exists else return 0.
        myset = set(A)
        for num in myset:
            myset.remove(num)
            if num + B in myset:
                return 1
            myset.add(num)

        return 0


A = [5, 10, 3, 2, 50, 80]
B = -7
B = -5
B = 5
B = -48
B = -70
# B = 6
# A = [-10, 20]
# B = -30
s = Solution()
print(s.solve2(A, B))
