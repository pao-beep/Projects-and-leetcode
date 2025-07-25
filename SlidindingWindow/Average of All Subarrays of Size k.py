"""Problem: Given an array, find the average of all contiguous subarrays of size k"""
#wrong solution
def find_averages_of_subarrays(k, arr):
    result = []
    lower = 0
    upper = k
    sum = 0
    for i in range(len(arr)):
        if i !=upper:
            sum += arr[i]
        else:
            result.append(sum/k)
            sum = 0
            lower+=1
            upper+= 1
            i =lower
#correct solution
def find_averages_of_subarrays(k, arr):
    if k <= 0 or k > len(arr):
        return []  # Handle edge cases where k is invalid

    result = []
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        # Add the next element to the window
        window_sum += arr[window_end]

        # Check if we've hit the window size of k
        if window_end >= k - 1:
            # Calculate the average and append to the result
            result.append(window_sum / k)
            # Slide the window forward: subtract the element going out
            window_sum -= arr[window_start]
            window_start += 1

    return result       
