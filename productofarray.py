# https://leetcode.com/problems/product-of-array-except-self/
# leetcode 238
# medium
# can  not use division operation
# time complexity needs to be O(n)
# using prefix and postfix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res