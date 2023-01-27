import sys
input = sys.stdin.readline
N = int(input())
images = [input() for _ in range(N)]


def check(i, h, j, w):
    allOne = True
    allZero = True
    for a in range(i, i + h):
        for b in range(j, j + w):
            val = images[a][b]
            if val == '0'and allOne :
                allOne = False
            elif val == '1' and allZero:
    
                allZero =False
        
    if allOne:
        return '1'
    elif allZero:
        return '0'
    else:
        return None
                

def compress(n, i, j):
    if n == 1:
        return images[i][j]
    
    half_length  = n // 2
    
    # 왼쪽 위
    val1 = check(i, half_length, j, half_length)
    if val1 is None:
        val1 = compress(half_length, i, j)
        
    # 오른쪽 위
    val2 = check(i, half_length, j + half_length, half_length)
    if val2 is None:
        val2 = compress(half_length, i, j + half_length)


    # 왼쪽 아래
    val3 = check(i + half_length, half_length, j, half_length)
    if val3 is None:
        val3 = compress(half_length, i + half_length, j)
        
    # 왼쪽 위
    val4 = check(i + half_length, half_length, j + half_length, half_length)
    if val4 is None:
        val4 = compress(half_length, i + half_length, j + half_length)
    
    if val1 == val2 ==val3 == val4:
        if len(val1) == 1:
            return val1

    return '({}{}{}{})'.format(val1, val2, val3, val4)

result = compress(N, 0, 0)
print(result)
        
    