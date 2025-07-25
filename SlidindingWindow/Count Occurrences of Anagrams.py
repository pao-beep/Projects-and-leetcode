"""Count Occurrences of Anagrams.Find all substrings in a string that are anagrams of a given pattern 7.

Example: For text "gotxxotgxdogt" and word "got", the output is 3 (anagrams: "got", "otg", "ogt")."""


from collections import defaultdict

def find_anagrams(s, pattern):
    pattern_counts = defaultdict(int)
    window_counts = defaultdict(int)
    left = 0
    matches = 0
    result = 0

    # Initialize pattern frequency map
    for char in pattern:
        pattern_counts[char] += 1

    for right in range(len(s)):
        char = s[right]
        if char in pattern_counts:
            window_counts[char] += 1
            if window_counts[char] == pattern_counts[char]:
                matches += 1

        # Check if current window is an anagram
        if matches == len(pattern_counts):
            result += 1

        # Shrink window if it exceeds pattern length
        if right >= len(pattern) - 1:
            left_char = s[left]
            if left_char in pattern_counts:
                if window_counts[left_char] == pattern_counts[left_char]:
                    matches -= 1
                window_counts[left_char] -= 1
            left += 1

    return result

"""
The find_anagrams function is designed to count the number of anagrams of a given pattern that appear as substrings in a larger string s. It uses the sliding window technique combined with frequency counting to efficiently solve the problem.

The function begins by initializing two defaultdict objects, pattern_counts and window_counts, to store the frequency of characters in the pattern and the current sliding window of s, respectively. It also initializes variables left (to track the left boundary of the sliding window), matches (to count how many characters in the current window match the required frequency in the pattern), and result (to store the total count of anagrams found).

The first step is to populate pattern_counts with the frequency of each character in the pattern. This serves as the reference for determining whether a substring of s is an anagram of the pattern.

Next, the function iterates through the string s using a for loop, where right represents the right boundary of the sliding window. For each character at position right, it checks if the character exists in pattern_counts. If it does, the character's count in window_counts is incremented. If the count of the character in window_counts matches its count in pattern_counts, the matches counter is incremented.

After updating the window, the function checks if the number of matches equals the number of unique characters in the pattern (i.e., len(pattern_counts)). If so, it means the current window is an anagram of the pattern, and the result counter is incremented.

To maintain the sliding window's size, the function checks if the window's length exceeds the length of the pattern. If it does, the character at the left boundary of the window is removed. If this character exists in pattern_counts and its count in window_counts matches the required count, the matches counter is decremented. The count of the character in window_counts is then reduced, and the left pointer is moved one step to the right.

Finally, after processing all characters in s, the function returns the result, which represents the total number of anagrams of the pattern found in s. This approach ensures an efficient solution with a time complexity of O(n), where n is the length of s.
"""