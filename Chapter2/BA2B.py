k = int(input())
dna = []

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    dna.append(line)

kmers = [""]
for _ in range(k):
    new = []
    for i in kmers:
        for base in "ACGT":
            new.append(i+base)
    kmers = new

best_pattern = ""
best_total = 10**9

for p in kmers:
    total = 0
    for text in dna:
        smallest = k
        for i in range(len(text)-k+1):
            diff = 0
            for j in range(k):
                if p[j] != text[i+j]:
                    diff += 1
            if diff < smallest:
                smallest = diff
        total += smallest

    if total < best_total:
        best_total = total
        best_pattern = p
print(best_pattern)