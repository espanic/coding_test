#24분 걸림. 

eq = input()


nums = []
operators = []
buffer = ""
for s in eq:
    if s in ("+", "-"):

        if len(buffer) != 0:
            nums.append(int(buffer))
        operators.append(s)
        buffer = ""
    else:
        buffer += s

if len(buffer) != 0:
    nums.append(int(buffer))
    
    
res = nums[0]
i = 0
while i < len(operators):
    operator = operators[i]
    if operator == '+':
        res += nums[i + 1]
        i += 1
    else:
        res -= nums[i + 1]
        j = i + 1
        buffer = 0
        while j < len(operators):
            if operators[j] == '-':
                break
            buffer += nums[j + 1]
            j += 1
        res -= buffer
        i = j

        
print(res)
            