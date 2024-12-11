def chmin(a, b):
    return min(a, b)

if __name__ == "__main__":
    S = input()
    T = input()

    # dp[i][j] --> Sの最初のi文字分と、Tの最初のj文字分との間の編集距離
    dp = [[float('inf') for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]

    # 初期化
    for i in range(len(S) + 1):
        dp[i][0] = i
    for j in range(len(T) + 1):
        dp[0][j] = j

    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            # 変更操作（右下に向かう処理）
            if S[i - 1] == T[j - 1]:  # 変更なし
                dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1])
            else:  # 変更あり
                dp[i][j] = chmin(dp[i][j], dp[i - 1][j - 1] + 1)
            # 削除操作（下に向かう処理）
            dp[i][j] = chmin(dp[i][j], dp[i - 1][j] + 1)
            # 挿入操作（右に向かう処理）
            dp[i][j] = chmin(dp[i][j], dp[i][j - 1] + 1)

    # 答えの出力
    print(dp[len(S)][len(T)])