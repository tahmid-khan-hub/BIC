text = input().strip()
k = int(input())

kmers = [""]
for _ in range(k):
    new = []
    for i in kmers:
        for base in "ACGT":
            new.append(i+base)
    kmers = new

counts = {}
for i in kmers:
    counts[i] = 0

for i in range(len(text)-k+1):
    window = text[i:i+k]
    counts[window] += 1

result = []
for i in kmers:
    result.append(str(counts[i]))

print(*result)