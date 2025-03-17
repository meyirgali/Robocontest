a,b,c = map(int,input().split())
result = max(c-b,b-a)-1
print(result)