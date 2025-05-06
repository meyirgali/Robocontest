N,K =map(int,input().split())

if (K - 1) == 0 or N % (K - 1) != 0:
    print("False")
else:
    V = N // (K - 1)
    A = V + N
    print(A, V)