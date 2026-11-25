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