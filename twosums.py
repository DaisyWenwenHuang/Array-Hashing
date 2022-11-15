# https://leetcode.com/problems/two-sum/
# leetcode 1
# easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,el in enumerate(nums):
            if (target - ele) in hashmap:
                return [hashmap[target-ele], index]
            else:
                hashmap[ele] = index
                