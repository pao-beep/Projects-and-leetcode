"""def merge(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on the start value
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # Overlapping intervals, merge them
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    return merged"""

def merge(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on the start value
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # Overlapping intervals, merge them
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    return merged

#redo
def mergeIntervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x:x[0])

    merged = intervals[0]
    for curr in intervals[1:]:
        if curr[0] <=merged[-1][1]:
            merged[-1][1] = max(curr[1],merged[-1][1])
        else:
            merged.append(curr[0])