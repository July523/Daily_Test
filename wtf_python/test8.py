# coding=utf-8 
# @Time :2018/12/16 17:56

"""
A tic-tac-toe where X wins in the first attempt!/一蹴即至!

具体参考：
https://github.com/leisurelicht/wtfpython-cn?utm_source=
qq&utm_medium=social&utm_oi=950291290743590912#structure-of-the
-examples%E7%A4%BA%E4%BE%8B%E7%BB%93%E6%9E%84

"""

# 我们先初始化一个变量row
row = [''] * 3  # row i['', '', '']
# 并且创建一个变量board
board = [row] * 3

print(board)
print(board[0])
print(board[0][0])

board[0][0] = "X"
print(board)

# 当通过对 row 做乘法来初始化 board 时, 内存中的情况
# (每个元素 board[0], board[1] 和 board[2] 都和 row 一样引用了同一列表.)

# 我们可以通过不使用变量 row 生成 board 来避免这种情况.

board_1 = [[''] * 3 for _ in range(3)]
board_1[0][0] = "X"
print(board_1)