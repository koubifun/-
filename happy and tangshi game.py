ass=1


def mauvel(i):
    if board[0][i] != "":
        print("此列已满，请重下")
        return True
while ass <100:
    xx = int(input(" 你要单人还是双人?(请打出1或2） "))
    if xx == 2:
        def check_win(x):
            for line in x:
                if ''.join(line).find('red' * 4) != -1:
                    print("红棋获胜，恭喜恭喜啦啦啦啦")
                    return 0
                elif ''.join(line).find('yellow' * 4) != -1:
                    print("黄棋获胜，恭喜恭喜啦啦啦啦")
                    return 1
            else:
                return -1  # 判断胜利方式


        def check_win2(board):
            board_b = [list(line) for line in zip(*board)]  # 将表格行列调换
            board_c = [[] for line in range(12)]
            for x in range(6):
                for y in range(7):
                    board_c[x + y].append(board[x][y])
            board_d = [[] for line in range(12)]
            for x in range(6):
                for y in range(7):
                    board_d[x - y].append(board[x][y])  # 定义列，斜行
            return [check_win(board), check_win(board_b), check_win(board_c), check_win(board_d)]  # 最终判断胜利方式


        def zth(y, color):
            i = 0
            while i < 6:
                if board[5 - i][y] != '':
                    i = i + 1
                else:
                    board[5 - i][y] = color
                    for i in board:
                        print(i)
                    return True


        # 落子函数

        board = [[''] * 7 for line in range(6)]

        for line in board:
            print(line)  # 棋盘
        lzy = 0
        szy = True
        while szy:
            if lzy == 0:
                print('这是红棋的回合')
                y = int(input("请选择你要下棋的那一列"))
                if mauvel(y):
                    lzy = 0
                else:
                   zth(y, "red")
                   lzy = 1
                if 0 in check_win2(board):
                    szy = False
                elif 1 in check_win2(board):
                    szy = False  # 停止
            else:
                print('这是黄棋的回合')
                y = int(input("请选择你要下棋的那一列"))
                if mauvel(y):
                    lzy = 0
                else:
                    zth(y, "yellow")
                    lzy = 0
                if 0 or 1 in check_win2(board):
                    szy = False
    # 相互落子方式

    if xx==1:
        def check_win(x):
            for line in x:
                if ''.join(line).find('red' * 4) != -1:
                    print("红棋获胜，恭喜恭喜啦啦啦啦")
                    return 0
                elif ''.join(line).find('yellow' * 4) != -1:
                    print("黄棋(computer)获胜，恭喜恭喜啦啦啦啦")
                    return 1
            else:
                return -1  # 判断胜利方式


        def check_win2(board):
            board_b = [list(line) for line in zip(*board)]  # 将表格行列调换
            board_c = [[] for line in range(12)]
            for x in range(6):
                for y in range(7):
                    board_c[x + y].append(board[x][y])
            board_d = [[] for line in range(12)]
            for x in range(6):
                for y in range(7):
                    board_d[x - y].append(board[x][y])  # 定义列，斜行
            return [check_win(board), check_win(board_b), check_win(board_c), check_win(board_d)]  # 最终判断胜利方式


        def zth(y, color):
            i = 0
            while i < 6:
                if board[5 - i][y] != '':
                    i = i + 1
                else:
                    board[5 - i][y] = color
                    for i in board:
                        print(i)
                    return True


        # 落子函数

        board = [[''] * 7 for line in range(6)]
        for line in board:
            print(line)  # 棋盘
        lzy = 0
        szy = True
        while szy:
            if lzy == 0:
                print('这是红棋的回合')
                y = int(input("请选择你要下棋的那一列"))
                if mauvel(y):
                    lzy = 0
                else:
                   zth(y, "red")
                   lzy = 1
                if 0 in check_win2(board):
                    szy = False
                elif 1 in check_win2(board):
                    szy = False  # 停止

            else:
                print('这是黄棋(computer)的回合')
                import random
                y = random.randint(0, 5)
                print("黄棋选择下",y)
                if mauvel(y):
                    lzy = 1
                else:
                    zth(y, "yellow")
                    lzy = 0
                    if 0 or 1 in check_win2(board):
                        szy = False

    # 相互落子方式










