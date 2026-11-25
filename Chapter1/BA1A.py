def pattern_count(text, pattern):
    k = len(pattern)
    count = 0
    for i in range(len(text)-k+1):
        if pattern == text[i:i+k]:
            count += 1
    return count

text = input().strip()
pattern = input().strip()
print(pattern_count(text, pattern))