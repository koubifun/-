import pygame as pg

WIDTH = 1050
HEIGHT = 900
board = [[''] * 7 for line in range(6)]


def zth(x,y,color):
    if board[x][y] != '':
        print('该位置已有小恐龙，你是小唐氏吧')
        return False
    else:
        if x==5:
            board[x][y]=color
            return True
        elif board[x+1][y] == '':
            print('下方格子有空格，请重新选择位置')
            return False
        else:
            board[x][y] = color
            return True


def check_win(board):
    for line in board:
        if ''.join(line).find('X' * 4) != -1:
            print("红棋获胜，恭喜恭喜啦啦啦啦")
            return 0
        elif ''.join(line).find('O' * 4) != -1:
            print("黄棋获胜，恭喜恭喜啦啦啦啦")
            return 1
    return -1


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
    letter_list = ['X', 'O']
    szy = 0
    going = True
    while going:
        screen.blit(background, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                a,b,i,j=0,0,0,0
                while i<=8:
                    if pos[0]>i*150 and pos[0]<i*150+150:
                        a=i *150
                        break
                    else:
                         i=i+1
                while j<=8:
                    if pos[1] > j * 150 and pos[1] < j * 150 + 150:
                        b = j * 150
                        break
                    else:
                        j=j+1

                if zth(j,i, letter_list[szy]):
                    objects.append([chess_list[szy], (a,b)])
                    szy = [1, 0][szy]
                    if 0 in check_win2(board) or 1 in check_win2(board):
                        going = False
        for o in objects:
            screen.blit(o[0], o[1])
        clock.tick(60)
        pg.display.update()

main()
pg.quit()