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