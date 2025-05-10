N = int(input())
A = list(map(int, input().split()))

mullist = list()
mullist.append(A[0])
dp = []
sum = A[0] * A[1]
for i in range(1, N - 1):
    A[i] += A[i - 1]
    sum += A[i] * A[i + 1]

print(sum)