class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            freqs = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                freqs[i] += 1
            if str(freqs) not in anagrams:
                anagrams[str(freqs)] = []
            anagrams[str(freqs)].append(s)
        return list(anagrams.values())