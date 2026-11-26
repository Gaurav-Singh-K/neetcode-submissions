class Solution:

    def encode(self, strs: List[str]) -> str:
        el = []
        for st in strs:
            el.append(f"{len(st)}#{st}")
        
        
        return "".join(el)


    def decode(self, s: str) -> List[str]:
        dl = []
        st = ""
        i = 0
    
        while i < len(s):
            if s[i] == "#":
                i += 1
                dl.append(s[i:int(st)+i])
                i += int(st)
                st = ""
                
            else:
                st += s[i]
                i += 1
            
        return dl
        

