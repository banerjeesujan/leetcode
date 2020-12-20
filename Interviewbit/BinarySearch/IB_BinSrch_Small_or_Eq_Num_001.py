class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        left = 0
        right = n - 1

        count = 0

        while (left <= right):
            mid = int((right + left) / 2)

            # Check if middle element is less than or equal to B
            if (A[mid] <= B):

                # At least (mid + 1) elements are there whose values are less than or equal to key
                count = mid + 1
                left = mid + 1

            # If B is smaller, ignore right half
            else:
                right = mid - 1

        return count

    def solve2(self, A, B):
        lo = 0
        hi = len(A) - 1
        mid = (lo + hi) // 2
        counter = -10

        if B > A[hi - 1]:
            return hi

        if B < A[0]:
            return 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if A[mid] == B:
                counter = mid
                break
            elif A[mid] > B:
                hi = mid - 1
            else:
                lo = mid + 1

        counter = mid

        while counter < len(A) and A[counter] <= B:
            counter += 1

        return counter

    def solve3(self, A, B):
        counter = 0
        while counter < len(A) and A[counter] <= B:
            counter += 1

        return counter


# A = [1, 3, 3, 4, 6, 6, 6, 7, 8, 9]
# B = 6
A = [1, 1, 1, 1, 1]
B = 1
# A = [1, 3, 5, 7, 9]
# B = 4
s = Solution()
print(s.solve(A, B))