# https://leetcode.com/problems/valid-anagram/
# leetcode 242
# easy
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hmaps, hmapt = {}, {}
        for i in range(len(s)):
            hmaps[s[i]] = hmaps.get(s[i],0) + 1
            hmapt[t[i]] = hmapt.get(t[i],0) + 1
        
        for ele in hmaps:
            if hmaps[ele] != hmapt.get(ele, 0):
                return False
        
        return True
