
s = input()
s = s.strip(" ").lower()

result = ""
in_space = False

for ch in s:
    if ch == " ":
        if not in_space:
            result += "_"
        in_space = True
    else:
        result += ch
        in_space = False

valid = 6 <= len(result) <= 16

for ch in result:
    if ch not in "abcdefghijklmnopqrstuvwxyz0123456789_":
        valid = False

print(result)
print("VALID" if valid else "INVALID")
