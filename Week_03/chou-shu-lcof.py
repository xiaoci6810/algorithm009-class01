#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class Solution:
    def nthUglyNumber(self, n):
        dp = [1 for i in range(n)]
        cnt = 1
        t2 = t3 = t5 = 0
        t2_val, t3_val, t5_val = 2, 3, 5
        while cnt < n:
            dp[cnt] = min(dp[t2]*t2_val, dp[t3]*t3_val, dp[t5]*t5_val)
            if dp[cnt] == dp[t2]*t2_val: t2 += 1
            if dp[cnt] == dp[t3]*t3_val: t3 += 1
            if dp[cnt] == dp[t5]*t5_val: t5 += 1
            cnt += 1
        return dp[-1]
    
solution = Solution()
print(solution.nthUglyNumber(10))
