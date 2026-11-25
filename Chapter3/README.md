# Chapter 3: How Do We Assemble Genomes?

Solutions to Rosalind Bioinformatics Textbook Track problems, written in Python.

Input is read from the keyboard with `input()`. For problems with an unknown number of lines, press Enter on an empty line to finish the input.

## Problems

- [BA3A: Generate the k-mer Composition of a String](#ba3a-generate-the-k-mer-composition-of-a-string)
- [BA3B: Reconstruct a String from its Genome Path](#ba3b-reconstruct-a-string-from-its-genome-path)
- [BA3C: Construct the Overlap Graph of a Collection of k-mers](#ba3c-construct-the-overlap-graph-of-a-collection-of-k-mers)
- [BA3D: Construct the De Bruijn Graph of a String](#ba3d-construct-the-de-bruijn-graph-of-a-string)
- [BA3E: Construct the De Bruijn Graph of a Collection of k-mers](#ba3e-construct-the-de-bruijn-graph-of-a-collection-of-k-mers)
- [BA3F: Find an Eulerian Cycle in a Graph](#ba3f-find-an-eulerian-cycle-in-a-graph)
- [BA3G: Find an Eulerian Path in a Graph](#ba3g-find-an-eulerian-path-in-a-graph)
- [BA3H: Reconstruct a String from its k-mer Composition](#ba3h-reconstruct-a-string-from-its-k-mer-composition)

---

## BA3A: Generate the k-mer Composition of a String

### Problem statement

Given an integer k and a string Text, return all k-mers of Text (repeats included).

### Input and output

**Sample input:**

```
5
CAATCCAAC
```

**Sample output:**

```
AATCC
ATCCA
CAATC
CCAAC
TCCAA
```

> The k-mers can be printed in any order. This code sorts them.

### Solution code

```python
k = int(input())
text = input().strip()

result = []
for i in range(len(text)-k+1):
    window = text[i:i+k]
    result.append(window)

result.sort()

for i in result:
    print(i)
```

---

## BA3B: Reconstruct a String from its Genome Path

### Problem statement

Given a sequence of k-mers where each k-mer overlaps the next one by k - 1 letters, return the string they spell. Take the first k-mer in full, then add the last letter of each next k-mer.

### Input and output

**Sample input:**

```
ACCGA
CCGAA
CGAAG
GAAGC
AAGCT
```

**Sample output:**

```
ACCGAAGCT
```

### Solution code

```python
kmers = []

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    kmers.append(line)

text = kmers[0]
for i in range(1, len(kmers)):
    kmer = kmers[i]
    last_char = kmer[len(kmer)-1]
    text = text + last_char

print(text)
```

---

## BA3C: Construct the Overlap Graph of a Collection of k-mers

### Problem statement

Given a collection of k-mers, build the overlap graph: draw an edge from k-mer a to k-mer b when the suffix of a (all but the first letter) equals the prefix of b (all but the last letter). Return it as an adjacency list.

### Input and output

**Sample input:**

```
ATGCG
GCATG
CATGC
AGGCA
GGCAT
```

**Sample output:**

```
AGGCA -> GGCAT
CATGC -> ATGCG
GCATG -> CATGC
GGCAT -> GCATG
```

> The edges can be printed in any order.

### Solution code

```python
kmers = []

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    kmers.append(line)

kmers.sort()

for i in range(len(kmers)):
    for j in range(len(kmers)):
        if i != j:
            a = kmers[i]
            b = kmers[j]
            suffix = a[1:]
            prefix = b[:len(b)-1]
            if suffix == prefix:
                print(a + " -> " + b)
```

---

## BA3D: Construct the De Bruijn Graph of a String

### Problem statement

Given an integer k and a string Text, build the De Bruijn graph: every k-mer in Text gives an edge from its prefix to its suffix (both of length k - 1). Nodes with the same label are glued into one node. Return it as an adjacency list.

### Input and output

**Sample input:**

```
4
AAGATTCTCTAC
```

**Sample output:**

```
AAG -> AGA
AGA -> GAT
ATT -> TTC
CTA -> TAC
CTC -> TCT
GAT -> ATT
TCT -> CTA,CTC
TTC -> TCT
```

### Solution code

```python
k = int(input())
text = input().strip()

graph = {}
for i in range(len(text)-k+1):
    window = text[i:i+k]
    prefix = window[:k-1]
    sufix = window[1:]
    if prefix in graph:
        graph[prefix].append(sufix)
    else:
        graph[prefix] = [sufix]

keys = list(graph.keys())
keys.sort()

for node in keys:
    nexts = graph[node]
    nexts.sort()
    print(node + " -> " + ",".join(nexts))
```

---

## BA3E: Construct the De Bruijn Graph of a Collection of k-mers

### Problem statement

Given a collection of k-mers (repeats allowed), build the De Bruijn graph: every k-mer gives an edge from its prefix to its suffix, and nodes with the same label are glued together. Return it as an adjacency list.

### Input and output

**Sample input:**

```
GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG
```

**Sample output:**

```
AGG -> GGG
CAG -> AGG,AGG
GAG -> AGG
GGA -> GAG
GGG -> GGA,GGG
```

### Solution code

```python
kmers = []

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    kmers.append(line)

kmers.sort()

graph = {}
for i in kmers:
    prefix = i[:len(i)-1]
    sufix = i[1:]
    if prefix in graph:
        graph[prefix].append(sufix)
    else:
        graph[prefix] = [sufix]

keys = list(graph.keys())
keys.sort()

for node in keys:
    nexts = graph[node]
    nexts.sort()
    print(node + " -> " + ",".join(nexts))
```

---

## BA3F: Find an Eulerian Cycle in a Graph

### Problem statement

Given an Eulerian directed graph as an adjacency list, find an Eulerian cycle: a cycle that uses every edge exactly once and returns to its starting node.

### Input and output

**Sample input:**

```
0 -> 3
1 -> 0
2 -> 1,6
3 -> 2
4 -> 2
5 -> 4
6 -> 5,8
7 -> 9
8 -> 7
9 -> 6
```

**Sample output:**

```
6->8->7->9->6->5->4->2->1->0->3->2->6
```

> Any valid Eulerian cycle is accepted. This code prints `0->3->2->6->8->7->9->6->5->4->2->1->0`, which is also correct.

### Solution code

```python
graph = {}
start = ""

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    parts = line.split(" -> ")
    node = parts[0]
    nexts = parts[1].split(",")
    graph[node] = nexts
    if start == "":
        start = node

stack = [start]
path = []

while len(stack) > 0:
    node = stack[len(stack)-1]
    if node in graph and len(graph[node]) > 0:
        next_node = graph[node].pop(0)
        stack.append(next_node)
    else:
        path.append(stack.pop())

path.reverse()
print("->".join(path))
```

---

## BA3G: Find an Eulerian Path in a Graph

### Problem statement

Given a directed graph that has an Eulerian path, find a path that uses every edge exactly once. The path starts at the node with one more outgoing edge than incoming edges.

### Input and output

**Sample input:**

```
0 -> 2
1 -> 3
2 -> 1
3 -> 0,4
6 -> 3,7
7 -> 8
8 -> 9
9 -> 6
```

**Sample output:**

```
6->7->8->9->6->3->0->2->1->3->4
```

### Solution code

```python
graph = {}
out_count = {}
in_count = {}

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    parts = line.split(" -> ")
    node = parts[0]
    nexts = parts[1].split(",")
    graph[node] = nexts

    out_count[node] = len(nexts)

    for n in nexts:
        if n in in_count:
            in_count[n] += 1
        else:
            in_count[n] = 1

start = ""
for node in out_count:
    incoming = 0
    if node in in_count:
        incoming = in_count[node]
    if out_count[node] - incoming == 1:
        start = node

stack = [start]
path = []

while len(stack) > 0:
    node = stack[len(stack)-1]
    if node in graph and len(graph[node]) > 0:
        next_node = graph[node].pop(0)
        stack.append(next_node)
    else:
        path.append(stack.pop())

path.reverse()
print("->".join(path))
```

---

## BA3H: Reconstruct a String from its k-mer Composition

### Problem statement

Given an integer k and a list of k-mers, return a string whose k-mer composition is exactly that list. Build the De Bruijn graph of the k-mers, find an Eulerian path in it, then spell the string from the path.

### Input and output

**Sample input:**

```
4
CTTA
ACCA
TACC
GGCT
GCTT
TTAC
```

**Sample output:**

```
GGCTTACCA
```

> If more than one string is possible, any one is accepted.

### Solution code

```python
k = int(input())
kmers = []

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    kmers.append(line)

graph = {}
out_count = {}
in_count = {}

for i in kmers:
    prefix = i[:k-1]
    suffix = i[1:]

    if prefix in graph:
        graph[prefix].append(suffix)
    else:
        graph[prefix] = [suffix]

    if prefix in out_count:
        out_count[prefix] += 1
    else:
        out_count[prefix] = 1

    if suffix in in_count:
        in_count[suffix] += 1
    else:
        in_count[suffix] = 1

start = kmers[0][:k-1]
for node in out_count:
    incoming = 0
    if node in in_count:
        incoming = in_count[node]
    if out_count[node] - incoming == 1:
        start = node

stack = [start]
path = []

while len(stack) > 0:
    node = stack[len(stack)-1]
    if node in graph and len(graph[node]) > 0:
        next_node = graph[node].pop(0)
        stack.append(next_node)
    else:
        path.append(stack.pop())

path.reverse()

text = path[0]
for i in range(1, len(path)):
    node = path[i]
    text = text + node[len(node)-1]

print(text)
```