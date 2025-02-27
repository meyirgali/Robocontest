N=int(input())
a=len(str(N))
for i in range(a-1,-1,-1):
  b=(N//10**i)%10
  if i%3==1:
    c={
      1: "o'n ",
      2: "yigirma ",
      3: "o'ttiz ",
      4: "qirq ",
      5: "ellik ",
      6: "oltmish ",
      7: "yetmish ",
      8: "sakson ",
      9: "to'qson ",
      0: ""
     }
    print(c[b],end='')
  else:
    c={
      1: "bir ",
      2: "ikki ",
      3: "uch ",
      4: "to'rt ",
      5: "besh ",
      6: "olti ",
      7: "yetti ",
      8: "sakkiz ",
      9: "to'qqiz ",
      0: ""
    }
    print(c[b],end='')
  if b!=0 and i%3==2:
    print("yuz ",end='')
  if i==9:
    print("milliard ",end='')
  if i==6:
    print("million ",end='')
  if i==3:
    print("ming ",end='')