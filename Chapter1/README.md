# Chapter 1: Where in the Genome Does DNA Replication Begin?

Solutions to Rosalind Bioinformatics Textbook Track problems, written in Python.

Input is read from the keyboard with `input()`. For problems with an unknown number of lines, press Enter on an empty line to finish the input.

## Problems

- [BA1A: Compute the Number of Times a Pattern Appears in a Text](#ba1a-compute-the-number-of-times-a-pattern-appears-in-a-text)
- [BA1B: Find the Most Frequent Words in a String](#ba1b-find-the-most-frequent-words-in-a-string)
- [BA1C: Find the Reverse Complement of a String](#ba1c-find-the-reverse-complement-of-a-string)
- [BA1D: Find All Occurrences of a Pattern in a String](#ba1d-find-all-occurrences-of-a-pattern-in-a-string)
- [BA1E: Find Patterns Forming Clumps in a String](#ba1e-find-patterns-forming-clumps-in-a-string)
- [BA1F: Find a Position in a Genome Minimizing the Skew](#ba1f-find-a-position-in-a-genome-minimizing-the-skew)
- [BA1G: Compute the Hamming Distance Between Two Strings](#ba1g-compute-the-hamming-distance-between-two-strings)
- [BA1H: Find All Approximate Occurrences of a Pattern in a String](#ba1h-find-all-approximate-occurrences-of-a-pattern-in-a-string)
- [BA1I: Find the Most Frequent Words with Mismatches in a String](#ba1i-find-the-most-frequent-words-with-mismatches-in-a-string)
- [BA1J: Find Frequent Words with Mismatches and Reverse Complements](#ba1j-find-frequent-words-with-mismatches-and-reverse-complements)
- [BA1K: Generate the Frequency Array of a String](#ba1k-generate-the-frequency-array-of-a-string)
- [BA1L: Implement PatternToNumber](#ba1l-implement-patterntonumber)
- [BA1M: Implement NumberToPattern](#ba1m-implement-numbertopattern)
- [BA1N: Generate the d-Neighborhood of a String](#ba1n-generate-the-d-neighborhood-of-a-string)

---

## BA1A: Compute the Number of Times a Pattern Appears in a Text

### Problem statement

Given a DNA string Text and a string Pattern, count how many times Pattern appears in Text. Overlapping appearances are counted too.

### Input and output

**Sample input:**

```
GCGCG
GCG
```

**Sample output:**

```
2
```

### Solution code

```python
def pattern_count(text, pattern):
    k = len(pattern)
    count = 0
    for i in range(len(text)-k+1):
        if pattern == text[i:i+k]:
            count += 1
    return count

text = input().strip()
pattern = input().strip()
print(pattern_count(text, pattern))
```

---

## BA1B: Find the Most Frequent Words in a String

### Problem statement

Given a DNA string Text and an integer k, find all k-mers that appear the most times in Text.

### Input and output

**Sample input:**

```
ACGTTGCATGTCGCATGATGCATGAGAGCT
4
```

**Sample output:**

```
CATG GCAT
```

> The k-mers can be printed in any order.

### Solution code

```python
def frequent_words(text, k):
    counts = {}
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        if kmer in counts:
            counts[kmer] += 1
        else:
            counts[kmer] = 1

    max_counts = 0
    for i in counts:
        if counts[i] > max_counts:
            max_counts = counts[i]

    result = []
    for i in counts:
        if counts[i] == max_counts:
            result.append(i)

    return result

text = input().strip()
k = int(input())
answer = frequent_words(text, k)
print(*answer)
```

---

## BA1C: Find the Reverse Complement of a String

### Problem statement

Given a DNA string Pattern, return its reverse complement: replace each nucleotide with its complement (A with T, T with A, C with G, G with C), then reverse the whole string.

### Input and output

**Sample input:**

```
AAAACCCGGT
```

**Sample output:**

```
ACCGGGTTTT
```

### Solution code

```python
pattern = input().strip()
complements = ""

for i in pattern:
    if i == 'A':
        complements += 'T'
    elif i == 'T':
        complements += 'A'
    elif i == 'G':
        complements += 'C'
    else:
        complements += 'G'

result = ""
for i in complements:
    result = i + result

print(result)
```

---

## BA1D: Find All Occurrences of a Pattern in a String

### Problem statement

Given two strings Pattern and Genome, find every starting position where Pattern appears in Genome. Positions start from 0.

### Input and output

**Sample input:**

```
ATAT
GATATATGCATATACTT
```

**Sample output:**

```
1 3 9
```

### Solution code

```python
pattern = input().strip()
genome = input().strip()

positions = []
for i in range(len(genome)-len(pattern)+1):
    window = genome[i:i+len(pattern)]
    if pattern == window:
        positions.append(i)

print(*positions)
```

---

## BA1E: Find Patterns Forming Clumps in a String

### Problem statement

Given a string Genome and integers k, L and t, find all distinct k-mers that appear at least t times inside some window of length L in Genome. Such k-mers form an (L, t)-clump.

### Input and output

**Sample input:**

```
CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA
5 50 4
```

**Sample output:**

```
CGACA GAAGA
```

> The k-mers can be printed in any order.

### Solution code

```python
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
```

---

## BA1F: Find a Position in a Genome Minimizing the Skew

### Problem statement

The skew at position i is (number of G) minus (number of C) in the first i nucleotides of Genome. Find all positions i where the skew is at its minimum.

### Input and output

**Sample input:**

```
TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT
```

**Sample output:**

```
11 24
```

### Solution code

```python
genome = input().strip()
skew = 0
min_skew = 0
positions = [0]

for i in range(len(genome)):
    if genome[i] == 'G':
        skew += 1
    elif genome[i] == 'C':
        skew -= 1

    if skew < min_skew:
        min_skew = skew
        positions = [i+1]
    elif skew == min_skew:
        positions.append(i+1)

print(*positions)
```

---

## BA1G: Compute the Hamming Distance Between Two Strings

### Problem statement

Given two DNA strings of equal length, count the number of positions where they have different letters (the Hamming distance).

### Input and output

**Sample input:**

```
GGGCCGTTGGT
GGACCGTTGAC
```

**Sample output:**

```
3
```

### Solution code

```python
def hamming_distance(dna1, dna2):
    d = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            d += 1

    return d

dna1 = input().strip()
dna2 = input().strip()
distance = hamming_distance(dna1, dna2)
print(distance)
```

---

## BA1H: Find All Approximate Occurrences of a Pattern in a String

### Problem statement

Given strings Pattern and Text and an integer d, find all starting positions where Pattern appears in Text with at most d mismatches. Positions start from 0.

### Input and output

**Sample input:**

```
ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
3
```

**Sample output:**

```
6 7 26 27
```

### Solution code

```python
def hamming_distance(pattern, window):
    diff = 0
    for i in range(len(pattern)):
        if pattern[i] != window[i]:
            diff += 1

    return diff

def approximate_occurrences(text, pattern, d):
    positions = []
    for i in range(len(text)-len(pattern)+1):
        window = text[i:i+len(pattern)]

        l = hamming_distance(pattern, window)

        if l <= d:
            positions.append(i)

    print(*positions)

pattern = input().strip()
text = input().strip()
d = int(input())

approximate_occurrences(text, pattern, d)
```

---

## BA1I: Find the Most Frequent Words with Mismatches in a String

### Problem statement

Given a string Text and integers k and d, find all k-mers that appear the most times in Text when up to d mismatches are allowed. The answer k-mer does not need to appear exactly in Text.

### Input and output

**Sample input:**

```
ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1
```

**Sample output:**

```
GATG ATGC ATGT
```

> The k-mers can be printed in any order.

### Solution code

```python

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
```

---

## BA1J: Find Frequent Words with Mismatches and Reverse Complements

### Problem statement

Same as BA1I, but an appearance of the k-mer's reverse complement (with up to d mismatches) also counts. Find all k-mers that maximize this total count.

### Input and output

**Sample input:**

```
ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1
```

**Sample output:**

```
ATGT ACAT
```

> The k-mers can be printed in any order.

### Solution code

```python

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
```

---

## BA1K: Generate the Frequency Array of a String

### Problem statement

Given a DNA string Text and an integer k, return the frequency array: a list of 4^k numbers where the i-th number is how many times the i-th k-mer (in lexicographic order) appears in Text.

### Input and output

**Sample input:**

```
ACGCGGCTCTGAAA
2
```

**Sample output:**

```
2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0
```

### Solution code

```python
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
```

---

## BA1L: Implement PatternToNumber

### Problem statement

Convert a DNA string to a number by treating it as a base-4 number, where A = 0, C = 1, G = 2 and T = 3.

### Input and output

**Sample input:**

```
AGT
```

**Sample output:**

```
11
```

### Solution code

```python
dna = input().strip()

value = {"A": 0, "C": 1, "G": 2, "T": 3}

answer = 0
for i in dna:
    answer = answer*4 + value[i]
print(answer)
```

---

## BA1M: Implement NumberToPattern

### Problem statement

Given integers index and k, convert index back into its k-letter DNA string (the reverse of PatternToNumber).

### Input and output

**Sample input:**

```
45
4
```

**Sample output:**

```
AGTC
```

### Solution code

```python
index = int(input())
k = int(input())

letter = ["A", "C", "G", "T"]

result = ""
for _ in range(k):
    remainder = index%4
    result = letter[remainder] + result 
    index = index // 4
print(result)
```

---

## BA1N: Generate the d-Neighborhood of a String

### Problem statement

Given a DNA string Pattern and an integer d, find all k-mers whose Hamming distance from Pattern is at most d.

### Input and output

**Sample input:**

```
ACG
1
```

**Sample output:**

```
CCG
TCG
GCG
AAG
ATG
AGG
ACA
ACC
ACT
ACG
```

> The strings can be printed in any order. This code prints them in lexicographic order.

### Solution code

```python
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
```