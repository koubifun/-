import pygame as pg
import random
WIDTH = 1050
HEIGHT = 900
board = [[''] * 7 for line in range(6)]

a=0
b=0
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


import random

def diannao_panduan():
    flag = False
    for x in range(6):
        for y in range(7):
            if move(x,y):
                make_move(x,y,"O")
                if 'O' in check_win2(board):
                    print('can win, change color')
                    board[x][y]="X"
                    flag = True
                    break
                else:
                    board[x][y]=""
                    make_move(x,y,"X")
                    if 'X' in check_win2(board):
                        flag = True
                        break
                    else:
                        board[x][y]=""
        if flag:
            break
    if not flag :
        for x in range(6):
            for y in range(7):
                if move(x, y):
                    make_move(x, y, "X")
                    if x>0:
                        make_move(x-1,y,"O")

                        if 'O' in check_win2(board):
                            board[x-1][y]=""
                            board[x][y]=""
                            global a
                            a=x
                            global b
                            b=y
                        else:
                            board[x - 1][y] = ""
                            board[x][y] = ""

        xx=False
        for i in range(1,5):
            if board[5][i]=="O"and board[5][i+1]=="O"and board[5][i-1]==""and board[5][i+2]=="0":
                print("g")
                make_move(5,i-1,"X")
                x=5
                y=i-1
                return(x,y)


        for x in range(6):
            for y in range(7):
                if move(x,y):
                    if x<5:
                        if (board[x+1][y]=="X") :
                            print("m")
                            make_move(x, y, "X")
                            return (x,y)

        going = True
        while going:
            x = random.randint(0, 5)
            y = random.randint(0, 6)
            print("l")
            print(a,b)
            while (x==a) and (y==b):
                x = random.randint(0, 5)
                y = random.randint(0, 6)
            if move(x, y):
                make_move(x, y, "X")
                going = False
        return (x, y)

    if flag :
        print('diannao_panduan, flag, quit function',x,y)
        return (x,y)
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
    ooo=False
    while going:
        screen.blit(background, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                y = pos[0] // 150
                for i in range (6):
                    if move(i, y):
                        make_move(i, y, 'O')
                        objects.append([chess_list[1], (y * 150, i * 150)])

                        print(check_win2(board))
                        if check_win2(board) != [None, None, None, None]:
                            going = False
                        else:
                            c, d = diannao_panduan()
                            print(board)
                            objects.append([chess_list[0], (d * 150, c * 150)])
                            if check_win2(board) != [None, None, None, None]:
                                ooo=True
        for o in objects:
            screen.blit(o[0], o[1])
        clock.tick(60)
        pg.display.update()
        if ooo:
            pg.time.wait(1000)
            going=False




    print (check_win2(board))
    if 'X' in check_win2(board):
        print("AI获胜，恭喜恭喜啦啦啦啦")
    elif 'O' in check_win2(board):
        print("玩家获胜，恭喜恭喜啦啦啦啦")
    else:
        print("平局")

    pg.quit()



if __name__ == "__main__":
    main()
