#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = [1, 5, 2, 3, 11, 15, 7]
target = 9
n="dum"
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([nums[i], nums[j]])
            n="sa"
            break
    if(n=="sa"):
        break