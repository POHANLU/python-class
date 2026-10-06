n = int(input())

hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10

total = hundreds + tens + ones
product = hundreds * tens * ones
reverse = ones * 100 + tens * 10 + hundreds

print(hundreds, tens, ones)
print(total)
print(product)
print(reverse)