N = int(input())

lines = []

for _ in range(N):
    a, b = map(int, input().split())
    lines.append([a,b])
    
lines.sort(key = lambda x: x[0], reverse= True)

answer = 0
buffer = 0
end = -1000000001
while lines:
    line = lines.pop()
    if line[0] <=end:
        buffer += max(0, line[1] - end)
        end = max(line[1], end)
    else:
        answer += buffer
        buffer = line[1] -line[0]
        end = line[1]
        
answer += buffer
print(answer)

    