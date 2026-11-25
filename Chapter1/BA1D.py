pattern = input().strip()
genome = input().strip()

positions = []
for i in range(len(genome)-len(pattern)+1):
    window = genome[i:i+len(pattern)]
    if pattern == window:
        positions.append(i)

print(*positions)