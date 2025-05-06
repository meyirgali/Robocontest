n,m = list(map(int,input().split()))
result = -1
if m % 2 == 0:
    result = n + m // 2+1
print(result)