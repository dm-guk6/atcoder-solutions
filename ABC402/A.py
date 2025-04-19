S = input()
out = []
for s in S:
    if ord(s) < 97:
        out.append(s)
print("".join(out))