class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for str in strs:
            key = tuple(sorted(str))
            if key not in d:
                d[key] = []
            d[key].append(str)
        return list(d.values())




        