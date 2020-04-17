"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
#*******************************************************
""" Two pointers can be used. At each step, move the pointer with less width. 
The idea is that we already have the maximum area using that point and there is no use to keep that in our calculations anymore. """

def maxArea(self, height):
    i, j = 0, len(height)-1
    max_area = 0
    while i < j:
        if height[i]< height[j]:
            min_w = height[i]
            i += 1
        else:
            min_w = height[j]
            j -= 1
        prod = min_w * (j - i + 1)
        max_area = max(max_area, prod)
    return max_area
