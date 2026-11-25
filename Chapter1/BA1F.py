genome = input().strip()
skew = 0
min_skew = 0
positions = [0]

for i in range(len(genome)):
    if genome[i] == 'G':
        skew += 1
    elif genome[i] == 'C':
        skew -= 1

    if skew < min_skew:
        min_skew = skew
        positions = [i+1]
    elif skew == min_skew:
        positions.append(i+1)

print(*positions)