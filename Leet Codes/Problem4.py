nums = [1, 5, 2, 3, 11, 15, 7]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([nums[i], nums[j]])
            break
    break