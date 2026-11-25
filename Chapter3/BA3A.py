k = int(input())
text = input().strip()

result = []
for i in range(len(text)-k+1):
    window = text[i:i+k]
    result.append(window)

result.sort()

for i in result:
    print(i)