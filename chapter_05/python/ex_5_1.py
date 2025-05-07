# Frog問題を動的計画法で解く

if __name__ == "__main__":
    N =7
    h = [2,9,4,5,1,6,10]

    dp = [10000 for _ in range(N)] # とりあえず、初期値は10000に設定（十分大きな数）
    dp[0] = 0 # 初期条件

    for i in range(1, N):
        if i == 1:
            dp[i] = abs(h[i] - h[i-1]) # i==1の時は、dp[0]が0なので、高さの差分がそのままdpに入る
        else:
            dp[i] = min([dp[i-1] + abs(h[i]-h[i-1]), dp[i-2] + abs(h[i]-h[i-2])])

    print(f"最小コスト：{dp[N-1]}") # dp[N-1]=8