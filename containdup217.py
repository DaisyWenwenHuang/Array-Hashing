# https://leetcode.com/problems/contains-duplicate/
# leetcode 217
# easy
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for num in nums:
            if num in h:
                return True
            else:
                h[num] = 1
        return False