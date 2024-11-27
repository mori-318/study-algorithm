# メモ化なし

def calc_tribonacci(n):
    if n==1 or n==2:
        return 0
    if n==3:
        return 1
    return calc_tribonacci(n-1) + calc_tribonacci(n-2) + calc_tribonacci(n-3)

print(calc_tribonacci(10))
"""
引数として、項数を与える。
(公式github?では、0項目スタートだったが、本コードでは、1項目スタート)
"""