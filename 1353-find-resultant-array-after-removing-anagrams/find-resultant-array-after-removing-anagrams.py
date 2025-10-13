class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev_sig = ""
        for w in words:
            sig = ''.join(sorted(w))
            if sig != prev_sig:
                result.append(w)
                prev_sig = sig
        return result