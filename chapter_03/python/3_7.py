S = "1234"
N = len(S)

sum = 0

# 2進数の1の部分に＋を入れるイメージ
for bit in range(1 << (N-1)):
    tmp = 0
    for i in range(N-1):
        tmp = tmp * 10 + int(S[i])

        # [+]を挿入する位置かどうかを確認
        if bit & (1 << i):
            sum += tmp
            tmp = 0

    # 最後の部分を加算
    tmp = tmp * 10 + int(S[-1])
    sum += tmp

print(f"sum : {sum}")