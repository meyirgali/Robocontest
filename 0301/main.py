N = int(input())
nums = list(map(int, input().split()))

if nums == list(range(1, N + 1)):
    print("YES")
else:
    print("NO")