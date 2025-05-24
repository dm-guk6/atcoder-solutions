S = input()
S = S[::-1]
B =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = int(S[0])
for i in range(1, len(S)):
    cnt += B[int(S[i]) - cnt % 10]
cnt += len(S)
print(cnt)