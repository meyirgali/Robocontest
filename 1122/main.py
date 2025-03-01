a=input()

a0=a.count('0')

a2=a.count('2')

a4=a.count('4')

a6=a.count('6')

a8=a.count('8')

a02468=a0+a2+a4+a6+a8

if len(a)%2==1:

    if a02468==0:

        print("YES")

    else:

        print("NO")

else:

    print("NO")