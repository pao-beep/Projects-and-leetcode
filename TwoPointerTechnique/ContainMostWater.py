

"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store."""


def maxArea(height):
    left, right = 0, len(height)-1
    maxArea = 0

    while left < right: 

        currentArea = abs(min(height[left],height[right]) * (right - left))
        if currentArea > maxArea:
            maxArea = currentArea

        if height[left] < height[right]:
            left+=1

        else:
            right-=1
    
    return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # Output should be 49