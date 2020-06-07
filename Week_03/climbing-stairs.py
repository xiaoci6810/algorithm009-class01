#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class Solution(object):
    def climbStairs(self, n):
        """
        desc: 动态规划
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        arryList = [0] * (n+1)
        arryList[1] = 1
        arryList[2] = 2
        for i in range(3, n+1):
            arryList[i] = arryList[i-1] + arryList[i-2]
        return arryList[n]