def mySoln(inputArr):
		# Write your code here
		memo1 = [0] * len(inputArr) 
		memo2 = [0] * len(inputArr) 
		memo3 = [0] * len(inputArr) 
		sum1 = 0
		sum2 = 0 
		sum3 = 0
		if len(inputArr) ==0:
			return 0
		if len(inputArr) ==1:
			return inputArr[0]
		memo1[0] = inputArr[0]
		memo2[0] = inputArr[0]
		memo3[0] = inputArr[0]
		if len(inputArr) > 1:
			memo1[1] = max(inputArr[0],inputArr[1])
			memo2[1] = max(inputArr[0],inputArr[1])
			memo3[1] = max(inputArr[0],inputArr[1])
		for i in range (2,len(inputArr)):
			memo1[i] = max(memo1[i-1], inputArr[i]+memo1[i-2])

		for j in range(len(inputArr)):
			memo2[j] = max(memo2[j-1], inputArr[j]+memo2[j-2])
		
		# for k in range(len(inputArr)):
		# 	memo3[k] = max(memo3[k-1], inputArr[k]+memo3[k-2])
		
		sum1 = memo1[-1]
		sum2 = memo2[-1]
		#sum3 = memo3[-1]
		return max(sum1,sum2)


def max_chocolates(jars):
    if not jars:
        return 0
    if len(jars) == 1:
        return jars[0]
    
    prev_max = jars[0]
    curr_max = max(jars[0], jars[1])
    
    for i in range(2, len(jars)):
        new_max = max(prev_max + jars[i], curr_max)
        prev_max, curr_max = curr_max, new_max
    
    return curr_max

# Example Usage
jars = [5, 3, 4, 11, 2]  # 5 + 11 = 16 (optimal)
print(max_chocolates(jars))  # Output: 16

"""The max_chocolates function is designed to solve a variation of the "House Robber Problem," where the goal is to maximize the number of chocolates collected from a series of jars without taking chocolates from two consecutive jars. This constraint ensures that no two adjacent jars are selected, making it a dynamic programming problem.

The function begins by handling edge cases. If the input list jars is empty, it returns 0 because there are no chocolates to collect. If there is only one jar, it returns the number of chocolates in that jar, as there are no adjacent jars to consider.

For cases where there are two or more jars, the function initializes two variables: prev_max and curr_max. The prev_max variable represents the maximum chocolates collected up to the jar before the current one, while curr_max represents the maximum chocolates collected up to the current jar. Initially, prev_max is set to the chocolates in the first jar (jars[0]), and curr_max is set to the maximum of the chocolates in the first and second jars (max(jars[0], jars[1])).

The function then iterates through the remaining jars starting from the third jar (index 2). For each jar, it calculates a new maximum (new_max) by considering two options:

Adding the chocolates in the current jar to prev_max (representing the case where the current jar is selected).
Keeping curr_max as is (representing the case where the current jar is skipped).
The maximum of these two options is stored in new_max. After calculating new_max, the function updates prev_max to the value of curr_max and curr_max to the value of new_max, effectively moving the window of consideration forward.

Once the loop completes, curr_max contains the maximum number of chocolates that can be collected without violating the constraint of skipping adjacent jars. This value is returned as the result.

This approach ensures an efficient solution with a time complexity of O(n), where n is the number of jars, and a space complexity of O(1), as it uses only a constant amount of additional memory.

"""


def max_chocolates_circular(jars):
    if not jars:
        return 0
    if len(jars) == 1:
        return jars[0]
    
    # Helper function to calculate max chocolates for a linear arrangement
    def max_chocolates_linear(jars):
        prev_max = 0
        curr_max = 0
        for jar in jars:
            new_max = max(prev_max + jar, curr_max)
            prev_max, curr_max = curr_max, new_max
        return curr_max

    # Case 1: Exclude the first jar
    max_exclude_first = max_chocolates_linear(jars[1:])
    # Case 2: Exclude the last jar
    max_exclude_last = max_chocolates_linear(jars[:-1])

    # Return the maximum of the two cases
    return max(max_exclude_first, max_exclude_last)

"""To handle the circular arrangement, you can break the problem into two subproblems:

Exclude the First Jar: Solve the problem for jars from index 1 to n-1.
Exclude the Last Jar: Solve the problem for jars from index 0 to n-2.
The maximum of these two solutions will give the correct result for the circular arrangement."""