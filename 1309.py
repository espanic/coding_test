from enum import Enum

N = int(input())

# None, right, left
record = [1 ,0, 0]

for i in range(1, N + 1):
    prev_record = record
    curr_record = [0, 0, 0]
    
    none_val = prev_record[0]
    right_val = prev_record[1]
    left_val = prev_record[2]
    
    curr_record[0] += none_val + right_val + left_val
    curr_record[1] += none_val + left_val
    curr_record[2] += none_val + right_val
    record = curr_record
        

print(sum(record) % 9901)

