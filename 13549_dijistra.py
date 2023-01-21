import heapq

class Vertex():
    def __init__(self, i):
        self.visited = False
        self.time = MAX_NUM
        self.index = i
        
    def __lt__(self, other):
        return self.time < other.time

N, K = list(map(int, input().split()))

MAX_NUM = 200000

# distance, visited, vertex_num

# times = [MAX_NUM] * (MAX_NUM + 1)
# visited = [False] * (MAX_NUM + 1)
# take_seconds = [[times[i], visited[i], i] for i in range(0, MAX_NUM + 1)]

vertices = [Vertex(i) for i in range(0, MAX_NUM + 1)]
heap = [vertices[i] for i in range(0, MAX_NUM + 1)]

vertices[N].time = 0
heap = []
heapq.heappush(heap, vertices[N])


while True:
    u = heapq.heappop(heap)
    u.visited = True
    if u.index == K:
        print(u.time)
        break
    
    # 1
    if u.index - 1>=0 and u.index - 1 <=MAX_NUM:
        v = vertices[u.index - 1]
        if  not v.visited and v.time > 1 + u.time:
            v.time=  1 + u.time
            heapq.heappush(heap, v)
            
    # 1
    if u.index + 1>=0 and u.index + 1 <=MAX_NUM:
        v = vertices[u.index + 1]
        if  not v.visited and v.time > 1 + u.time:
            v.time=  1 + u.time
            heapq.heappush(heap, v)
            
    # 1
    if u.index *2>=0 and u.index *2 <=MAX_NUM:
        v = vertices[u.index * 2]
        if  not v.visited and v.time > u.time:
            v.time=  u.time
            heapq.heappush(heap, v)
    
        
