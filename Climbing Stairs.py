class Solution:
    def __init__(self):
        self.mem = [1, 2]

    def climbStairs(self, n: int) -> int:

        if n == 1:
            return self.mem[n - 1]
        if n == 2:
            return self.mem[n - 1]
        if n == -1 or 0:
            return 0
        if len(self.mem) >= n and self.mem[n - 1] is not None:
            print("ln 17 exec")
            return self.mem[n - 1]
        else:
            ndiff_ways = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.mem.append(ndiff_ways)
            print(self.mem)
            return ndiff_ways

