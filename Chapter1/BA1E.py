genome = input().strip()
k, L, t = map(int, input().split())

pattern = []

for i in range(len(genome)-L+1):
    window = genome[i:i+L]
    freq = {}
    for j in range(L-k+1):
        kmer = window[j:j+k]
        if kmer in freq:
            freq[kmer] += 1
        else:
            freq[kmer] = 1

    for kmer in freq:
        if freq[kmer] >= t:
            pattern.append(kmer)

result = set(pattern)
print(*result)