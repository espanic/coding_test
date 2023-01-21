import sys
input = sys.stdin.readline



# records = [[[None] * 21] * 21] * 21


records = [[[None for _ in range(21)] for _ in range(21)]for _ in range(21)]
def w(a, b, c):
    
    if a<=0 or b<=0 or c<=0:
        records[0][0][0] = 1
        return 1
    
    
    if a > 20 or b > 20 or  c> 20:
        return w(20, 20, 20)
    
    if records[a ][b][c] is not None:
        return records[a][b][c]
    
    if a < b and b < c:
        val = w(a, b, c - 1) + w(a, b- 1, c-1) - w(a, b-1, c)
        records[a][b][c] = val
        return val

    val = w(a - 1, b, c) + w(a-1, b-1, c) +w(a - 1, b, c- 1) - w(a - 1, b- 1, c - 1)
    records[a][b][c] = val
    return val
    
    


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    val = w(a, b, c)
    print("w({}, {}, {}) = {}".format(a, b, c, val))

    

