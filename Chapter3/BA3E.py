kmers = []

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    kmers.append(line)

kmers.sort()

graph = {}
for i in kmers:
    prefix = i[:len(i)-1]
    sufix = i[1:]
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