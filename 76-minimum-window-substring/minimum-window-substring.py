class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c , 0)
        
        l = 0 
        res = ""
        reslen = float('inf')
        need = len(set(t))
        have = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r] , 0)

            c = s[r]

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:

                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                    res = s[l : r + 1]

                
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        return res
                

                