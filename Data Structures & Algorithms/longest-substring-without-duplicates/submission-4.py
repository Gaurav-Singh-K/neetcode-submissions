class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        st = set()
        
        ma = 0
        i = 0
        for j in range(len(s)):
            while s[j] in st:
                st.remove(s[i])
                i += 1

            st.add(s[j])

            ma = max(ma, j - i + 1)

            

        return ma

        