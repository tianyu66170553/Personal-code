# -*- coding: utf-8 -*-
# edit by xty
# Leetcode 1289

class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        minFirstSum, minSecondSum = 0, 0
        minLastIdx = -1

        for row in grid:
            curMinFirstSum, curMinSecondSum = 10**9, 10**9
            curMinLastIdx = -1
            for idx, num in enumerate(row):
                if idx == minLastIdx:
                    curSum = num + minSecondSum
                else:
                    curSum = num + minFirstSum
                if curSum < curMinFirstSum:
                    curMinSecondSum = curMinFirstSum
                    curMinFirstSum = curSum
                    curMinLastIdx = idx
                elif curSum < curMinSecondSum:
                    curMinSecondSum = curSum
            minFirstSum, minSecondSum = curMinFirstSum, curMinSecondSum
            minLastIdx = curMinLastIdx
        print(minFirstSum)
        return minFirstSum
            
    
    
solu = Solution()
grid = [[50,-18,-38,39,-20,-37,-61,72,22,79],[82,26,30,-96,-1,28,87,94,34,-89],[55,-50,20,76,-50,59,-58,85,83,-83],[39,65,-68,89,-62,-53,74,2,-70,-90],[1,57,-70,83,-91,-32,-13,49,-11,58],[-55,83,60,-12,-90,-37,-36,-27,-19,-6],[76,-53,78,90,70,62,-81,-94,-32,-57],[-32,-85,81,25,80,90,-24,10,27,-55],[39,54,39,34,-45,17,-2,-61,-81,85],[-77,65,76,92,21,68,78,-13,39,22]]

solu.minFallingPathSum(grid)