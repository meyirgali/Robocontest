import math
def chess(n):
    a = n // 2
    b = n - a
    return (a+1)*(b+1)

n = int(input())
print(chess(n))