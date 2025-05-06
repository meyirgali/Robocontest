import math

T = int(input())
N_list = list(map(int, input().split()))

for N in N_list:
    if N == 1:
        print(0)
        continue

    max_gcd = 0
    for d in range(N // 2, 0, -1):
        k = N // d
        if k >= 2:
            max_gcd = d
            break
    print(max_gcd)