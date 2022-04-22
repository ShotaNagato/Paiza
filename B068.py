"""
チョコの行数:num_h_cho
チョコの列数:num_w_cho
"""

# --------入力処理
num_h_cho, num_w_cho = list(map(int, input().split()))
# print(num_h_cho)
# print(num_w_cho)

# 糖度を記録する配列を準備
array_suger = [[0] * num_w_cho for i in range(num_h_cho)]
# 各糖度を入力
for i in range(num_h_cho):
    sugers = list(map(int, input().split()))
    for j in range(num_w_cho):
        array_suger[i][j] = sugers[j]
        # print(array_suger[i][j])

# 出力用配列
array_output = [["N"] * num_w_cho for i in range(num_h_cho)]

# ---------確認処理
# 全ての行分けることができたか確認用変数
check = 0
#各行のpointを記録する配列
array_point = [0 for i in range(num_h_cho)]
# 繰り返し開始
for i in range(num_h_cho):
    # 行ごとに計算
    # A,Bの合計用の変数
    sum_A = 0
    sum_B = 0
    # 基準の変数(1ずつ増える)
    point = 0

    # 端から計算 0 == 1 + 2 + 3 + 4なら次の行に 出力用配列の0にA, 1,2,3,4にBを代入
    while point < num_w_cho-1:
        for j in range(num_w_cho):
            # Aの合計求める処理
            if j <= point:
                sum_A = sum_A + array_suger[i][j]
                # print(f"{i+1}行目A合計{sum_A}")
            # Bの合計求める処理
            else:
                sum_B = sum_B + array_suger[i][j]
                # print(f"{i+1}行目B合計{sum_B}")
        if sum_A == sum_B:
            # print(f"{point+1}周目")
            # print(f'合計{i}:{sum_B}')
            check += 1
            array_point[i] = point
            break
            
        point += 1
        sum_A = 0
        sum_B = 0

# ---------出力処理
if check != num_h_cho:
    print("No")
else:
    print("Yes")
    for i in range(num_h_cho):
        for j in range(num_w_cho):
            if j <= array_point[i]:
                print("A",end="")
            else:
                print("B",end="")
        print()
    
