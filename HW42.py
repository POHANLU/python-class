s = int(input())

hours = s // 3600
remaining = s % 3600

minutes = remaining // 60
seconds = remaining % 60

print(hours, minutes, seconds)
