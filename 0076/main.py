a, b, c, d, e, f, g = map(int, input().split())
h = int(input())
x = h - (a + b + c + d + e + f + g)
if x > 0:
  print(x)
else:
  print(0)