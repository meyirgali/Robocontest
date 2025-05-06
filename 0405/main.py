x1, y1, x2, y2 = map(int, input().split())

qadamlar = max(abs(x2 - x1), abs(y2 - y1))
vaqt = qadamlar * 0.5

print(vaqt)