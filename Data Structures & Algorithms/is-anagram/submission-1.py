class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        listFromS = []
        listFromT = []

        for i in range(len(s)):
            listFromS.append(s[i])
            listFromT.append(t[i])

        from collections import Counter

        return Counter(listFromS) == Counter(listFromT)