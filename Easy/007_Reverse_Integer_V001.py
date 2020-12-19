# class Solution:
#     def reverse(self, x: int) -> int:


def reverse(x):
    if 0 <= x <= ((2 ** 31) - 1):
        y = int(str(x)[::-1])
        if -2 ** 31 <= y <= (2 ** 31) - 1:
            return y
        else:
            return 0
    elif (-2 ** 31) <= x < 0:
        y = int(str(x)[1::][::-1]) * -1
        if -2 ** 31 <= y <= (2 ** 31) - 1:
            return y
        else:
            return 0
    else:
        return 0


num = 1534236469
val = reverse(num)
print(f'Reverse of {num} is {val}')
