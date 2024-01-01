# -*- coding: utf-8 -*-

# Leetcode 1154

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = [int(x) for x in date.split('-')]
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and year % 100 != 0:
            days[1] += 1
        elif year % 100 == 0 and year % 400 == 0:
            days[1] += 1
        else:
            pass
        result = sum(days[:month-1])
        result += day
        print(result)
        return result
    
    
sul = Solution()
sul.dayOfYear("2020-02-11")