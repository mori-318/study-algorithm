global count # 条件を満たす個数を記録
count = 0

def func(K, current_num, use):
    global count

    if current_num > K: # Kを超える場合はreturn
        return
    if use == 0b111: # ビット演算で、753数であることを確認
        count += 1

    # 7,5,3のそれぞれで探索を進める
    func(K, current_num*10+7, use|0b001) # ７を付け加える
    func(K, current_num*10+5, use|0b010) # ５を付け加える
    func(K, current_num*10+3, use|0b100) # ３を付け加える

if __name__ == "__main__":
    K = 10000
    func(K, 0, 0)
    print(count)

"""
計算量はO(3^d) d:Kの桁数
"""