N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

S[i][j] = S[j][(N - 1) - i]
print(S)