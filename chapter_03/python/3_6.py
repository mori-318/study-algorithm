K = 10
N = 20

count = 0
for x in range(K):
    for y in range(K):
        z = N-x-y
        if (z>=0) and (z<=K):
            count += 1

print(f"count : {count}")

"""
計算量はO(N^2)
"""