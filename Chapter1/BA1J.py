
def hamming_distance(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff

def all_kmers(k):
    kmers = [""]
    for _ in range(k):
        new = []
        for i in kmers:
            for base in "ACGT":
                new.append(i+base)
        kmers = new
    return kmers

def reverse_complement(pattern):
    complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
    result = ""
    for i in pattern:
        result = complements[i] + result
    return result

def frequent_words_mismatches_and_reverse_complements(text, k, d):
    counts = {}
    for pattern in all_kmers(k):
        rc = reverse_complement(pattern)
        count = 0
        for i in range(len(text)-k+1):
            window = text[i:i+k]
            if hamming_distance(pattern, window) <= d:
                count += 1
            if hamming_distance(rc, window) <= d:
                count += 1
        counts[pattern] = count
    m = max(counts.values())
    result = []
    for i in counts:
        if counts[i] == m:
            result.append(i)
    return result

text = input().strip()
k, d = map(int, input().split())

print(*frequent_words_mismatches_and_reverse_complements(text, k, d))