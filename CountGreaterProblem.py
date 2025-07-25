'''Problem: Pivot Comparison - Greater or Smaller?
Problem Statement
Given an array of integers nums and a pivot value pivot, count how many numbers are less than the pivot (countLess) and how many are greater than the pivot (countGreater). Then, compare the two counts and return:

"greater" if countGreater > countLess,

"smaller" if countGreater < countLess,

"tie" if they are equal.

Input
An array nums of length n (1 ≤ n ≤ 10^5).

An integer pivot (-10^9 ≤ pivot ≤ 10^9).

Output
A string: "greater", "smaller", or "tie".

Examples
Input: nums = [1, 5, 3, 7, 2], pivot = 4
Output: "smaller"
Explanation:

countLess = 3 (elements 1, 3, 2 are < 4)

countGreater = 2 (elements 5, 7 are > 4)

Since 2 < 3, return "smaller".

Input: nums = [10, 2, 8, 5, 6], pivot = 6
Output: "tie"
Explanation:

countLess = 2 (elements 2, 5 are < 6)

countGreater = 2 (elements 10, 8 are > 6)

Since counts are equal, return "tie".

Input: nums = [9, 12, 15], pivot = 10
Output: "greater"
Explanation:

countLess = 1 (element 9 is < 10)

countGreater = 2 (elements 12, 15 are > 10)

Since 2 > 1, return "greater".

Constraints
The array may contain duplicates, but they are counted individually.

Numbers equal to the pivot are ignored (they don’t contribute to either count).

The solution must run in O(n) time with O(1) space (no extra data structures).

Follow-Up (Optional)
What if you needed to return the indices of the elements contributing to countGreater or countLess?

How would you handle multiple queries efficiently (e.g., for different pivots)?'''


def Solution(nums, pivot):
    countGreater = 0
    countLess = 0
    for num in nums:
        if num < pivot:
            countLess += 1
        elif num > pivot:  # Changed from 'else' to 'elif' to ignore nums[i] == pivot
            countGreater += 1

    if countGreater > countLess:
        return "greater"
    elif countLess > countGreater:
        return "smaller"
    else:
        return "tie"  # Added missing 'return'

print(Solution([1, 5, 3, 7, 2], 4))   # Output: "smaller" (3 < 2)
print(Solution([10, 2, 8, 5, 6], 6))  # Output: "tie"     (2 == 2)
print(Solution([9, 12, 15], 10))      # Output: "greater" (2 > 1)
print(Solution([4, 4, 4], 4))        # Output: "tie"     (0 == 0)


#What if you needed to return the indices of the elements contributing to countGreater or countLess?
def SolutionGetIndexes(nums, pivot):
    countGreaterIndexes = []
    countLessIndexes = []
    
    for idx, num in enumerate(nums):  # More Pythonic than range(len(nums))
        if num < pivot:
            countLessIndexes.append(idx)
        elif num > pivot:  # Explicitly ignore num == pivot
            countGreaterIndexes.append(idx)
    
    if len(countGreaterIndexes) > len(countLessIndexes):
        return countGreaterIndexes
    elif len(countLessIndexes) > len(countGreaterIndexes):
        return countLessIndexes
    else:
        return (countLessIndexes, countGreaterIndexes)  # Return both as a tuple
    
    test_result = SolutionGetIndexes([1, 5, 3, 7, 2], 4)
    print("Indices of elements less than pivot:", test_result[0])  # Should be [0, 2, 4]

    

    #How would you handle multiple queries efficiently (e.g., for different pivots)?
def SolutionManyPivots(nums,pivots):
    countGreater = 0
    countLess = 0
    dict_res = {}
    for idx, pivot in enumerate(pivots):
        for num in nums:
            if num < pivot:
                countLess += 1
            elif num > pivot:  # Changed from 'else' to 'elif' to ignore nums[i] == pivot
                countGreater += 1

        if countGreater > countLess:
             dict_res[pivot]="greater"
        elif countLess > countGreater:
            dict_res[pivot]= "smaller"
        else:
            dict_res[pivot]= "tie"  # Added missing 'return'
    return dict_res


#Solution below is Best for large n and m (e.g., n = 1e5, m = 1e5).
import bisect
from collections import Counter

def SolutionManyPivots(nums, pivots):
    nums_sorted = sorted(nums)
    #unter is a specialized subclass of Python's dict that is designed to count occurrences of hashable items (like numbers, strings, etc.). It stores the items as dictionary keys and their counts as dictionary values. For example:
#c = Counter('aabbcc')
#print(c)  # Output: Counter({'a': 2, 'b': 2, 'c': 2})
    freq = Counter(nums)
    result = {}
    
    for pivot in pivots:
        left_count = bisect.bisect_left(nums_sorted, pivot)
        right_count = len(nums) - left_count - freq.get(pivot, 0)
        
        if right_count > left_count:
            result[pivot] = "greater"
        elif left_count > right_count:
            result[pivot] = "smaller"
        else:
            result[pivot] = "tie"
    return result