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