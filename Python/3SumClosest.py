"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Solution:
1- sort the list.
2- use two pointers at the beginning and at the end of the list (s,e).
3- if partial_sum = (nums[0] + nums[1] + nums[2]) closer to target update 'closest' variable.
*4- if partial_sum > target, then there is no need to have nums[s] in out calculation and by increasing s we can have a larger number.
"""

def threeSumClosest(nums, target):
        
        nums.sort()
        closest = target - (nums[0] + nums[1] + nums[2])
        
        n = len(nums)        
        
        for i in range(n):
            s = i+1
            e = n-1
                       
            while s < e:
                tmp = target - (nums[i] + nums[s] + nums[e])
                if tmp == 0:
                    return target
                
                if abs(tmp)<abs(closest):
                    closest = tmp
                
                if tmp > 0:
                    s += 1
                else:
                    e -= 1
        return target - closest
