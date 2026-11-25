class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for st in s:
            if st not in d:
                d[st] = 1
            else:
                d[st] = d[st]+1
        for rt in t:
            if rt in d:
                d[rt] = d[rt] - 1
            else:
                return False
        for value in d.values():
            if value != 0:
                return False

        return True
        