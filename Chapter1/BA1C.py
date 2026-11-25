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
    result = i + complements

print(result)