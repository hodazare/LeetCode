class Solution(object):
    def twoSum(self, nums, target):
        partial_sum = {}
        result = []
        for i in range(len(nums)):
            second_num = target - nums[i]
            if second_num in partial_sum:
                result.append(i)
                result.append(partial_sum[second_num])
                return result
            else:
                partial_sum[nums[i]] = i
