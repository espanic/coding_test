#LCS 20분 정도? 
from enum import Enum

class Direction(Enum):
    diagonal =0
    left = 1
    top = 2
    end = 3


a = input()
b = input()




records = [[0 for _ in range(len(b))] for _ in range(len(a))]
loc= [[None for _ in range(len(b))] for _ in range(len(a))] 



for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if i - 1>=0 and j - 1>= 0:
                records[i][j] = records[i - 1][j - 1] + 1
                loc[i][j] = [a[i], Direction.diagonal]
            else:
                records[i][j] = 1
                loc[i][j] = [a[i], Direction.end]
        else:
            first = records[i -1][j] if i-1>=0 else 0
            second = records[i][j-1] if j - 1>= 0 else 0
            # records[i][j] = max(first, second)
            
            if i-1 >=0 and j-1>=0:
                direction = Direction.top if first >=second else Direction.left
                records[i][j] = max(first, second)
            elif i - 1>= 0:
                direction = Direction.top
                records[i][j] = first
            elif j - 1>= 0:
                direction = Direction.left
                records[i][j] = second
            else:
                direction = Direction.end
                records[i][j] = 0
            loc[i][j] = [None, direction]

            
i, j = len(a) - 1, len(b) - 1
res = ""

while True:
    loc_e = loc[i][j]
    letter = loc_e[0]
    direction = loc_e[1]
    if letter is not None:
        res += letter
    if direction ==Direction.end:
        break
    elif direction == Direction.diagonal:
        i -= 1
        j -= 1
    elif direction == Direction.left:
        j -= 1
    else:
        i -= 1
            
        
                
print(records[-1][-1])
print(res[::-1])        
        