import random

k, t = map(int, input().split())
dna = []
for _ in range(t):
    dna.append(input().strip())

def get_profile(motifs):
    profile = []
    for i in range(k):
        col = {"A": 1, "C": 1, "G": 1, "T": 1}
        for motif in motifs:
            col[motif[i]] += 1
        profile.append(col)
    return profile

def most_probable(text, profile):
    best_kmer = text[:k]
    best_prob = -1
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        prob = 1
        for j in range(k):
            prob = prob * profile[j][kmer[j]]
        if prob > best_prob:
            best_prob = prob
            best_kmer = kmer
    return best_kmer

def score(motifs):
    total = 0
    for i in range(k):
        col = {"A": 0, "C": 0, "G": 0, "T": 0}
        for motif in motifs:
            col[motif[i]] += 1
        total += len(motifs) - max(col.values())
    return total

def one_run():
    motifs = []
    for text in dna:
        start = random.randint(0, len(text)-k)
        motifs.append(text[start:start+k])

    best = motifs

    while True:
        profile = get_profile(motifs)
        motifs = []

        for text in dna:
            motifs.append(most_probable(text, profile))

        if score(motifs) < score(best):
            best = motifs
        else:
            return best

overall_best = one_run()
for _ in range(999):
    result = one_run()
    if score(result) < score(overall_best):
        overall_best = result

for i in overall_best:
    print(i)