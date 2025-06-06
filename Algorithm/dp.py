N = int(input()) # 並んでいる数字の個数～
a = list(map(int, input().split())) # 数値入力　最後はイコールっす

# 0～20の値を保存してそれが11回分あるよ
dp = [[0 for _ in range(21)] for _ in range(N)]
# 0層目のスタート地点の値のカウントを1にします!!
dp[0][a[0]] = 1

# なんで最後から2番目なの? 1層目は8でそれスタートにしてるから実際見る個数はN-1になるはずで
# 最終層の一個前分かればもう分かる
for i in range(N - 2):
    # 21個数字見ていきましょう
    for j in range(21):
        d = dp[i][j]
        if d != 0: #　すでにきてた値の場合まぁ来ん時だけよね動くの
            # 加算して20以下ならその層に値プラスしてんで現在そこまで来てたパターン数も加算
            if j + a[i + 1] <= 20:
                dp[i + 1][j + a[i + 1]] += d
            # 減算して0以上ならその層に値プラスしてそこまできてたパターン数も加算
            if j - a[i + 1] >= 0:
                dp[i + 1][j - a[i + 1]] += d
# 最後からN - 1層目で目的の値になる個数
print(dp[(N - 1) - 1][a[N - 1]])