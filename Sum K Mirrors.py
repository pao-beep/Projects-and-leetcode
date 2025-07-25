"""A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
Given the base k and the number n, return the sum of the n smallest k-mirror numbers.



Example 1:

Input: k = 2, n = 5
Output: 25
Explanation:
The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
  base-10    base-2
    1          1
    3          11
    5          101
    7          111
    9          1001
Their sum = 1 + 3 + 5 + 7 + 9 = 25.
Example 2:

Input: k = 3, n = 7
Output: 499
Explanation:
The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
  base-10    base-3
    1          1
    2          2
    4          11
    8          22
    121        11111
    151        12121
    212        21212
Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
Example 3:

Input: k = 7, n = 17
Output: 20379000
Explanation: The 17 smallest 7-mirror numbers are:
1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596


Constraints:

2 <= k <= 9
1 <= n <= 30"""



def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def to_base_k(num, k):
    """Convert a number to base-k as a string."""
    result = []
    while num > 0:
        result.append(str(num % k))
        num //= k
    return ''.join(result[::-1])

# def generate_palindromes():
#     """Generate palindromic numbers in base-10."""
#     num = 1
#     while True:
#         # Generate odd-length palindromes
#         s = str(num)
#         yield int(s + s[-2::-1])  # Mirror all but the last digit
#         # Generate even-length palindromes
#         yield int(s + s[::-1])  # Mirror all digits
#         num += 1

def generate_palindromesDeep():
        length = 1
        while True:
            # Generate all palindromes of 'length' digits
            half_len = (length + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            for num in range(start, end):
                num_str = str(num)
                if length % 2 == 0:
                    palindrome = num_str + num_str[::-1]
                else:
                    palindrome = num_str + num_str[:-1][::-1]
                yield int(palindrome)
            length += 1
    

def sum_k_mirror_numbers(k, n):
    """Find the sum of the n smallest k-mirror numbers."""
    count = 0
    total_sum = 0
    palindromes = generate_palindromesDeep()

    while count < n:
        num = next(palindromes)
        base_k_representation = to_base_k(num, k)
        if is_palindrome(base_k_representation):
            print(f"Valid k-mirror: {num} (Base-{k}: {base_k_representation})")
            total_sum += num
            count += 1

    return total_sum

# Example usage
print(sum_k_mirror_numbers(2, 5))  # Output: 25
# print(sum_k_mirror_numbers(3, 7))  # Output: 499
# print(sum_k_mirror_numbers(7, 17))  # Output: 20379000