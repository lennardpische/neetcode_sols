class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signatures ={}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in signatures:
                signatures[sorted_s].append(s)
            else:
                signatures[sorted_s] = [s]
        return list(signatures.values())

        