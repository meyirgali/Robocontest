a,b = map(int,input().split())
s = b // a
if b%a == 0:
    print("Yes")
else:
    print("No")