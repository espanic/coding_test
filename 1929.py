import sys
print = sys.stdout.write

from math import sqrt

M, N = map(int, input().split())
           
    
grid = [i for i in range(N + 1)]

for i in range(2, int(sqrt(N)) +1):
    if grid[i]:
        j= 2
        while i * j <= N:
            grid[i*j] = 0
            j += 1
            

s =""

for p in grid[M:]:
    if p != 0 and p!= 1:
        s += str(p) + "\n"
print(s)
        
        
        
            
             
    