MOD = 10**9 + 7

N = int(input())

a = (N + 1)
b = N * (N + 1) // 2
c = N * (N + 1) * (2 * N + 1) // 6

s = a + 3 * b + 3 * c
print(s % MOD)