x = int(input())
n = list(map(int,input().split()))
n.remove(max(n))
print(max(n))