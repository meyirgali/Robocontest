m,n = map(int,input().split())
toshlar = list(map(int,input().split()))

toshlar.sort(reverse=True)
total = 0
count = 0
for stones in toshlar:
    total += stones
    count += 1
    if total >= m:
        print(count)
        break
else:
    print(-1)