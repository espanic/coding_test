L, C = int(input())
# https://velog.io/@yeseolee/python으로-순열과-조합-직접-구현하기
# a c i s t w 

arr = list(map(int, input().split()))
arr.sort()

n = L
while n >= 0:
    