# 1.入力
a = list(map(int, input().split()))

# 2.並び替え
a.sort(reverse=True)

# 3.3番目を出力
print(a[2])