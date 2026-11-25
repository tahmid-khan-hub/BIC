import random

k, t, N = map(int, input().split())
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

def score(motifs):
    total = 0
    for i in range(k):
        col = {"A": 0, "C": 0, "G": 0, "T": 0}
        for motif in motifs:
            col[motif[i]] += 1
        total += len(motifs) - max(col.values())
    return total

def random_kmer(text, profile):
    kmers = []
    probs = []
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        prob = 1
        for j in range(k):
            prob = prob * profile[j][kmer[j]]
        kmers.append(kmer)
        probs.append(prob)

    roll = random.random() * sum(probs)
    running = 0
    for i in range(len(kmers)):
        running += probs[i]
        if roll < running:
            return kmers[i]
    return kmers[len(kmers)-1]

def one_start():
    motifs = []
    for text in dna:
        start = random.randint(0, len(text)-k)
        motifs.append(text[start:start+k])

    best = motifs[:]

    for _ in range(N):
        i = random.randint(0, t-1)

        others = []
        for j in range(t):
            if j != i:
                others.append(motifs[j])

        profile = get_profile(others)
        motifs[i] = random_kmer(dna[i], profile)

        if score(motifs) < score(best):
            best = motifs[:]

    return best

overall_best = one_start()
for _ in range(19):
    result = one_start()
    if score(result) < score(overall_best):
        overall_best = result

for i in overall_best:
    print(i)