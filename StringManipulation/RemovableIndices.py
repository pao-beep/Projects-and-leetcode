def getRemovableIndices(str1, str2):
    if len(str1) != len(str2) + 1:
        return [-1]
    
    result = []
    n = len(str2)
    i = 0
    
    # Find the first differing character
    while i < n and str1[i] == str2[i]:
        i += 1
    
    # The extra character could be at position i in str1
    # Check if str1[i+1:] matches str2[i:]
    if str1[i+1:] == str2[i:]:
        result.append(i)
    
    # Also check if the extra character is after position i
    # So we check if str1[i:] matches str2[i+1:] (but since str2 is shorter, we adjust)
    # Actually, we should check if str1[i+1:] matches str2[i:]
    # But we already did that above. To find other possible positions, we need to look further
    
    # Now check if there are other positions where the extra character could be
    # For example, if the strings are "abdgggda" and "abdggda", the first difference is at position 3
    # We need to check if any 'g' can be removed (positions 3,4,5)
    # So we need to find all consecutive same characters at the point of difference
    
    if i < n and str1[i+1] == str2[i]:
        # The extra character is str1[i], but there might be multiple consecutive same characters
        char = str2[i]
        j = i
        while j < len(str1) and str1[j] == char:
            if str1[:j] + str1[j+1:] == str2:
                result.append(j)
            j += 1
    
    if not result:
        return [-1]
    return sorted(result)


#more efficient and cleaner
def getRemovableIndices(str1, str2):
    if len(str1) != len(str2) + 1:
        return [-1]
    
    result = []
    n = len(str2)
    i = 0
    
    # Find the first point of difference
    while i < n and str1[i] == str2[i]:
        i += 1
    
    # Now check all possible positions from i to the end where the character equals str2[i] (if any)
    # The extra character must be in positions where removing it makes str1 match str2
    for j in range(i, len(str1)):
        if str1[:j] + str1[j+1:] == str2:
            result.append(j)
    
    if not result:
        return [-1]
    return result


#final solution code
def getRemovableIndices(str1, str2):
    if len(str1) != len(str2) + 1:
        return [-1]
    
    result = []
    n = len(str2)
    i = 0
    
    # Find the first differing character
    while i < n and str1[i] == str2[i]:
        i += 1
    
    # Case 1: Extra character is at position i (removing it makes str1 match str2)
    if str1[:i] + str1[i+1:] == str2:
        result.append(i)
    
    # Case 2: Extra character is part of a repeated sequence before i
    # (e.g., str1 = "aab", str2 = "ab" → remove either 'a' at 0 or 1)
    if i > 0:
        char = str2[i-1] if i > 0 else str1[i]
        j = i - 1
        while j >= 0 and str1[j] == char:
            if str1[:j] + str1[j+1:] == str2:
                result.append(j)
            j -= 1
    
    # Case 3: Extra character is part of a repeated sequence after i
    # (e.g., str1 = "abbb", str2 = "abb" → remove any 'b' at 1, 2, or 3)
    if i < n:
        char = str2[i-1] if i < n else str1[i]
        j = i +1
        while j < len(str1) and str1[j] == char:
            if str1[:j] + str1[j+1:] == str2:
                result.append(j)
            j += 1
    
    return sorted(result) if result else [-1]