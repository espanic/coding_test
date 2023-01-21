

# count  = 0
# def count_asc(arr):
#     global count
#     if len(arr) == N:
#         count += 1
#         return 
        
#     last_val = arr[-1] if arr else 0
#     for i in range(last_val, 10):
#         arr.append(i)
#         count_asc(arr)
#         arr.pop()
        
# count_asc([])
# print(count % 10007)

N = int(input())
records = [[1] * 10]

for i in range(1, N):
    record_ist = []
    for j in range(0, 10):
        record_ist.append(sum(records[i - 1][:j + 1]))
            
    records.append(record_ist)
            

print(sum(records[-1])% 10007)