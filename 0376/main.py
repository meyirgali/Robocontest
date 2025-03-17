month = int(input())
if month in [12, 1, 2]:
    result = "Winter"
elif month in [3, 4, 5]:
    result = "Spring"
elif month in [6, 7, 8]:
    result = "Summer"
elif month in [9, 10, 11]:
    result = "Autumn"
else:
    result = "Error"

print(result)