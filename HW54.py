h = int(input())

if h <= 2:
    fee = h * 30
elif h <= 5:
    fee = 60 + (h - 2) * 20
else:
    fee = 120 + (h - 5) * 10

print(fee)
