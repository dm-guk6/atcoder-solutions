from collections import deque
Q = int(input())
q = deque()
for _ in range(Q):
    i_num = list(map(int, input().split()))
    if i_num[0] == 1:
        q.append(i_num[1])
    else:
        a = q.popleft()
        print(a)