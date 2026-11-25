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