class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
           return False

        res = {}

        for char in s:
            if char not in res:
                res[char] = 1
            else:
                res[char]+= 1

        for char in t :
            if char not in res:
                return False
            else:
                res[char]-=1
            
            if res[char]<0:
                return False

        return True
        