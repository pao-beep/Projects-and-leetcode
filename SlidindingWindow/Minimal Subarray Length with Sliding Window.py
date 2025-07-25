"""Given an array of positive integers nums and a positive integer target,
 return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

from typing import List


def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    min_length = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0


def maxSubArrayLen(target: int, nums: List[int]) -> int:
    max_length = 0
    window_sum = 0
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        # Update max_length when sum >= target (but don't shrink the window yet!)
        if window_sum >= target:
            max_length = max(max_length, right - left + 1)

        # Reset window if sum drops below target (no larger window possible)
        if window_sum < target:
            left = right + 1
            window_sum = 0  # Reset sum for new window

    return max_length