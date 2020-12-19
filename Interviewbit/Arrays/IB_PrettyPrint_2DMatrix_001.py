class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint2(self, A):
        for i in range(1, 2 * A):
            print()
            for j in range(1, 2 * A):
                # print(str(i) + str(j) + ' ', end='')
                # print(str((abs(min(i, j) - A) + 1)) + ' ', end='')
                print(str(max(abs(A - i), abs(A - j)) + 1) + ' ', end='')

        return None


    def prettyPrint(self, A):
        list_of_lists = list()
        for i in range(2 * A - 1):
            small_list = list()
            for j in range(2 * A - 1):
                small_list.append(max(abs((A - 1) - i), abs((A - 1) - j)) + 1)
            list_of_lists.append(small_list)

        return list_of_lists


A = 9
s = Solution()
print(s.prettyPrint(A))
print(s.prettyPrint2(A))
