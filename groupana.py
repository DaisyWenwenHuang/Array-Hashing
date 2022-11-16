# https://leetcode.com/problems/group-anagrams/
# leetcode 49
# medium
# edge case- empty

# if iterate, need three nested loops, O(n^3)
# what if sorted first
# sort taking O(nlogn),and there still a outer loop 

# hashmap ? mapping each string from a-z 
# O(m*n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        # each string in strs
        for s in strs:
            count = [0] * 26 # there are only 26 lowercase letters
            
            # each letter in string
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)    
            
        return res.values()
            