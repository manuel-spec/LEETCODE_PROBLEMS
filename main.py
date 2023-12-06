
def twoSum(nums, target):
    sum = 0
    list = []
    pointers = [0, len(nums)-1]
    for i in range(len(nums)):
        sum += i
    for j in range(sum):
        if nums[pointers[0]] + nums[pointers[1]] > target:
            pointers[1] -= 1
        elif nums[pointers[0]] + nums[pointers[1]] < target:
            pointers[1] = len(nums) - 1
            pointers[0] += 1
        else:
            return pointers
