x1, v1, x2, v2 = map(int,input().split())

javob = "NO"
if v1 > v2:
    if (x2 - x1) % (v1 - v2) == 0:
        javob = "YES"

print(javob)