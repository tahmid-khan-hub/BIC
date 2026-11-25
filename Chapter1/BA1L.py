dna = input().strip()

value = {"A": 0, "C": 1, "G": 2, "T": 3}

answer = 0
for i in dna:
    answer = answer*4 + value[i]
print(answer)