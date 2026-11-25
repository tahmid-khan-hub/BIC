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
        prob = 1
        kmer = text[i:i+k]
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

best_motifs = []
for text in dna:
    best_motifs.append(text[:k])

for start in range(len(dna[0])-k+1):
    motifs = [dna[0][start :start +k]]
    for i in range(1, t):
        profile = get_profile(motifs)
        motifs.append(most_probable(dna[i], profile))
    if score(motifs) < score(best_motifs):
        best_motifs = motifs

for i in best_motifs:
    print(i)