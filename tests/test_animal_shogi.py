from pgx.animal_shogi import *
import numpy as np


INIT_BOARD = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 11(右上) 後手のゾウ
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12 空白
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13 空白
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 14(右下) 先手のキリン
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 21 後手ライオン
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 22 後手ヒヨコ
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 23 先手ヒヨコ
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 24 先手ライオン
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 31 後手キリン
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 32 空白
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 33 空白
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 34 先手ゾウ
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 先手ヒヨコ
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 先手キリン
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 先手ゾウ
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 後手ヒヨコ
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 後手キリン
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 後手ゾウ
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 手番の情報
])
#  doctest用の盤面
TEST_BOARD = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 11 後手ゾウ
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12 先手ヒヨコ
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13 空白
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 14 先手のニワトリ
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 21 後手ライオン
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 22 空白
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 23 先手キリン
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 24 後手キリン
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 31 空白
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 32 空白
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 33 空白
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 34 先手ライオン
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 先手ヒヨコ
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 先手キリン
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 先手ゾウ
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 後手ヒヨコ
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 後手キリン
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 持ち駒 後手ゾウ
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 手番の情報)
])


def test_turn_change():
    b = turn_change(INIT_BOARD, 0)
    assert b[18][0] == 0
    assert b[18][1] == 1


def test_move():
    b = move(INIT_BOARD, 0, 6, 5, 1, 1, 0)
    assert b[6][0] == 1
    assert b[5][1] == 1
    assert b[12][1] == 1
    b2 = move(TEST_BOARD, 0, 1, 0, 1, 3, 1)
    assert b2[0][5] == 1
    assert b2[1][0] == 1
    assert b2[14][2] == 1


def test_drop():
    b = drop(TEST_BOARD, 0, 2, 3)
    assert b[2][3] == 1
    assert b[14][0] == 1


def test_owner_piece():
    assert owner_piece(INIT_BOARD, 3) == (0, 2)
    assert owner_piece(INIT_BOARD, 5) == (1, 1)
    assert owner_piece(INIT_BOARD, 9) == (2, 0)


def test_legal_move():
    assert legal_moves(INIT_BOARD, 0) == [[3, 2, 2, 0, 0], [6, 5, 1, 1, 0], [7, 2, 4, 0, 0], [7, 10, 4, 0, 0]]
    assert legal_moves(INIT_BOARD, 1) == [[4, 1, 4, 0, 0], [4, 9, 4, 0, 0], [5, 6, 1, 1, 0], [8, 9, 2, 0, 0]]
    assert legal_moves(TEST_BOARD, 0) == [[1, 0, 1, 3, 1], [3, 2, 5, 0, 0], [3, 7, 5, 2, 0], [6, 2, 2, 0, 0], [6, 5, 2, 0, 0], [6, 7, 2, 2, 0], [6, 10, 2, 0, 0], [11, 7, 4, 2, 0], [11, 10, 4, 0, 0]]


def test_legal_drop():
    assert legal_drop(TEST_BOARD, 0) == [[2, 1], [5, 1], [9, 1], [10, 1], [2, 2], [5, 2], [8, 2], [9, 2], [10, 2], [2, 3], [5, 3], [8, 3], [9, 3], [10, 3]]


def test_legal_drop_moves():
    assert legal_drop_moves(TEST_BOARD, 0) == [(0, [1, 0, 1, 3, 1]), (0, [3, 2, 5, 0, 0]), (0, [3, 7, 5, 2, 0]), (0, [6, 2, 2, 0, 0]), (0, [6, 5, 2, 0, 0]), (0, [6, 7, 2, 2, 0]), (0, [6, 10, 2, 0, 0]), (0, [11, 7, 4, 2, 0]), (0, [11, 10, 4, 0, 0]), (1, [2, 1]), (1, [5, 1]), (1, [9, 1]), (1, [10, 1]), (1, [2, 2]), (1, [5, 2]), (1, [8, 2]), (1, [9, 2]), (1, [10, 2]), (1, [2, 3]), (1, [5, 3]), (1, [8, 3]), (1, [9, 3]), (1, [10, 3])]


if __name__ == '__main__':
    test_turn_change()
    test_move()
    test_drop()
    test_owner_piece()
    test_legal_move()
    test_legal_drop()
    test_legal_drop_moves()