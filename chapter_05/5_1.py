import random

def chmax(a, b):
    return max(a, b)

if __name__ == "__main__":
    N = 10
    dp = [[0 for _ in range(3)] for _ in range(N+1)]
    a = [[random.randint(1, 10) for _ in range(3)] for _ in range(N)]

    # i日目からi+1日目
    for i in range(N):
        # i日目の状態は、j、i+1日目の状態は、k
        for j in range(3): # i日目の選択肢
            for k in range(3): # i+1日目の選択肢
                if j != k:
                    dp[i+1][k] = chmax(dp[i+1][k], dp[i][j]+a[i][k])

    result = max(dp[N])
    print(result)