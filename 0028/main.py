N = int(input())

for i in range(N):
    A_x, A_y, B_x, B_y = map(int, input().split())

    A__x = 2 * B_x - A_x
    A__y = 2 * B_y - A_y

    print(A__x,A__y)