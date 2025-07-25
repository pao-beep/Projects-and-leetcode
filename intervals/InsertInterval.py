"""You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 """

def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    
    # Add all intervals before the newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    result.append(newInterval)
    
    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

#redo
def insertInterval(intervals, newInterval):
    if intervals is None:
        return []
    if newInterval is None:
        return []
    intervals.sort(keys=lambda x: x[0])
    results = []
    i =0
    n = len(intervals)
    while i < n and intervals[i][1] < newInterval[0]:
        results.append(intervals[i])
        i+=1

    while i < n and intervals[i][0] < newInterval[1]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1],newInterval[1])
        i+=1
    results.append(newInterval)

    while i < n :
        results.append(intervals[i])
        i+=1

    return results 