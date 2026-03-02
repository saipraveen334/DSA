class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # FREQUENCY ARRAY ----CRAZYYY 
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True






        # HASHMAP 

        if len(s) != len(t):
            return False
        
        hashmapS = {}
        hashmapT = {}

        for i in range(len(s)):
            hashmapS[s[i]] = 1 + hashmapS.get( s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get( t[i], 0)
        
        return hashmapS == hashmapT
        