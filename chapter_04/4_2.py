# メモ化あり

N = 100 # 計算する項数

memo = [-1 for _ in range(N)] # 計算結果を保存するリスト（-1なら、保存されていない）

def calc_tribonacci(N):
    if N==1 or N==2:
        return 0
    if N==3:
        return 1

    """
    ・メモにN項目の計算結果が保存されていたら、保存されていた値を返す
    (memo内のインデックスは0~N-1)
    ・計算結果が保存されていなかったら、計算を行い、結果をmemoに保存して計算結果を返す
    """
    if memo[N-1] != -1:
        return memo[N-1]
    else:
        memo[N-1] = calc_tribonacci(N-1) + calc_tribonacci(N-2) + calc_tribonacci(N-3)
        return memo[N-1]

print(calc_tribonacci(N))
"""
引数として、項数を与える。
(公式github?では、0項目スタートだったが、本コードでは、1項目スタート)
"""
"""
計算量はO(N) ・・・計算結果がメモ化されているため、各項の計算を一回ずつ行えばいい
"""