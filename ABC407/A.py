A, B = map(int, input().split())
small = A // B
big = (A - 1) // B + 1
sas = abs(A / B - small)
sab = abs(A / B - big)

if sas < sab:
    print(small)
else:
    print(big)