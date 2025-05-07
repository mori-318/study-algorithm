# メモ化なし

N = 100 # 計算する項数

def calc_tribonacci(N):
    if N==1 or N==2:
        return 0
    if N==3:
        return 1

    return calc_tribonacci(N-1) + calc_tribonacci(N-2) + calc_tribonacci(N-3)

print(calc_tribonacci(N))
"""
引数として、項数を与える。
(公式github?では、0項目スタートだったが、本コードでは、1項目スタート)
"""