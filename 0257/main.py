s = input()

first = s.find('1')
last = s.rfind('1')

segment = s[first:last+1]

if '0' not in segment:
    print("YES")
else:
    print("NO")