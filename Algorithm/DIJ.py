import sys
from heapq import heappush, heappop
#ファイルから読み込みたい場合は、直後の行を有効化してください。完成時は、コメントに戻すのを忘れずに！
#import sys; sys.stdin =  open('hopData/sample.in', 'r', )
ONE_HOP = 10.00001 # 念のための誤差対策で0.01プラスしてる
MAX = sys.float_info.max # 無限大　ありえない数ならなんでもいいはず


def solve() -> float: # これはコメント的な意味でfloatの型を返すよってこと　見やすさのため　動的型付き言語だから
    q = []
    cost = [MAX for _ in range(n)]

    start = 0 # スタート地点のインデックス番号
    goal = n - 1 # 終了のインデックス番号
    cost[0] = 0.0 # 今のコスト

    heappush(q, [0.0, start])

    while q:
        path, here = heappop(q) # 現在地点のコストと番号取得
        # もっといい道がある
        if cost[here] < path:
            continue
        # 現在ゴールなら終わる
        if here == goal:
            break
        # 全点のペア確認
        for j in range(1, n):
            if here == j:
                continue
            # 距離計算
            diff = points[j] - points[here]
            dist = abs(diff)
            #

            # 10よりでかいとこには行けないから別の点
            if dist > ONE_HOP:
                continue

            # 前回までと今回の距離が次のパス
            next_path = path + dist

            # もっといいとこあれば無視
            if cost[j] <= next_path:
                continue
            else:
                cost[j] = next_path # そうじゃなかったら次のパスへ
                heappush(q, [next_path, j]) # 追加する

    return cost[goal] if cost[goal] < MAX else 0.0 # 辿り付けなかったらMAXのままだから未更新ってことで0を出力


# ここmain文とかじゃなくただのループだ
while True:
    n = int(input()) # 点の個数を入力

    # 点0個で終了
    if n == 0:
        exit(0)
    # 座標を複素数化して距離の計算を楽にしている
    points = [complex(*list(map(int, input().split()))) for _ in range(n)]
    result = solve() # 0 0から 12 0に行く最短の距離の大きさ
    print(result)

"""
20.0000
22.1854
0.0000
219.5084
81.0
"""