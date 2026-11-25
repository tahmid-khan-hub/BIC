k = int(input())
text = input().strip()

graph = {}
for i in range(len(text)-k+1):
    window = text[i:i+k]
    prefix = window[:k-1]
    sufix = window[1:]
    if prefix in graph:
        graph[prefix].append(sufix)
    else:
        graph[prefix] = [sufix]

keys = list(graph.keys())
keys.sort()

for node in keys:
    nexts = graph[node]
    nexts.sort()
    print(node + " -> " + ",".join(nexts))