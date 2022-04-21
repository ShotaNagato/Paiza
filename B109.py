# ----------------------入力、席座標作成処理
"""
予約済みの席数: num_reserved_seat
縦の席数: num_seat_h
横の席数: num_seat_w
最も見やすい席の座標: (position_clear_seat_h, position_clear_seat_w)
座席配列: array_seat
"""
# 各変数で　入力値を取得
num_reserved_seat, num_seat_h, num_seat_w, position_clear_seat_h, position_clear_seat_w = list(map(int, input().split()))

# 座席配列の値を全て0で初期化
array_seat = [[0] * num_seat_w for i in range(num_seat_h)]

# 予約済み席の数繰り返し
for i in range(num_reserved_seat):
    # 予約済みの席の座標を入力
    index = list((map(int, input().split())))
    # 予約済みの席の座標の値を1にする
    array_seat[index[0]][index[1]] = 1


# 最も見やすい席が予約されていなければ(座標の値が0なら) 座標を返して終了
if array_seat[position_clear_seat_h][position_clear_seat_w] == 0:
    print(f'{position_clear_seat_h} {position_clear_seat_w}')
# ----------------------マンハッタン距離を求める処理
else:
    # マンハッタン距離用の配列をゼロで初期化
    array_man = [[0] * num_seat_w for i in range(num_seat_h)]
    # 最短の距離を表す変数 初期値は座席の中の最大値を設定
    min = num_seat_h + num_seat_w - 2
    # 座席分繰り返し開始
    for i in range(num_seat_h):
        for j in range(num_seat_w):
            # もし座席が予約済みでなければ
            if array_seat[i][j] != 1:
                # マンハッタン距離を配列arary_manに追加
                array_man[i][j] = abs(i - position_clear_seat_h) + abs(j - position_clear_seat_w)
                # もしminよりも小さければ(距離が短ければ)minを更新
                if min > array_man[i][j]:
                    min = array_man[i][j]
    # ----------------------出力処理
    for i in range(num_seat_h):
        for j in range(num_seat_w):
            if array_man[i][j] == min:
                print(f'{i} {j}')

