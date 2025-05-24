# 1.ビンゴカード作成
A = []
for _ in range(0, 3):
    # 1行分受け取る
    row = list(map(int, input().split()))
    # 1行分追加する
    A.append(row)
 # A = [input() for _ in range(3)]

# 2.ビンゴカード穴あき確認
M = [[False, False, False], [False, False, False], [False, False, False]]

# # 穴あき確認
# M = []
# for i in range(0, 3):
#     # 1行分保存
#     row = []
#     for j in range(0, 3):
#         row.append(False)
#     # 1行分で保存
#     M.append(row)

# M = [[False for _ in range(3)] for _ in range(3)]

# 3.ガラガラ回して穴あき
# ガラガラ回数入力
N = int(input())

# ガラガラ回す
for _ in range(0, N):

    # あってれば入力
    b = int(input())

    for i in range(0, 3):
        for j in range(0, 3):
            # 一致してれば・・・
            if A[i][j] == b:
                M[i][j] = True

# 4.ビンゴ確認
bingo = False

# 列ビンゴ確認
for i in range(0, 3):
    # Trueで保存されてるからこれで印確認
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True

# 行ビンゴ確認
for i in range(0, 3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True

# 右斜めビンゴ確認
for i in range(0, 3):
    if M[0][0] and M[1][1] and M[2][2]:
        bingo = True

# 左斜めビンゴ確認
for i in range(0, 3):
    if M[2][0] and M[1][1] and M[0][2]:
        bingo = True

# 5.ビンゴ出力
if bingo:
    print("Yes")
else:
    print("No")