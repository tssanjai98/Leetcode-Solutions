class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        l =len(haystack)
        i=idx=0
        while i <= l-n:
            if haystack[i:i+n] == needle:
                return i
            i+=1
        return -1