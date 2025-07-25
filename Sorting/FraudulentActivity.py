"""
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is
greater than or equal to 2x the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send
the client any notifications until they have at least that trailing number of prior days' transaction data.
Given the number of trailing days d and a client's total daily expenditures for a period of n days, determine the number of times the client will receive a notification over
all n days.

Example

expenditure = [10, 20, 30, 40, 50]
d=3

On the first three days, they just collect spending data. At day 4, trailing expenditures are [10, 20, 30]. The median is 20 and the day's expenditure is 40. Because
40 ≥ 2 x 20, there will be a notice. The next day, trailing expenditures are [20, 30, 40] and the expenditures are 50. This is less than 2 x 30 so no notice will be sent.
Over the period, there was one notice sent.

Note: The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number of values, the middle one is picked. If there is an
even number of values, the median is then defined to be the average of the two middle values. (Wikipedia)

Function Description

Complete the function activityNotifications in the editor below.

activityNotifications has the following parameter(s):
. int expenditure[n]: daily expenditures
. int d: the lookback days for median spending

Returns
. int: the number of notices sent

Input Format

The first line contains two space-separated integers n and d, the number of days of transaction data, and the number of trailing days' data used to calculate median
spending respectively.
The second line contains n space-separated non-negative integers where each integer i denotes expenditure[i].

Constraints

. 1<n ≤2×105
. 1<d <n
. 0 ≤ expenditure[i] ≤ 200

Output Format

Sample Input O

STDIN

9 5
2 3 4 2 3 6 8 4 5

Sample Output O

Function

expenditure[] size n =9, d = 5
expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]

2"""

def activityNotifications(expenditure, d):
    notifications = 0
    count = [0] * 201  # Expenditure values are between 0 and 200

    # Initialize count with the first 'd' elements
    for i in range(d):
        count[expenditure[i]] += 1 #this implicitly sorts the numbers and calc their frequencies

    for i in range(d, len(expenditure)):
        # Calculate the median
        median = 0
        total = 0
        if d % 2 == 1:
            # Odd case: find the middle element
            for j in range(201):
                total += count[j]
                if total > d // 2:
                    median = j
                    break
        else:
            # Even case: find the two middle elements
            first = -1
            second = -1
            for j in range(201):
                total += count[j]
                if first == -1 and total >= d // 2:
                    first = j
                if total >= d // 2 + 1:
                    second = j
                    break
            median = (first + second) / 2

        # Check if current expenditure triggers a notification
        if expenditure[i] >= 2 * median:
            notifications += 1

        # Update the count array for the sliding window
        count[expenditure[i - d]] -= 1  # Remove the oldest element
        count[expenditure[i]] += 1      # Add the new element

    return notifications