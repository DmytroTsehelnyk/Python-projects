s = "4445664456"

f = ''.join('0' if n < '5' else '2' for n in s)

print(f)