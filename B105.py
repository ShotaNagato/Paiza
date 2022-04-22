# ターン数num_turn、ボードの高さh_boardと幅w_board

num_turn, h_board, w_board = list(map(int, input().split()))
# print(num_turn)
# print(h_board)
# print(w_board)

# 座標準備 全て0に初期化
array_board = [[0] * w_board for i in range(h_board)]
# print(array_board)

# ターン数×3繰り返し開始
for i in range(1,num_turn*3+1):
    # 正方形の左上のx座標ope_x, y座標open_y, 正方形の長さope_len
    ope_x, ope_y, ope_len = list(map(int, input().split()))
    # 繰り返し開始
    for j in range(ope_x,ope_x + ope_len):
        # print(j + ope_len - 2)
        if j+1 > w_board: 
            continue
        for k in range(ope_y,ope_y + ope_len):
            # print(k + ope_len - 2)
            if k+1 > h_board:
                continue
            # ---------------もし座標の値が0(色が塗られていない)なら-----------------
            if array_board[k][j] == 0:
                # もしプレイヤー1のターンなら
                if i%3 == 1:
                    array_board[k][j] = 1
                    # print(f'行{k}列{j}')
                    # print(array_board[k][j])
                # もしプレイヤー2のターンなら
                elif i%3 == 2:
                    array_board[k][j] = 2
                # もしプレイヤー3のターンなら
                else: 
                    array_board[k][j] = 3
            # ---------------もし座標の値が1(プレイヤー1)なら-----------------
            elif array_board[k][j] == 1:
                # もしプレイヤー2のターンなら
                if i%3 == 2:
                    array_board[k][j] = 3
                # もしプレイヤー3のターンなら
                elif i%3 == 0:
                    array_board[k][j] = 2

            # ---------------もし座標の値が2(プレイヤー2)なら-----------------
            elif array_board[k][j] == 2:
                # もしプレイヤー1のターンなら
                if i%3 == 1:
                    array_board[k][j] = 3
                # もしプレイヤー3のターンなら
                elif i%3 == 0:
                    array_board[k][j] = 1
            
            # ---------------もし座標の値が3(プレイヤー3)なら-----------------
            else: # if array_board[k][j] == 3:
                # もしプレイヤー1のターンなら
                if i%3 == 1:
                    array_board[k][j] = 2
                # もしプレイヤー2のターンなら
                elif i%3 == 2:
                    array_board[k][j] = 1
    # print(array_board)

# 出力処理
sum_1 = 0
sum_2 = 0
sum_3 = 0
for i in range(h_board):
    for j in range(w_board):
        if array_board[i][j] == 1:
            sum_1 += 1
        elif array_board[i][j] == 2:
            sum_2 += 1
        elif array_board[i][j] == 3:
            sum_3 += 1


print(f'{sum_1} {sum_2} {sum_3}')
    