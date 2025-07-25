"""A string is said to be a special string if either of two conditions is met:

. All of the characters are the same, e.g. aaa.

. All characters except the middle one are the same, e.g. aadaa.

A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

Example

s = mnonopoo

s contains the following 12 special substrings: {m, n, o, n, o, p, o, o, non, ono, opo, oo}.

Function Description

Complete the substrCount function in the editor below.

substrCount has the following parameter(s):

. int n: the length of string s

. string s: a string

Returns
- int: the number of special substrings

Input Format

The first line contains an integer, n, the length of s.
The second line contains the string s.

Constraints

1≤n ≤106
Each character of the string is a lowercase English letter, ascii [a-z].

Sample Input O

5

asasd

Sample Output O

7

Explanation O

The special palindromic substrings of s = asasd are {a, s, a, s, d, asa, sas}

Sample Input 1

7

abcbaba"""

def substrCount(n, s):
    count = 0
    # Step 1: Count all single character substrings
    count += n
    
    # Step 2: Count all substrings with all same characters
    i = 0
    while i < n:
        j = i + 1
        while j < n and s[j] == s[i]:
            j += 1
        length = j - i
        count += length * (length - 1) // 2
        i = j
    
    # Step 3: Count all substrings with middle character different
    for i in range(1, n-1):
        if s[i] != s[i-1] and s[i-1] == s[i+1]:
            left_char = s[i-1]
            left = i - 1
            right = i + 1
            # Expand to the left and right as long as characters match left_char. two-ptr technique
            while left >= 0 and right < n and s[left] == left_char and s[right] == left_char:
                count += 1
                left -= 1
                right += 1
    return count

"""Explanation:
Single Character Substrings: The initial count is set to n because each individual character is a special substring.

All Same Characters: For each sequence of the same character, the number of substrings with all same characters is calculated using the formula k*(k+1)/2, where k is the length of the sequence. This formula counts all possible substrings within the sequence.

Middle Character Different: For each character in the string, we check if it is the middle character of a substring where all other characters are the same. We expand around this middle character to count all valid substrings where the middle character is different and all other characters are the same.

This approach efficiently counts all special substrings in O(n) time, making it suitable for large input sizes"""
"""
Why Does This Formula Work?

1. Problem Context:

o A special substring can either be:

All characters the same (e.g., "aaa").

All characters the same except the middle one (e.g., "aabaa").

· We need to count all such possible substrings in a given string.

2. Counting Substrings with All Same Characters:

o Suppose we have a sequence of k identical characters (e.g., "aaaaa" where k=5 ).

o The number of valid substrings in this sequence is the sum of all possible lengths (from 1 to

Length 1: "a", "a", "a", "a", "a" - 5 substrings.

Length 2: "aa", "aa", "aa", "aa" - 4 substrings.

Length 3: "aaa", "aaa", "aaa" -> 3 substrings.

Length 4: "aaaa", "aaaa" -> 2 substrings.

Length 5: "aaaaa" - 1 substring.

o Total substrings = 5 + 4 + 3 + 2 + 1 = 15.

o This is the sum of the first k natural numbers, which is given by the formula k*(k+1)/2.

3. Mathematical Derivation:

o The sum of the first n natural numbers is:

S=1+2+3+ ... +n=

o Here, n = k (length of the sequence), so:

S =-

o This formula avoids an O(k) loop by computing the sum in constant time.

n(n+1)
2

k(k+1)
2

Example

· String: "aaa" ( k=3 ).

· Substrings:

o Length 1: "a", "a", "a" -> 3.

o Length 2: "aa", "aa" -> 2.

o Length 3: "aaa" - 1.

. Total = 3 + 2 + 1 = 6.
. Using the formula: 3x4
:2 = 6.
"""
