a, b = map(int, input().split())
c, d = map(int, input().split())

det = a * d - b * c

r11 = d / det
r12 = -b / det
r21 = -c / det
r22 = a / det

print(f"{r11:.4f} {r12:.4f}")
print(f"{r21:.4f} {r22:.4f}")
