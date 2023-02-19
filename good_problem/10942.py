import sys
input = sys.stdin.readline
N = int(input())

nums = list(map(int,input().split()))

records = [[True for _ in range(N)]]  # 길이가 1인 것들에 대한 참거짓 여부
start_length = 2

M = int(input())

def dp(S, E):
    global start_length
    finish_length = E - S + 1
    if finish_length < start_length:
        return records[finish_length - 1][S]
    
    for length in range(start_length, finish_length + 1):
        
        new_record = []
        for i in range(N - length + 1):
            res = False
            if nums[i] == nums[i + length - 1]:
                if length <= 2 or records[length - 3][i +1]:
                    res = True
            new_record.append(res)
        records.append(new_record)
    start_length = finish_length + 1
    return records[finish_length - 1][S]
    
        


for _ in range(M):
    S, E = map(int, input().split())
    S -= 1
    E -= 1
    print(int(dp(S, E)))
    

