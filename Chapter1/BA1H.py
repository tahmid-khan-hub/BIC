
def hamming_distance(pattern, window):
    diff = 0
    for i in range(len(pattern)):
        if pattern[i] != window[i]:
            diff += 1

    return diff

def approximate_occurrences(text, pattern, d):
    positions = []
    for i in range(len(text)-len(pattern)+1):
        window = text[i:i+len(pattern)]
        
        l = hamming_distance(pattern, window)

        if l <= d:
            positions.append(i+1)

    print(*positions)

text = input().strip()
pattern = input().strip()
d = int(input())

approximate_occurrences(text, pattern, d)