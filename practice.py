
# 論理値表まんま
table_mul = [[0, 0, 0], [0, 1, 1], [0, 1, 2]]

# 論理値表まんま
table_add = [[0, 1, 2], [1, 1, 2], [2, 2, 2]]


def eval_exp(line, env):

    # 数字が来てたらその部分intにして返却
    if line[0] in '012':
        return int(line[0]), line[1:]
    # PQR来てたら辞書に対応する文字にして返却
    if line[0] in 'PQR':
        return env[line[0]], line[1:]
    # -来てたらそれより後ろの文字をみて012かPQRだろからそれとってきて
    # -なら2 - vってするとうまい具合に反転処理になる
    if line[0] == '-':
        v, rest = eval_exp(line[1:], env)
        return 2 - v, rest
    # (なら
    if line[0] == '(':
        # まず最初にくるやつに数字とか文字とか反転とかの処理して保存
        v1, rest1 = eval_exp(line[1:], env)
        # 最初の文字とか数字の一個となりを保存(100%+とか*とかの値)
        ope = rest1[0]
        # rest1の[1]以降が二つ目の文字　一個目の文字とおんなじ感じの処理を施す
        # rest2[1:]だから)は飛ばしてる
        v2, rest2 = eval_exp(rest1[1:], env)

        # +だったら+の論理値表みてこれでv1～v2の処理終わったからそれ以降の処理をって感じ
        if ope == '+':
            return table_add[v1][v2], rest2[1:]
        # *だったら*の論理値表みてまぁ+とおんなじ感じ
        if ope == '*':
            return table_mul[v1][v2], rest2[1:]
        raise RuntimeError('Why', ope) # なんか謎なのがきたらエラーにする


def solve(line):
    # 結果0にする
    result = 0
    # 0~2の全組み合わせ(27通り)試し2になる組み合わせをカウント
    for pv in range(0, 3):
        for qv in range(0, 3):
            for rv in range(0, 3):
                # {}は上でenvで使われてる辞書
                # _はとりあえずある返り値置き場所かと
                v, _ = eval_exp(line, {'P': pv, 'Q': qv, 'R': rv})
                if v == 2:
                    result += 1
    return result


def main():
    while True:
        # 読み込み
        line = input()

        # .を読み込んだら終了
        if line == '.':
            break
        
        # 関数実行
        print(solve(line))


main()