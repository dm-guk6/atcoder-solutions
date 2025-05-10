N , M = map(int, input().split())

A = list(map(int, input().split()))
a = dict()
cnt = 0

for i in range(N):
    a[A[i]] = a.get(A[i], i)
    if len(a) == M:
        break
else:
    print(0)
    exit()
a = sorted(a.items(), key=lambda x : x[1], reverse=True)
print(N - a[0][1])