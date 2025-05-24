# 1.入力する
S = input()
nman = []

# 2.当選者を数える
for i in range(ord('a'), ord('z') + 1):
    nman.append(S.count(chr(i)))
# 3.最大値求める
mx = max(nman)

# 4.一番多い人を出力する
for i in range(26):
    if nman[i] == mx:
        print(chr(ord('a') + i))

# 最も大きい人を出力する
# if na > nb and na > nc:
#     print('a')
# elif nb > na and nb > nc:
#     print('b')
# elif nc > na and nc > nb:
#     print('c')
