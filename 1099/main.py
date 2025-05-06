def u(n):
    return (3+n//3*3)*(n//3)//2
def y(n):
    return (21+n//21*21)*(n//21)//2
  
a,n= map(int,input().split())

javob = (u(n) - y(n)) - (u(a-1)- y(a-1))

print(javob)