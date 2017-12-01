digits = map(int, list(open('input.txt').read().strip()))
n = len(digits)
total = 0

for i in range(len(digits)):
    total += digits[i] if digits[i] == digits[(i+1) % n] else 0

print total
