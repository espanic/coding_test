n, m =map(int, input().split())

line_drawn_point = set()

class Vertex:
    def __init__(self, key):
        self.key = key
        self.children = []

vertices = [Vertex(i) for i in range(n)]


def check_cycle():
    visited = [False for _ in range(n)]
    for i in line_drawn_point:
        if not visited[i]:
            vertex = vertices[i]
            if back_tracking(vertex, visited, i, 1):
                return True
    return False

def back_tracking(vertex, visited, i, num):
    visited[vertex.key] = True
    if vertex.key == i and num != 1:
        return True
    
    for child in vertex.children:
        if not visited[child.key] or (child.key == i and num > 2):
            temp = back_tracking(child, visited, i, num + 1)
            if temp:
                return True
            
    return False
            


answer = None
for i in range(m):
    a, b = map(int, input().split())
    line_drawn_point.add(a)
    line_drawn_point.add(b)
    

    vertices[a].children.append(vertices[b])
    vertices[b].children.append(vertices[a])
    


    if check_cycle():
        answer = i +1
        break
    
for j in range(i+1, m):
    input()
    
    

print(0) if answer is None else print(answer)
    