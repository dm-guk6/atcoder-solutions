N = int(input())
S = [input() for _ in range(N)]
i = 0
cnt = 0
for s in S:
    if s == "login":
        i = 1
    elif s == "logout":
        i = 0
    elif s == "private" and i == 0:
        cnt += 1


print(cnt)