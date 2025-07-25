"""Given a 6 x 6 2D array, arr, an hourglass is a subset of values with indices falling in the following pattern:

a b c

d

e f g

There are 16 hourglasses in a 6 x 6 array. The hourglass sum is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in arr, then
print the maximum hourglass sum.

Example

arr =

-9-9-9 111
0-9 0 432
-9-9-9 12 3
008660
000-200
001 240

The 16 hourglass sums are:

-63, -34,-9,12,
-10, 0,28,23,
-27, -11, -2, 10,
9, 17, 25, 18

1

1

The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:

043

866

Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Function Description

Complete the function hourglassSum with the following parameter(s):
. int arr[6][6]: a 2-D array of integers

Returns
. int: the maximum hourglass sum

Input Format

Each of the 6 lines of inputs arr[i] contains 6 space-separated integers arr[i][j].

Constraints

. -9 ≤ arr[i][j] ≤ 9
. 0<i,j≤5"""

#myversion

def hourglassSum(arr):
    # Write your code here
  
    maxsum = -float('inf')
  
    cidx = 0
    
    for row in range(4):
        for col in range(4):
            hsum=0
            while cidx <= 2:
                hsum += arr[row][col+cidx]
                hsum += arr[row+2][col+cidx]
                if cidx ==1:
                    hsum+=arr[row +1][col+cidx]
                cidx+=1
            cidx=0
            if hsum > maxsum:
                maxsum = hsum
    return maxsum
            

#deepseek
def hourglassSum(arr):
    maxsum = -float('inf')  # Initialize to negative infinity to handle all negative sums
    for row in range(4):
        for col in range(4):
            # Calculate the hourglass sum
            hsum = (arr[row][col] + arr[row][col+1] + arr[row][col+2] +  # Top row
                    arr[row+1][col+1] +                                  # Middle element
                    arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2])  # Bottom row
            if hsum > maxsum:
                maxsum = hsum
    return maxsum