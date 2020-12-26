class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        # return the number of elements left in the array A after removing all the instances of B in array A.
        # First condition : B not present in A
        if B not in A:
            return len(A)

        # Second Condition : All elements of A are identical and B
        set_A = set(A)
        if len(set_A) == 1 and set_A.pop() == B:
            return 0

        cursor1 = 0
        cursor2 = len(A) - 1
        while cursor1 < cursor2:
            if A[cursor1] == B and A[cursor1] == A[cursor2]:
                cursor2 -= 1
            elif A[cursor1] == B and A[cursor1] != A[cursor2]:
                A[cursor1], A[cursor2] = A[cursor2], A[cursor1]
                cursor1 += 1
                cursor2 -= 1
                # print(cursor1, cursor2, A)
            else:
                cursor1 += 1

        print(cursor1, cursor2, A)

        for num in range(len(A)):
            if A[num] == B:
                break

        A = A[:num]

        # print(A)

        return num

    def removeElement2(self, A, B):
        # return the number of elements left in the array A after removing all the instances of B in array A.
        # First condition : B not present in A
        if B not in A:
            return len(A)

        pointer1 = 0
        pointer2 = pointer1 + 1
        while pointer2 < len(A):
            if A[pointer1] == B and A[pointer2] != B:
                A[pointer1], A[pointer2] = A[pointer2], A[pointer1]
                pointer1 += 1
                pointer2 += 1
            elif A[pointer1] == B and A[pointer2] == B:
                pointer2 += 1
            else:
                pointer1 += 1
                pointer2 += 1

        # print(A)

        for num in range(len(A)):
            if A[num] == B:
                break

        # A = A[:num + 1]

        return num

# A = [0, 0, 0, 0, 0, 0, 0, 0]
# B = 32
# B = 0
# A = [3, 4, 1, 1, 1, 3, 3, 5, 4, 2, 3]
# A = [3, 4, 4, 4]
# B = 4
# B = 1
# B = 5
# B = 32
A = [2, 0, 1, 2, 0, 3, 2, 2, 2, 1, 0, 0, 0, 1, 0, 0, 2, 2, 2, 3, 2, 3, 1, 2, 1, 2, 2, 3, 2, 3, 0, 3, 0, 2, 1, 2, 0, 0, 3, 2, 3, 0, 3, 0, 2, 3, 2, 2, 3, 1, 3, 3, 0, 3, 3, 0, 3, 3, 2, 0, 0, 0, 0, 1, 3, 0, 3, 1, 3, 1, 0, 2, 3, 3, 3, 2, 3, 3, 2, 2, 3, 3, 3, 1, 3, 2, 1, 0, 0, 0, 1, 0, 3, 2, 1, 0, 2, 3, 0, 2, 1, 1, 3, 2, 0, 1, 1, 3, 3, 0, 1, 2, 1, 2, 2, 3, 1, 1, 3, 0, 2, 2, 2, 2, 1, 0, 2, 2, 2, 1, 3, 1, 3, 1, 1, 0, 2, 2, 0, 2, 3, 0, 1, 2, 1, 1, 3, 0, 2, 3, 2, 3, 2, 0, 2, 2, 3, 2, 2, 0, 2, 1, 3, 0, 2, 0, 2, 1, 3, 1, 1, 0, 0, 3, 0, 1, 2, 2, 1, 2, 0, 1, 0, 0, 0, 1, 1, 0, 3, 2, 3, 0, 1, 3, 0, 0, 1, 0, 1, 0, 0, 0, 0, 3, 2, 2, 0, 0, 1, 2, 0, 3, 0, 3, 3, 3, 0, 3, 3, 1, 0, 1, 2, 1, 0, 0, 2, 3, 1, 1, 3, 2]
B = 2
# A = [4, 1, 1, 2, 1, 3]
# B = 1
# A = [ 1, 3, 3, 2, 1 ]
# B = 0
s = Solution()
print(s.removeElement2(A, B))