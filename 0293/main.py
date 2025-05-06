text = input()
print(len(text))
for letter in text:
    print(bin(ord(letter))[2:])