baho = int(input())

if baho < 38:
    natija = baho
else:
    keyingi_5lik = ((baho // 5) + 1) * 5
    if keyingi_5lik - baho < 3:
        natija = keyingi_5lik
    else:
        natija = baho

print(natija)