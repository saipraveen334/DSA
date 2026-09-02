class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows = len(classroom)
        cols = len(classroom[0])

        directions =[[0 ,1] , [1 , 0] , [0 , -1] , [-1 , 0]]

        litters = {}
        count = 0 

        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    st_r = r
                    st_c = c
                
                if classroom[r][c] == 'L':
                    litters[(r,c)] = count 
                    count += 1
        
        # if count is zero then no litters 

        if count == 0:
            return 0

        target = ( 1 << count ) - 1

        best = [[{} for _ in range(cols)] for _ in range(rows)]

        q = collections.deque()

        q.append((st_r , st_c , 0 , energy , 0))

        best[st_r][st_c][0] = energy

        while q:
            r , c , mask , en , moves = q.popleft()

            for dr , dc in directions:
                nr = dr + r
                nc = dc + c

                # out of bounds condition 

                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue 
                
                # obstacle 

                if classroom[nr][nc] == 'X':
                    continue 
                
                # out of energy 

                if en == 0:
                    continue 
                
                new_energy = en - 1
                new_mask = mask

                # found the litter 

                if classroom[nr][nc] == 'L':
                    index = litters[(nr ,nc)]
                    new_mask = ( 1 << index) | mask 

                # reset energy 

                if classroom[nr][nc] == "R":
                    new_energy = energy
                
                # final case 

                if new_mask == target:
                    return moves + 1
                
                old_energy = best[nr][nc].get(new_mask , -1)

                if old_energy >= new_energy:
                    continue
                
                best[nr][nc][new_mask] = new_energy 

                q.append((nr , nc , new_mask , new_energy , moves + 1))
        return -1

                
                


                






        