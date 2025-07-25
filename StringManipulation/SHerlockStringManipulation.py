"""Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the
string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

Example

s = abc

This is a valid string because frequencies are {a : 1, b : 1, c : 1}.

s = abcc

This is a valid string because we can remove one c and have 1 of each character in the remaining string.

s = abccc

This string is not valid as we can only remove 1 occurrence of c. That leaves character frequencies of {a : 1, b : 1, c : 2}.

Function Description

Complete the isValid function in the editor below.

isValid has the following parameter(s):

. string s: a string

Returns

. string: either YES or NO

Input Format

A single string s.

Constraints

. 1 ≤ |s| ≤ 105

. Each character s[i] E ascii[a - z]

Sample Input O

aabbcd

Sample Output O

NC

Explanation O

Given s = "aabbcd", we would need to remove two characters, both c and d -> aabb or a and b -> abcd, to make it valid. We are limited to removing only one
character, so s is invalid.

Sample Input 1

aabbccddeefghi

Sample Output 1"""


from collections import defaultdict

def isValid(s):
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    
    freq_counts = defaultdict(int)
    for count in freq.values():
        freq_counts[count] += 1
    
    if len(freq_counts) == 1:
        return "YES"
    elif len(freq_counts) == 2:
        keys = sorted(freq_counts.keys())
        if (keys[1] - keys[0] == 1 and freq_counts[keys[1]] == 1) or (keys[0] == 1 and freq_counts[keys[0]] == 1):
            return "YES"
    
    return "NO"


"""
Explanation:
First, we count how often each character appears in the string.

Then, we count how often each frequency value occurs (meta-frequency).

If all characters have the same frequency (meta-frequency has only one entry), the string is valid.

If there are exactly two different frequencies:

Case 1: The higher frequency is exactly 1 more than the lower frequency, and there's only one character with the higher frequency. We can remove one occurrence of this character to make all frequencies equal.

Case 2: One of the frequencies is 1 and it occurs only once. We can remove this character to make all remaining frequencies equal.

In all other cases, it's impossible to make all frequencies equal by removing at most one character, so we return "NO".
"""