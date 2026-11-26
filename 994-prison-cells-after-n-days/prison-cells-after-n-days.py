class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        cycleCount = 0 
        seen = {}

        while n > 0:

            state = tuple(cells)

            if state in seen:
                cycleCount = seen[state] - n
                n = n % cycleCount
            
            seen[state] = n


            if n > 0:
                n -= 1
                nextcells = [0] * 8 
                for i in range(1 , 7):
                    if cells[i - 1] == cells[i + 1]:
                        nextcells[i] = 1
                
                cells = nextcells 

        return cells 