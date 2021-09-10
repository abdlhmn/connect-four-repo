class Board:
    def __init__(self):
        self.board = [[' '] * 8 for _ in range(9)]
        
    def display(self):
        print(' ', end=' ')
        print(*[chr(i + 65) for i in range(8)], sep=' |')
        for i in range(1, 9):
            print('_' * 25)
            print(i, end='|')
            print(*self.board[i-1], sep=' |')

    def validating_syntax(self, move):
        if move in range(8):
            if self.board[0][move] != ' ':
                return False
            else:
                return True
        return False
    
    def finding_coords(self, move):
        i = 7
        while self.board[i][move] != ' ':
            i -= 1
        return move, i

    def making_moves(self, other, coords):
        self.board[coords[1]][coords[0]] = other
    
    def is_full(self):
        val = 0
        for i in range(8):
            if self.board[0][i] != ' ':
                val += 1
        if val == 8:
            return True
        else:
            return False
    
    def has_won(self, other, coords):
        # y = x
        # contiguous = 1
        # scan_x = coords[0] + 1
        # while scan_x != 8 and isinstance(self.board[coords[1]][scan_x], Players):
        #     if contiguous == 4:
        #         return True
        #     if self.board[coords[1]][scan_x].side == other.side:
        #         contiguous += 1
        #     else:
        #         break
        #     scan_x += 1
        # scan_x = coords[0] - 1
        # while scan_x != -1 and isinstance(self.board[coords[1]][scan_x], Players):
        #     if contiguous == 4:
        #         return True
        #     if self.board[coords[1]][scan_x].side == other.side:
        #         contiguous += 1
        #     else:
        #         break
        #     scan_x -= 1

        # print(contiguous, 'CONTIGUOUS')
        # c = coords[1] - coords[0] * m
        # y = mx + c
        def bad_func(other, coords, is_pos, m):
            if m == 'undefined':
                contiguous = 1
                scan_y = coords[1] + is_pos
                while scan_y not in (8, -1) and isinstance(self.board[scan_y][coords[0]], Players):
                    if self.board[scan_y][coords[0]].side != other.side:
                        return contiguous
                    else:
                        contiguous += 1
                        scan_y += is_pos
                    if contiguous == 4:
                        return contiguous
                return contiguous
            c = coords[1] - coords[0] * m
            check_coords = (coords[0] + is_pos, m*(coords[0]+is_pos) + c) # check
            contiguous = 0
            while max(check_coords) != 8 and min(check_coords) != -1 and isinstance(self.board[check_coords[1]][check_coords[0]], Players):
                if self.board[check_coords[1]][check_coords[0]].side == other.side:
                    contiguous += 1
                else:
                    break
                if contiguous == 4:
                    print(contiguous)
                    return contiguous
                check_coords = (check_coords[0] + is_pos, m * (check_coords[0]+is_pos) + c)
            return contiguous
        lst = [bad_func(other, coords, 1, 0) + bad_func(other, coords, -1, 0),  bad_func(other, coords, 1, 'undefined'), bad_func(other, coords, 1, 1) + bad_func(other, coords, -1, 1), bad_func(other, coords, 1, -1) + bad_func(other, coords, -1, -1)]
        # print(lst)
        vertical = lst.pop(1)
        if vertical >= 4:
            return True
        elif max(lst) >= 3:
            return True
        else:
            return False


class Players:
    def __init__(self, side, image):
        self.side = side
        self.image = image

    def __str__(self):
        return self.image

board = Board()
white = Players('white', '●')
black = Players('black', '○')
turn = 0
while True:
    turn += 1
    board.display()
    output = 'Black' if turn % 2 else 'White'
    try:
        print(output, 'to move.')
        move = ord(input('Input the columna at which you\'d like to put the counter. '))-65
        while not board.validating_syntax(move):
            move = ord(input('Inavlid move. '))-65
    except TypeError:
        print('Invalid move.')
        continue
    coords = board.finding_coords(move)
    # print(coords)
    if turn % 2 == 0:
        output = 'WHITE'
        board.making_moves(white, coords)
        status = board.has_won(white, coords)
    else:
        output = 'BLACK'
        board.making_moves(black, coords)
        status = board.has_won(black, coords)
    if status:
        print(output, 'HAS WON')
        break
    if board.is_full():
        print('IT\'S A DRAW')
        break
board.display()