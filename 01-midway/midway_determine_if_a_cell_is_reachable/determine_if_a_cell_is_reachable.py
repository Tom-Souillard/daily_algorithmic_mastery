class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t == 1 and sx == fx and sy == fy:
            return False
        return max((abs(sx - fx)), (abs(sy - fy))) <= t