def func(i, w, a):
    # ベースケース
    if i==0:
        if w==0:
            return True
        else:
            return False

    # wが負の値の場合
    if w < 0:
        return False

    # メモの確認
    if memo[i-1][w-1] != -1:
        return memo[i-1][w-1]

    # a[i-1]を選ばない場合
    if func(i-1, w, a):
        memo[i-1][w-1] = True
        return memo[i-1][w-1]

    # a[i-1]を選ぶ場合
    if func(i-1, w-a[i-1], a):
        memo[i-1][w-1] = True
        return memo[i-1][w-1]

    # どちらもFalseの場合
    memo[i-1][w-1] = False
    return memo[i-1][w-1]


if __name__ == "__main__":
    a = [11,22,42,61,33,64,21,51,19,12] # テキトー
    n = len(a)
    w = 32 # ターゲット
    i=7
    memo = [[-1 for _ in range(w)] for _ in range(i)]
    if func(i, w, a):
        print("Yes!")
    else:
        print("No...")

    """
    計算量はO(n*w)
    """
