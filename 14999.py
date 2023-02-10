from enum import Enum
class Direction(Enum):
    east = 1
    west = 2
    north = 3
    south = 4
    up = 5
    down = 6
    
N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

orders = list(map(int, input().split()))
orders = list(map(Direction, orders))


    
class Dice:
    def __init__(self, board, location):
        self.location = location
        self.board = board
        self.up = 0
        self.north = 0
        self.east = 0
        self.west = 0
        self.south = 0
        self.down = 0
        
    def _update_next_location(self, order):
        new_location = self.location.copy()
        if order == Direction.east:
            new_location[1] += 1
        elif order == Direction.west:
            new_location[1] -= 1
        elif order == Direction.north:
            new_location[0] -= 1
        else:
            new_location[0] += 1
        i, j = new_location
        if i >=0 and i < N and j >= 0 and j < M:
            self.location = new_location
            return True
        return False
    
    def _rotate(self, order):
        if order == Direction.east:
            # south, north는 바뀌지 않는다. up -> east east -> down, down->west, west->up
            buffer = [self.up, self.east, self.down, self.west]
            self.east = buffer[0]
            self.down = buffer[1]
            self.west = buffer[2]
            self.up = buffer[3]
        elif order == Direction.west:
            buffer = [self.up, self.west, self.down, self.east]
            self.west = buffer[0]
            self.down = buffer[1]
            self.east = buffer[2]
            self.up = buffer[3]
        elif order == Direction.north:
            # east west는 바뀌지 않는다. 
            buffer = [self.up, self.north, self.down, self.south]
            self.north= buffer[0]
            self.down = buffer[1]
            self.south = buffer[2]
            self.up = buffer[3]
        else:
            buffer = [self.up, self.south, self.down, self.north]
            self.south= buffer[0]
            self.down = buffer[1]
            self.north = buffer[2]
            self.up = buffer[3]
            
    def _update_board_or_dice(self):
        x, y = self.location
        if self.board[x][y] == 0:
            self.board[x][y] = self.down
        else:
            self.down = self.board[x][y]
            self.board[x][y] = 0
            
                
        
    def move(self, order):
        if not self._update_next_location(order):
            pass
        else:
            self._rotate(order) 
            self._update_board_or_dice()
            print(self.up)
        
        

dice = Dice(board, [x,y])
for order in orders:
    dice.move(order)