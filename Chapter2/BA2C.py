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