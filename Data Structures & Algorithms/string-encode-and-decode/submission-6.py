class Solution:

    def encode(self, strs: List[str]) -> str:
        el = []
        for st in strs:
            el.append(f"{st}€")
        
        
        return "".join(el)


    def decode(self, s: str) -> List[str]:
        dl = []
        st = ""
        for i in range(len(s)):
            if s[i] != "€":
                st += s[i]
            else:
                dl.append(st)
                st = ""
        return dl
        

