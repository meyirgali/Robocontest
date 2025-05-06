s = input()
prefixes = set()
for i in range(len(s)):
    prefix = s[i:+1]
    prefixes.add(prefix)

print(len(prefixes))
    