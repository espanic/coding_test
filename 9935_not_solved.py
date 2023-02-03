


def preprocessing(pattern):
    k = -1
    j = 0
    m = len(pattern)
    pi = [0] * (m+1)
    pi[0] = -1
    while j < m:
        if k == -1 or pattern[k] == pattern[j]:
            k += 1
            j += 1
            pi[j] = k
        else:
            k = pi[k]
            
    return pi

# def kmp(string, pattern, pi):
#     matches = []
#     i = 0
#     j = 0
#     n = len(string)
#     m = len(pattern)
#     while i < n:
#         if j == -1 or string[i] == pattern[j]:
#             i+=1
#             j+=1
#         else:
#             j = pi[j]
#         if j == m:
#             matches.append(i - m)
#             j = 0
#     return matches



# string = input()
# explode = input()
# m =len(explode)
# pi = preprocessing(explode)

# while True:
#     matches = kmp(string, explode, pi)

#     if len(matches) == 0:
#         if len(string) == 0:
#             print("FRULA")
#         else:
#             print(string)
#         break
    
#     temp = ""
#     j = 0
#     for i in matches:
#         temp += string[j:i]
#         j = i + m
    
#     if j < len(string):
#         temp += string[j:]
#     string = temp
        
from collections import deque
string = input()
pattern = list(input())
m =len(pattern)
stack = list(string)
stack =deque(stack)

isReversed = False
buffer_can_match = deque()
while stack:
    before_explode_len = len(stack)
    i = 0
    buffer_not_match = deque()


    isReversed = not isReversed
    while stack:
        c = stack.popleft()
        if pattern[i] == c:
            buffer_can_match.append(c)
            i += 1
            if i == m:
                i = 0
                buffer_can_match.clear()
        else:
            while buffer_can_match:
                buffer_not_match.append(buffer_can_match.popleft())
            i = 0
            if pattern[i] == c:
                # stack.appendleft(c)
                buffer_can_match.append(c)
                i += 1
            else:
                buffer_not_match.append(c)
    stack = buffer_not_match
    stack.extend(buffer_can_match)
    buffer_can_match.clear()
    
    # print(stack)
    # print(before_explode_len, len(stack))
    if before_explode_len == len(stack):
        break

s = "".join(stack)
if len(s) == 0:
    print("FRULA")
else:
    print(s)
    
    

            
    