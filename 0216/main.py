n = int(input())

count3 = (n - 3) // 10 + 1 if n >= 3 else 0
count7 = (n - 7) // 10 + 1 if n >= 7 else 0

print(count3 + count7)
