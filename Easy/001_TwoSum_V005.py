def twoSum(nums, target):
    hash_dict = dict()
    for ind in range(len(nums)):
        if target - nums[ind] in hash_dict:
            return [hash_dict[target - nums[ind]], ind]
        else:
            hash_dict[nums[ind]] = ind
    print(hash_dict)

    return "not found"


# num_list = [3, 2, 4]; tg = 6
# num_list = [15, 13, 15, 15, 17, 19]; tg = 30
# num_list = [2, 7, 11, 15]; tg = 9
num_list = [3, 3]; tg = 6
print(twoSum(num_list, tg))
