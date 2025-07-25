def find_n_roll_faces(n_weight_tot, missing_obsvs, n, inf):
    six_die = 6
    sum = 0
    if n_weight_tot == 0:
        return 0
    elif n == 0:
        return -1


    for i in range(1, n + 1):
        for j in range(1,six_die+1) :
            if n_weight_tot >= j:
                temp = inf
                temp = find_n_roll_faces(n_weight_tot - j, missing_obsvs, n - 1, inf)
                print(f"temp: {temp}")
                print(f"j:{j}")
                if temp == 0:
                    missing_obsvs.append(j)
                    print(missing_obsvs)
    return (n_weight_tot, missing_obsvs, n, inf),  missing_obsvs
    #find missing observations

def missingRolls1(rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        m_plus_n = m + n
        sum_of_m = 0
        missing_obsvs = []
        for i in range(m):
            sum_of_m += rolls[i]
        print(f"sum of m: {sum_of_m}")
        sum_nums_to_find = (mean * m_plus_n) - sum_of_m
        print(f"sums to find:{sum_nums_to_find}")
        inf = sum_nums_to_find * 2
        val, list=find_n_roll_faces(sum_nums_to_find, missing_obsvs, n, inf)
        print("list:")
        print(list)
        return list


def missingRolls(rolls, mean, n) :
        target_sum = (len(rolls) + n) * mean
        missing_sum = target_sum - sum(rolls)
        if missing_sum < n or missing_sum > n * 6:
            return []
        n_avg, n_mod = missing_sum // n, missing_sum % n
        res = [n_avg] * n
        for i in range(n_mod):
            res[i] += 1
        print(res)
        return res

"""The missingRolls function is designed to calculate the values of n missing dice rolls such that the overall mean of all rolls (including the given ones) equals the specified mean. The function ensures that the missing rolls are valid dice rolls (i.e., integers between 1 and 6) and returns the list of missing rolls if a solution exists. If no valid solution is possible, it returns an empty list.

The function starts by calculating the target_sum, which is the total sum of all dice rolls (both given and missing) required to achieve the specified mean. This is computed as (len(rolls) + n) * mean, where len(rolls) is the number of given rolls, and n is the number of missing rolls. The missing_sum is then calculated by subtracting the sum of the given rolls (sum(rolls)) from the target_sum. This represents the total sum that the missing rolls need to achieve.

Next, the function checks if the missing_sum is feasible. Each missing roll must be between 1 and 6, so the minimum possible sum of n rolls is n, and the maximum possible sum is n * 6. If the missing_sum is outside this range, it is impossible to construct valid missing rolls, and the function returns an empty list.

If the missing_sum is feasible, the function calculates the average value of the missing rolls (n_avg) by performing integer division of missing_sum by n. It also calculates the remainder (n_mod) using the modulus operator. The result list res is initialized with n elements, all set to n_avg. To distribute the remainder (n_mod) evenly, the function increments the first n_mod elements of res by 1. This ensures that the sum of the elements in res equals missing_sum while keeping all values within the valid range of 1 to 6.

Finally, the function prints the resulting list of missing rolls (res) for debugging purposes and returns it. This approach ensures that the missing rolls are distributed as evenly as possible while meeting the constraints of valid dice rolls and the target mean.

"""
missingRolls([3,2,4,3],4,2)