class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A == 0 and B != 0:
            return B
        if A != 0 and B == 0:
            return A

        if A < B:  # Ensuring that A always greater than B
            A, B = B, A

        if A % B == 0:
            return B

        n = (B // 2) + 1  # Half of the smaller number + 1
        # m = int(B ** 0.5) + 1  # Square Root of the smaller number + 1
        # prime_factors = list()

        hcf = 1
        i = 2
        while i <= n:
            while B % i == 0 and A % i == 0:
                hcf *= i
                B = B / i
                A = A / i

            i += 1

        return hcf

    def gcd2(self, A, B):
        if A == 0 and B != 0:
            return B
        if A != 0 and B == 0:
            return A

        if A < B:  # Ensuring that A always greater than B
            A, B = B, A

        if A % B == 0:
            return B

        factors = self.factor(B)

        for i in factors:
            if A % i == 0:
                return i

    def factor(self, B):
        fact = [1, B]
        for i in range(2, int(B ** 0.5) + 1):
            if B % i == 0:
                fact.append(i)
                fact.append(B // i)

        return sorted(fact, reverse=True)

    def gcd3(self, A, B):
        if B > A:
            A, B = B, A
        while B != 0:
            temp = B
            B = A % B
            A = temp
        return A


A = 60;
B = 108
A = 12;
B = 18
A = 16;
B = 25
A = 38;
B = 57
A = 6630;
B = 4199
s = Solution()
print(s.gcd3(A, B))
# print(s.factor(B))
