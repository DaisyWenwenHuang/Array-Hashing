# https://leetcode.com/problems/top-k-frequent-elements/
# leetcode 347
# medium
# O(n) linear time
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        f = [[] for i in range(len(nums) + 1)]
        for ele in nums:
            hashmap[ele] = hashmap.get(ele,0) + 1
        for n , c in hashmap.items():
            f[c].append(n)
        
        res = []
        for i in range(len(f)-1,0,-1):
            for n in f[i]:
                res.append(n)
                if len(res) == k:
                    return res