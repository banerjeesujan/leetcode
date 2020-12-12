import time


class Solution:
    # @param A : integer
    # @return a list of strings  Fizz Buzz FizzBuzz
    def fizzBuzz(self, A):
        retArray = list()
        for i in range(1, A + 1):
            if i % 3 == 0 and i % 5 == 0:
                retArray.append('FizzBuzz')
            elif i % 3 == 0:
                retArray.append('Fizz')
            elif i % 5 == 0:
                retArray.append('Buzz')
            else:
                retArray.append(str(i))

        return retArray


    def fizzBuzz2(self, A):
        resArray = list()

        retArray = [0] * (A + 1)

        for i in range(3, A + 1, 3):
            retArray[i] += 3

        for i in range(5, A + 1, 5):
            retArray[i] += 5

        for i in range(1, A + 1):
            if retArray[i] == 0:
                resArray.append(str(i))
            elif retArray[i] == 3:
                resArray.append('Fizz')
            elif retArray[i] == 5:
                resArray.append('Buzz')
            else:
                resArray.append('FizzBuzz')

        return resArray


start_time = time.perf_counter()
A = 50000
s = Solution()
print(s.fizzBuzz2(A))
end_time = time.perf_counter()
print(end_time - start_time)   # 0.054255205  # 0.05325494
