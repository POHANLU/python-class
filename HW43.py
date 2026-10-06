x1, x2, x3 = map(int, input().split())

mean = (x1 + x2 + x3) / 3

variance = ((x1 - mean) ** 2 +
            (x2 - mean) ** 2 +
            (x3 - mean) ** 2) / 3

print(f"{mean:.2f}")
print(f"{variance:.2f}")
