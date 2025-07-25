'''You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.'''
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # Helper function to solve the problem for a linear street
    def rob_linear(nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[ i -1], dp[ i -2] + nums[i])
        return dp[-1]

    # Case 1: Rob houses from 0 to n-2 (excluding the last house)
    case1 = rob_linear(nums[:-1])

    # Case 2: Rob houses from 1 to n-1 (excluding the first house)
    case2 = rob_linear(nums[1:])

    # Return the maximum of the two cases
    return max(case1, case2)

# Example usage:
nums = [2, 3, 2]
print(rob(nums))  # Output: 3

"""
Define the Subproblems:

Let dp1[i] represent the maximum amount of money that can be robbed from the first i houses, considering the first house.

Let dp2[i] represent the maximum amount of money that can be robbed from the first i houses, considering the second house.
Base Cases:

For dp1, the base case is dp1[0] = nums[0] (if there's only one house, rob it).

For dp2, the base case is dp2[0] = 0 (if there's only one house, and we start from the second house, we don't rob it).


Recurrence Relation:

For dp1, the recurrence relation is:
    dp1[i]= max(dp2[i-1],dp2[i-2]+nums[i])
For dp2, the recurrence relation is
    dp2[i]= max(dp2[i-1],dp2[i-2]+nums[i])
    
Final Result:

The result will be the maximum of the last elements of dp1 and dp2, but we need to exclude the last house in dp1 and the first house in dp2

"""