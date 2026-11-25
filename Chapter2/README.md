# Chapter 2: Which DNA Patterns Play the Role of Molecular Clocks?

Solutions to Rosalind Bioinformatics Textbook Track problems, written in Python.

Input is read from the keyboard with `input()`. For problems with an unknown number of lines, press Enter on an empty line to finish the input.

## Problems

- [BA2B: Find a Median String](#ba2b-find-a-median-string)
- [BA2C: Find a Profile-most Probable k-mer in a String](#ba2c-find-a-profile-most-probable-k-mer-in-a-string)
- [BA2E: Implement GreedyMotifSearch with Pseudocounts](#ba2e-implement-greedymotifsearch-with-pseudocounts)
- [BA2F: Implement RandomizedMotifSearch](#ba2f-implement-randomizedmotifsearch)
- [BA2G: Implement GibbsSampler](#ba2g-implement-gibbssampler)

---

## BA2B: Find a Median String

### Problem statement

Given an integer k and a collection of DNA strings, find a k-mer Pattern that minimizes d(Pattern, Dna). For each string, d is the smallest Hamming distance between Pattern and any k-mer in that string; d(Pattern, Dna) is the sum over all strings.

### Input and output

**Sample input:**

```
3
AAATTGACGCAT
GACGACCACGTT
CGTCAGCGCCTG
GCTGAGCACCGG
AGTACGGGACAG
```

**Sample output:**

```
GAC
```

> If more than one k-mer ties, any of them is accepted. This code prints `ACG`, which has the same total distance (2) as `GAC`.

### Solution code

```python
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
```

---

## BA2C: Find a Profile-most Probable k-mer in a String

### Problem statement

Given a string Text, an integer k and a 4 x k profile matrix (rows A, C, G, T), find the k-mer in Text with the highest probability. The probability of a k-mer is the product of the profile values of its letters at each position. If there is a tie, use the first one in Text.

### Input and output

**Sample input:**

```
ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
5
0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2
```

**Sample output:**

```
CCGAG
```

### Solution code

```python
text = input().strip()
k = int(input())

profile = []
for _ in range(4):
    row = input().split()
    numbers = []
    for i in row:
        numbers.append(float(i))
    profile.append(numbers)

best_kmer = ""
best_prob = -1

for i in range(len(text)-k+1):
    prob = 1
    kmer = text[i:i+k]
    for j in range(k):
        letter = kmer[j]

        if letter == "A":
            row_number = 0
        elif letter == "C":
            row_number = 1
        elif letter == "G":
            row_number = 2
        else:
            row_number = 3

        prob = prob * profile[row_number][j]

    if prob > best_prob:
        best_prob = prob
        best_kmer = kmer

print(best_kmer)
```

---

## BA2E: Implement GreedyMotifSearch with Pseudocounts

### Problem statement

Given integers k and t and t DNA strings, run GreedyMotifSearch with pseudocounts and return the best motifs (one k-mer from each string). Start from each k-mer of the first string, then pick the profile-most probable k-mer in each next string. Pseudocounts mean every letter count starts at 1 instead of 0.

### Input and output

**Sample input:**

```
3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG
```

**Sample output:**

```
TTC
ATC
TTC
ATC
TTC
```

### Solution code

```python
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
```

---

## BA2F: Implement RandomizedMotifSearch

### Problem statement

Given integers k and t and t DNA strings, run RandomizedMotifSearch 1000 times (with pseudocounts) and return the best motifs. Each run starts from random k-mers, then keeps rebuilding the motifs from the profile until the score stops improving.

### Input and output

**Sample input:**

```
8 5
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA
```

**Sample output:**

```
TCTCGGGG
CCAAGGTG
TACAGGCG
TTCAGGTG
TCCACGTG
```

> This is a random algorithm, so the output can change between runs. Any set of motifs with the same best score (9 here) is correct.

### Solution code

```python
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
```

---

## BA2G: Implement GibbsSampler

### Problem statement

Given integers k, t and N and t DNA strings, run GibbsSampler with 20 random starts (with pseudocounts) and return the best motifs. In each of the N steps, one random motif is removed, a profile is built from the rest, and a new k-mer is chosen for that string at random, weighted by its probability.

### Input and output

**Sample input:**

```
8 5 100
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
TAGTACCGAGACCGAAAGAAGTATACAGGCGT
TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
AATCCACCAGCTCCACGTGCAATGTTGGCCTA
```

**Sample output:**

```
TCTCGGGG
CCAAGGTG
TACAGGCG
TTCAGGTG
TCCACGTG
```

> This is a random algorithm, so the output can change between runs. Any set of motifs with the same best score (9 here) is correct. If you get a worse score, run it again.

### Solution code

```python
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
```