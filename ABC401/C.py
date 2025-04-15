N, K = map(int, input().split())
A = [1 for _ in range(N + 1)]
i = K
while (1):
    if i > N:
        i = N
        break
    if i == K:
        A[i] = K
    elif i > K:
        A[i] = 2 * A[i - 1] - A[i - K - 1]
    A[i] %= 10 ** 9
    i += 1


print(A[i] % 10 ** 9)