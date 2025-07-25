def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        # If duplicate found, move `left` past the previous occurrence
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right  # Update last seen index
        max_length = max(max_length, right - left + 1)

    return max_length