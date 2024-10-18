class Solution:
    def maximumSwap(self, num: int) -> int:
        snum = [int(_) for _ in str(num)]
        i_maior = -1
        new = ''
        i = 0
        while i < len(snum):
            for j in range(len(snum)-1, i, -1):
                if snum[i] < snum[j] and (i_maior == -1 or snum[j] > snum[i_maior]):
                    i_maior = j
            
            if i_maior != -1:
                snum[i], snum[i_maior] = snum[i_maior], snum[i]
                break
            i += 1
            
        for i in range(len(snum)):
            new += str(snum[i])
        
        return int(new)
    