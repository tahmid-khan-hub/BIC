
def hamming_distance(pattern, window):
    diff = 0
    for i in range(len(pattern)):
        if pattern[i] != window[i]:
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

def frequent_words_mismatches(text, k, d):
    counts = {}

    for pattern in all_kmers(k):
        count = 0
        for i in range(len(text)-k+1):
            window = text[i:i+k]
            if hamming_distance(pattern, window) <= d:
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

print(*frequent_words_mismatches(text, k, d))