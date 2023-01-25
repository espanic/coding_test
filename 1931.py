import sys
import heapq
input = sys.stdin.readline


N = int(input())
meetings = [list(map(int, input().split()))[::-1] for _ in range(N)]
heapq.heapify(meetings)

count  = 0
endtime = 0


while meetings:
    next = heapq.heappop(meetings)
    
    # starttime is prior than endtime
    if next[1] < endtime:
        continue
    endtime = next[0]
    count += 1

print(count)

