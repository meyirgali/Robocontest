n = int(input())
k,f = 1,0
for z in range(n):
  k,f = k+f,k
print(f*2)