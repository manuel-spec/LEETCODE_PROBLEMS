class Solution(object):
    def twoSum(self, nums, target):
        nums = [-x for x in nums]
        target = -1 * target
        sum = 0
        result = []
        pointers = [0, len(nums)-1]
        for i in range(len(nums)):
            sum += nums[i]
        for j in range(len(nums)):
            if nums[pointers[0]] + nums[pointers[1]] > target:
                pointers[1] -= 1
            elif nums[pointers[0]] + nums[pointers[1]] < target:
                pointers[1] = len(nums) - 1
                pointers[0] += 1
            else:
                return [pointers[0], pointers[1]]


c = Solution()
print(c.twoSum([-1, -2, -3, -4, 10], 8))
