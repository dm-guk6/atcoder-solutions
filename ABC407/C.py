S = input()
S = S[::-1]
cnt = int(S[0])
for i in range(1, len(S)):
    if int(S[i]) - cnt >= 0:
        cnt += int(S[i])
    else:
        cnt += 10 - abs(int(S[i]) - cnt) % 10
print(cnt)