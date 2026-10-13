a, b, c = map(int, input().split())

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print(largest)
