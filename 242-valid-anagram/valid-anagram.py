from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sFreq = Counter(s)

        for c in t:
            if c not in sFreq:
                return False
            else:
                if sFreq[c] == 0:
                    return False
                sFreq[c] -=1
        return True

            
