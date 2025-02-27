N = int(input())
a,b,c = map(int,input().split())
s = (a+b+c)
if s >= N:
    print("Yes")
else:
    print("No")