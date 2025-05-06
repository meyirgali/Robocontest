a,b,c,x = map(int,input().split())
s = a*x**2+b*x+c
if s == 0:
  print("YES")
else:
  print("NO")