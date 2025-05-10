from collections import deque
H, W = map(int, input().split())

math = [input() for _ in range(H)]
visited = [[False for _ in range(H)]]
visited[0][0] = True

q = deque([[0, 0, 0, 0]])

while (1):
    i, j, cost, dir = q.popleft()

    if i == 0 and j == 0:
        break

    I = i - 1
    if I >= 0 and q[I][j] == '#' and visited[I][j] == False:
        visited[I][j] = True
        q.append([I, j, cost + 1, dir])