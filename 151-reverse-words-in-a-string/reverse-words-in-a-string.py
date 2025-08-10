class Solution:
    def reverseWords(self, s: str) -> str:

        #return " ".join(s.split()[::-1])

        q = deque()
        
        start = -1 
        i = 0

        while i < len(s):

            if s[i] != " ":

                start = i
                while i <len(s) and s[i]!= " ":
                    i += 1
                q.appendleft(s[start:i])

                i-= 1
            i+= 1
        return " ".join(q)


        