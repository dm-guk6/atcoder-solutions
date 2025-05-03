N, M = map(int, input().split())
node = {i + 1:[0] for i in range(N)}
s = set()

for i in range(M):
    A, B = map(int, input().split())
    if not (A, B) in s and not (B, A) in s:
        s.add((A, B))
        s.add((B, A))
        node[A][0] += 1
        node[A].append(B)
        node[B][0] += 1
        node[B].append(A)

for i in node.values():
    if i[0] != 2 or len(i) != 3 or M != N:
        print('No')
        exit()

if len(node[1]) < 3:
    print("No")
    exit()

cnt = 0
def dfd(no1, no2, pred, now):
    global cnt
    if cnt == N and now == 1:
        print("Yes")
        exit()

    if no1 == pred or pred == -1:
        cnt += 1
        dfd(node[no2][1], node[no2][2], now, no2)
    elif no2 == pred:
        cnt += 1
        dfd(node[no1][1], node[no1][2], now, no1)
    else:
        print("No")
        exit()



dfd(node[1][1], node[1][2], -1, 1)