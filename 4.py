import pygame as pg

WIDTH = 1050
HEIGHT = 900
board = [[''] * 7 for line in range(6)]


def move(x, y):
    # 判断是否为有效移动
    if x < 0 or x >= 6 or y < 0 or y >= 7:
        return False
    if board[x][y] != '':
        return False
    if x == 5:
        return True
    if board[x + 1][y] != '':
        return True
    return False


def make_move(x, y, color):
    # 进行棋局移动
    if move(x, y):
        board[x][y] = color
        return True
    return False


def check_win(board):
    for line in board:
        if ''.join(line).find('X' * 4) != -1:
            return "X"
        elif ''.join(line).find('O' * 4) != -1:
            return "O"
    return None


def check_win2(board):
    board_b = [list(line) for line in zip(*board)]  # 将表格行列调换
    board_c = [[] for line in range(14)]
    for x in range(6):
        for y in range(7):
            board_c[x + y].append(board[x][y])
    board_d = [[] for line in range(14)]
    for x in range(6):
        for y in range(7):
            board_d[x - y].append(board[x][y])  # 定义列，斜行
    return [check_win(board), check_win(board_b), check_win(board_c), check_win(board_d)]  # 最终判断胜利方式


def evaluate(board):
    # 评估当前棋盘状态
    result = check_win2(board)
    if "X" in result:
        return 100
    elif 'O' in result:
        return -100
    else:
        return 0
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or check_win2(board) != [None, None, None, None]:
        return evaluate(board)
    if maximizing_player:
        max_eval = float('-inf')
        for y in range(7):
            for x in range(6):
                if move(x, y):
                    make_move(x, y, 'X')
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[x][y] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for y in range(7):
            for x in range(6):
                if move(x, y):
                    make_move(x, y, 'O')
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[x][y] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def get_best_move():
    best_score = float('-inf')
    best_move = None
    for y in range(7):
        for x in range(6):
            if move(x, y):
                make_move(x, y, 'O')
                score = minimax(board, 4, float('-inf'), float('inf'), False)
                board[x][y] = ''
                if score > best_score:
                    best_score = score
                    best_move = (x, y)
    return best_move
def main():
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    red = pg.image.load("red.jpg").convert_alpha()
    yellow = pg.image.load("yellow.jpg").convert_alpha()
    background = pg.image.load("棋盘.png").convert_alpha()
    objects = []
    pg.display.set_caption("petits dinosaures")
    chess_list = [red, yellow]
    going = True
    while going:
        screen.blit(background, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                x = pos[1] // 150
                y = pos[0] // 150
                if move(x, y):
                    make_move(x, y, 'O')
                    objects.append([chess_list[1], (y * 150, x * 150)])
                    if check_win2(board) != [None, None, None, None]:
                        going = False
                    else:
                        best_move = get_best_move()
                        make_move(best_move[0], best_move[1], 'X')
                        objects.append([chess_list[0], (best_move[1] * 150, best_move[0] * 150)])
                    if check_win2(board) != [None, None, None, None]:
                        going = False

        for o in objects:
            screen.blit(o[0], o[1])
        clock.tick(60)
        pg.display.update()

    if 'X' in check_win2(board):
        print("AI获胜，恭喜恭喜啦啦啦啦")
    elif 'O' in check_win2(board):
        print("玩家获胜，恭喜恭喜啦啦啦啦")
    else:
        print("平局")

    pg.quit()



if __name__ == "__main__":
    main()

