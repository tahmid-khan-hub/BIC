index = int(input())
k = int(input())

letter = ["A", "C", "G", "T"]

result = ""
for _ in range(k):
    remainder = index%4
    result = letter[remainder] + result 
    index = index // 4
print(result)