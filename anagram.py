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
# O(s+t)  as iterarte both strings
# memory complexity is O(s+t) as building hashmap requires extra memory

# solution 2
# using Counter
# might not be ok in interview ?
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
# time complexity and memory is the same as solution 1

# follow up question
# what if no extra memory?
# can sort both strings inplace first then compare each elements one by one
# depends on the sorting algorithm choosen, time complexity can be O(n^2) or O(nlogn)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
