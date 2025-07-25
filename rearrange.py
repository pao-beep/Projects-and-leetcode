"""The provided code defines a method rearrangeArray within the Solution class. This method rearranges elements in a list (nums) to ensure that no three consecutive elements form an increasing or decreasing sequence. Let me break it down step by step:
"""

#solution


from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #The loop iterates over the indices of the list, starting from 1 and stopping at len(nums) - 2. This ensures that we always have a previous (pre), current (current), and next (next) element to work with.
        for i in range(1, len(nums) - 1):
            pre = nums[i - 1]
            current = nums[i]
            next = nums[i + 1]

            # If block will run when we meet 1 2 3 or 6 4 2
            #This checks if the three consecutive elements form either:

            #An increasing sequence (pre < current < next), e.g., 1, 2, 3.
            #A decreasing sequence (pre > current > next), e.g., 6, 4, 2.

            if (pre < current < next) or (pre > current > next):
                # Swap next and current
                # For example:
                # 1 2 3 -> 1 3 2
                # 6 4 2 -> 6 2 4
                nums[i + 1], nums[i] = nums[i], nums[i + 1]

        return nums

