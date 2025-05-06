s, p = map(int, input().split())

for x in range(1, s):
    y = s - x
    if x * y == p:
        print(y, x)
        break
else:
    print(-1)