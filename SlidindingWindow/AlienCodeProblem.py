'''Given a string s consisting of digits ('0' to '9'), find the number of non-empty substrings where the numeric value of the substring is divisible by 3.'''

def alienCodeSolution(alienCode):
    len_ac = len(alienCode)
    sum = 0

    if int(alienCode)%3 == 0:
        sum = sum + 1

    # if sub.index(0) == '0' and len(sub) > 1:
    #     print("constraint violated")

    jump = 1
    while jump <= len_ac:

        for i in range(len(alienCode)):
            #print(alienCode[i:jump])
            if alienCode[i:jump] != '':
                if int(alienCode[i:jump]) == 0 and len(alienCode[i:jump]) > 1:
                    print("constraint violated")
                if i+jump <= len_ac: 
                    #print(i+jump)
                    if int(alienCode[i:jump]) % 3 == 0:
                        sum = sum + 1
        jump= jump + 1
    return sum


#proper code
def alienCodeSolutionImp(alienCode):
    count = 0
    n = len(alienCode)
    for i in range(n):
        for j in range(i, n):
            substring = alienCode[i:j+1]
            # Skip substrings with leading zeros (unless "0")
            if len(substring) > 1 and substring[0] == '0':
                continue
            # Check divisibility by 3
            if int(substring) % 3 == 0:
                count += 1
    return count

#efficient solution deepseek

def count_valid_substrings(s):
    count = 0
    n = len(s)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += int(s[j])
            # Skip leading zeros (except single "0")
            if s[i] == '0' and j > i:
                continue
            # Check divisibility by 3
            if current_sum % 3 == 0:
                count += 1
    return count


""" Hash Map Optimization (Advanced)
We can use a hash map to track the frequency of remainders modulo 3. This allows us to count valid substrings in constant time for each index."""
def count_valid_substrings_hash_map(s):
    count = 0
    remainder_count = {0: 1}  # Initialize with remainder 0 (empty prefix)
    current_sum = 0

    for char in s:
        current_sum = (current_sum + int(char)) % 3
        # Count substrings ending at the current index
        count += remainder_count.get(current_sum, 0)
        # Update remainder frequency
        remainder_count[current_sum] = remainder_count.get(current_sum, 0) + 1

    return count

"""Dynamic Programming Approach
We can use a DP table to store the cumulative remainder modulo 3 for substrings ending at each index. This avoids recalculating the sum for overlapping substrings.

Key Idea:
Use a DP array dp[i] to store the cumulative sum modulo 3 for the substring ending at index i.
If dp[i] == 0, it means the substring from the start to index i is divisible by 3.
Use a hash map to count how many times each remainder (0, 1, 2) has been seen so far. This allows us to count substrings ending at i that are divisible by 3.
"""
def count_valid_substrings_dp(s):
    count = 0
    remainder_count = {0: 1}  # Initialize with remainder 0 (empty prefix)
    current_sum = 0

    for i, char in enumerate(s):
        current_sum = (current_sum + int(char)) % 3
        # Count substrings ending at the current index
        count += remainder_count.get(current_sum, 0)
        # Update remainder frequency
        remainder_count[current_sum] = remainder_count.get(current_sum, 0) + 1

    return count


#alienCodeSolution("456")
print(alienCodeSolution("456"))#20
print(alienCodeSolution("90090"))
print(alienCodeSolution("1203"))
print(alienCodeSolution("13579"))
print(alienCodeSolution("55555"))
print(alienCodeSolution("1234567890"))
print(alienCodeSolution("1"))
print(alienCodeSolution("0012"))
print(alienCodeSolution("222"))
print(alienCodeSolution("100"))#11
print(alienCodeSolution("111111"))#10
print(alienCodeSolution("3030"))
print(alienCodeSolution("102"))
print(alienCodeSolution("123"))
print(alienCodeSolution("369"))
print(alienCodeSolution("124"))
print(alienCodeSolution("003"))
print(alienCodeSolution("000"))
print(alienCodeSolution("3"))
print(alienCodeSolution("0"))#1

# print(count_valid_substrings("456"))#20
# print(count_valid_substrings("90090"))
# print(count_valid_substrings("1203"))
# print(count_valid_substrings("13579"))
# print(count_valid_substrings("55555"))
# print(count_valid_substrings("1234567890"))
# print(count_valid_substrings("1"))
# print(count_valid_substrings("0012"))
# print(count_valid_substrings("222"))
# print(count_valid_substrings("100"))#11
# print(count_valid_substrings("111111"))#10
# print(count_valid_substrings("3030"))
# print(count_valid_substrings("102"))
# print(count_valid_substrings("123"))
# print(count_valid_substrings("369"))
# print(count_valid_substrings("124"))
# print(count_valid_substrings("003"))
# print(count_valid_substrings("000"))
# print(count_valid_substrings("3"))
# print(count_valid_substrings("0"))#1
            

            
            