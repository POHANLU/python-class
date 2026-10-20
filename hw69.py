n = int(input())
result = 0

while n > 0:
    digit = n % 10
    result = result * 10 + digit
    n //= 10

print(result)
