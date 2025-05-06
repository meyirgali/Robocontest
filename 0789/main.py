n = int(input())
count_2 = 1 if n>= 2 else 0
count_5 = 1 if n>= 5 else 0
print(min(count_2, count_5))