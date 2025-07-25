def MatrixDiagonalPatternSoution(pattern, matrix):

    matrix_len = len(matrix)
    pattern_len = len(pattern)
    idx = 0
    itr = 0
    for i in range(matrix_len):
        
        for j in range(len(matrix[i])):
            if matrix[i][j+itr] == pattern[idx]:
                idx = idx + 1
                itr = j+1
                break
        continue

    if idx == (pattern_len - 1):
        return True
    
"""Explanation:
Primary Diagonal:

The primary diagonal consists of elements where row == col (matrix[0][0], matrix[1][1], etc.).

We compare each element in this diagonal with the corresponding character in pattern.

Edge Cases:

If the matrix is empty, return False.

If pattern is longer than the diagonal, return False."""
def MatrixDiagonalPatternSolution(pattern, matrix):
    rows = len(matrix)
    if rows == 0:
        return False
    cols = len(matrix[0])
    pattern_len = len(pattern)
    
    # Check primary diagonal (top-left to bottom-right)
    min_length = min(rows, cols)
    if pattern_len > min_length:
        return False
    
    for i in range(min_length):
        if matrix[i][i] != pattern[i]:
            return False
    return True


"""Generalized Solution (All Diagonals)
To check all possible diagonals (not just the primary one), use this approach:
Key Improvements:
Sliding Window:

For each diagonal, maintain a window of characters (matched) and compare it with pattern when the window size matches pattern_len.

All Diagonals:

Diagonals starting from the first row (left to right) and first column (top to bottom) are checked separately.

Efficiency:

Time: O(n × m) (worst case, but early termination if a match is found)."""

def is_diagonal_match(matrix, pattern):
    rows, cols = len(matrix), len(matrix[0])
    pattern_len = len(pattern)
    
    # Check diagonals starting from the first row
    for col in range(cols):
        i, j = 0, col
        matched = []
        while i < rows and j < cols:
            matched.append(matrix[i][j])
            if len(matched) == pattern_len:
                if ''.join(matched) == pattern:
                    return True
                matched.pop(0)  # Sliding window
            i += 1
            j += 1
    
    # Check diagonals starting from the first column (skip row 0 to avoid overlap)
    for row in range(1, rows):
        i, j = row, 0
        matched = []
        while i < rows and j < cols:
            matched.append(matrix[i][j])
            if len(matched) == pattern_len:
                if ''.join(matched) == pattern:
                    return True
                matched.pop(0)
            i += 1
            j += 1
    
    return False

"""To skip irrelevant diagonals early, modify the logic:

Early Termination: If current[0] != pattern[0], reset current immediately (no sliding).

No Sliding for Mismatches: Only slide if the first character matches.
Skips Useless Windows: If current[0] doesn’t match pattern[0], it resets instead of sliding.

Still Uses Sliding for Partial Matches: If current = ["a", "b"] and next char is "x", it slides to ["b", "x"] to check other possibilities.
"""


def is_diagonal_match(matrix, pattern):
    if not matrix or not pattern:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    pattern_len = len(pattern)
    
    for col in range(cols):  # Diagonals starting from first row
        i, j = 0, col
        current = []
        while i < rows and j < cols:
            char = matrix[i][j]
            if not current and char != pattern[0]:
                i += 1; j += 1  # Skip entire diagonal if first char mismatches
                continue
            current.append(char)
            if len(current) == pattern_len:
                if ''.join(current) == pattern:
                    return True
                current.pop(0)  # Slide only if we had a partial match
            i += 1; j += 1
    
    for row in range(1, rows):  # Diagonals starting from first column (skip row 0)
        i, j = row, 0
        current = []
        while i < rows and j < cols:
            char = matrix[i][j]
            if not current and char != pattern[0]:
                i += 1; j += 1
                continue
            current.append(char)
            if len(current) == pattern_len:
                if ''.join(current) == pattern:
                    return True
                current.pop(0)
            i += 1; j += 1
    
    return False




"""Alternative Approach (Fixed-Window Check)
If the problem requires the pattern to start at the diagonal’s first character, simplify to:
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == pattern[0]:  # Only start if first char matches
            matched = []
            i, j = row, col
            while len(matched) < len(pattern) and i < rows and j < cols:
                matched.append(matrix[i][j])
                i += 1; j += 1
            if ''.join(matched) == pattern:
                return True
return False

Your intuition was correct: Popping mismatched characters ("c" in ["c", "a", "t"]) is useless if the first character doesn’t match.

Optimized Fix: Skip diagonals early when current[0] != pattern[0].

Trade-offs:

Sliding Window: More efficient for long diagonals with partial matches.

Fixed-Window: Simpler but checks all possible starting points.
"""

#Test case:
matrix = [
    ['c', 'a', 't'],
    ['d', 'o', 'g'],
    ['b', 'l', 'u']
]
pattern = "bolder"  # Correct pattern is "bol" (if diagonal starts at 'b'), but len("bolder") > max diagonal length (3)

matrix = [
    ['a', 'b', 'c'],
    ['d', 'a', 'b'],
    ['e', 'f', 'a']
]
pattern = "abc"

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
pattern = "aei"