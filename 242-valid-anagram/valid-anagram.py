class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = Counter(s)
        for i in t:
            if i not in counter:
                return False
            else:
                if counter[i] == 0:
                    return False
                counter[i] -= 1
        return True


