pattern = input().strip()
d = int(input())

def hamming_distance(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff

kmers = [""]
for _ in range(len(pattern)):
    new = []
    for i in kmers:
        for base in "ACGT":
            new.append(i+base)
    kmers = new

result = []
for i in kmers:
    if hamming_distance(pattern, i) <= d:
        result.append(i)

for i in result:
    print(i)