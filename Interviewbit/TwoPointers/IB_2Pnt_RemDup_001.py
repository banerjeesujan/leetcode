class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        # Introduced this condition for only 1 element, say A = [0]
        if len(A) == 1:
            return 1

        cursor1 = 0
        cursor2 = cursor1 + 1
        while cursor1 < len(A) - 1:
            flag = False
            while cursor2 < len(A) - 1 and cursor1 < len(A) - 1 and A[cursor1] >= A[cursor2]:
                flag = True
                cursor2 += 1
            if flag:
                A[cursor1 + 1], A[cursor2] = A[cursor2], A[cursor1 + 1]

            cursor1 += 1

        # print(A)

        for num in range(len(A) - 1):
            if A[num] >= A[num + 1]:
                break
        else:
            return len(A)  # If break is not hit, it means the list has only unique elements in sorted array

        final_val = num + 1

        return final_val


    def removeDuplicates1(self, A):
        # B = set(A)
        # N = sorted(list(B))
        # return N
        ret_A = list()
        for i in A:
            if i not in ret_A:
                ret_A.append(i)

        return ret_A


    def removeDuplicates2(self, A):
        # This is incomplete
        for i in range(len(A) - 1):
            print(i)
            lo = i + 1
            if A[i] <= A[lo]:
                hi = lo + 1
                while hi < len(A):
                    print(lo, hi, A)
                    if A[hi] <= A[i]:
                        hi += 1
                    else:
                        A[lo], A[hi] = A[hi], A[lo]
                        break

        return A


# A = [-3, -3, 3, 3, 3, 5, 9, 11, 11, 13]
# A = [1, 1, 1, 1, 1, 1, 1]
# A = [1, 1, 1, 3, 3, 3, 3, 4]
# A = [0]
# A = [1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9]
# A = [1, 2, 3]
# A = [1, 2, 3, 3, 3]
A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
s = Solution()
print(s.removeDuplicates(A))
