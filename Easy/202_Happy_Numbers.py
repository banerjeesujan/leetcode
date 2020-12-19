# class Solution:
#     def isHappy(self, n: int) -> bool;


def happy_numbers(n):
    item_list = list()
    while n != 1:
        full_num = str(n)
        digit_list = list()
        for num in full_num:
            digit_list.append(int(num))

        # print(digit_list)

        total = 0
        for vals in digit_list:
            total += vals ** 2

        n = total
        if total in item_list:
            return False

        item_list.append(n)
        print(n)

    return True


x = happy_numbers(20)
print(x)
