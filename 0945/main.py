a,b = map(int,input().split())
S = a * b
P = 2 * (a + b)
if S > P:
    print(S)
else:
    print(P)