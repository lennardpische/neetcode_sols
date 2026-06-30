class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_t = {}
        count_s = {}
        for i in s:
            if i in count_s:
                count_s[i] += 1
            else:
                count_s[i] = 1
        for j in t:
            if j in count_t:
                count_t[j] += 1
            else:
                count_t[j] = 1   
        return count_t == count_s

