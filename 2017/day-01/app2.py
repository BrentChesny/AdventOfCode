digits = map(int, list(open('input.txt').read().strip()))
n = len(digits)
total = 0

for i in range(len(digits)):
    total += digits[i] if digits[i] == digits[(i + (n/2)) % n] else 0

print total
