ones = { 1:" bir", 2:" ikki", 3:" uch", 4:" to'rt", 5:" besh", 6:" olti", 7:" yetti", 8:" sakkiz", 9:" to'qqiz"}
tens = {10:" o'n", 20:" yigirma", 30:" o'ttiz", 40:" qirq", 50:" ellik", 60:" oltmish", 70:" yetmish", 80:" sakson", 90:" to'qson"}
n = int(input())
if n == 1000:
    result = "bir ming"
else:
    result = ""
    if n >=100:
        result += ones[n // 100] +  " yuz"
        n %= 100
    if n in tens:
        result += tens[n]
    else:
        if n >=10:
            result += tens[n // 10*10]+ ""
            n%=10
        if n in ones:
            result += ones[n]
print(result.strip())