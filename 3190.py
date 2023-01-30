import sys
from enum import Enum
from collections import deque
    
input  = sys.stdin.readline







N = int(input())
K = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

L = int(input())
change_direction = []
for _ in range(L):
    a, b = input().split()
    a = int(a)
    change_direction.append((a, b))
    
# 나중에 pop해서 없애기 위함. 
change_direction.reverse()

#Direction 정의
class Direction(Enum):
    north = 0
    west = 1
    south = 2
    east = 3
    
    @staticmethod
    def next_direction(direction, s):
        val = 1 if s == 'L' else -1
        temp = direction.value + val
        if temp > 3:
            temp -= 4
        elif temp < 0:
            temp += 4
        return Direction(temp)
        
    def next_point(self, point):
        x, y = point
        if self == Direction.north:
            return x - 1, y
        elif self == Direction.south:
            return x + 1, y 
        elif self == Direction.east:
            return x, y + 1
        else:
            return x, y - 1

#queue임 왼쪽이 머리다
snake = deque()
snake.append((0, 0))
curr_dir = Direction.east
t = 0 

def check_collision(next_point, snake):
    #벽에 부딛히는 경우
    x, y = next_point
    if x < 0 or x >= N:
        return True
    if y < 0 or y>=N:
        return True
    
    # 자기 몸에 부딛히는 경우
    for point in snake:
        if point == next_point:
            return True
    return False

while True:

    t += 1
    if change_direction and change_direction[-1][0] == t - 1:
        temp = change_direction.pop()
        curr_dir = Direction.next_direction(curr_dir, temp[1])
    next_point = curr_dir.next_point(snake[0])
    
    # check collsiion
    if check_collision(next_point, snake):
        print(t)
        break
    
    # check if apple
    if board[next_point[0]][next_point[1]]:

        board[next_point[0]][next_point[1]] = 0
        snake.appendleft(next_point)
    else:
        snake.appendleft(next_point)
        snake.pop()
        

        

    