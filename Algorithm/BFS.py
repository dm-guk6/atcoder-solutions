from collections import deque

# 「初期設定」
H, W = map(int, input().split())
# 色マス作成
math = [input() for _ in range(H)]
# 訪問有無のマス作成
visited = [[False for _ in range(W)] for _ in range(H)]
visited[0][0] = True

ans = -1 # マス数
queue = deque([[0, 0, 0]]) # [行数,列数,歩数]

# 「幅優先探索」
while(queue):
    # 行数、列数、移動コスト
    i, j, cost = queue.popleft()

    if i == H - 1 and j == W - 1:
        ans = cost
        break

    # 上
    I = i - 1
    if I >= 0 and math[i][j] != math[I][j] and not visited[I][j]:
        visited[I][j] = True
        queue.append([I, j, cost + 1])

    # 下
    I = i + 1
    if I < H and math[i][j] != math[I][j] and not visited[I][j]:
        visited[I][j] = True
        queue.append([I, j, cost + 1])

    # 左
    J = j - 1
    if J >= 0 and math[i][j] != math[i][J] and not visited[i][J]:
        visited[i][J] = True
        queue.append([i, J, cost + 1])

    # 右
    J = j + 1
    if J < W and math[i][j] != math[i][J] and not visited[i][J]:
        visited[i][J] = True
        queue.append([i, J, cost + 1])

print(ans)