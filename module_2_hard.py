def generate_password(n):
    password = ""
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))
    for pair in pairs:
        pair_sum = sum(pair)
        if n % pair_sum == 0:
            password += f"{pair[0]}{pair[1]}"
    return password
for i in range(3, 21):
    result = generate_password(i)
    print(f"{i} - {result}")