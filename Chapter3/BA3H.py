k = int(input())
kmers = []

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    kmers.append(line)

graph = {}
out_count = {}
in_count = {}

for i in kmers:
    prefix = i[:k-1]
    suffix = i[1:]

    if prefix in graph:
        graph[prefix].append(suffix)
    else:
        graph[prefix] = [suffix]

    if prefix in out_count:
        out_count[prefix] += 1
    else:
        out_count[prefix] = 1

    if suffix in in_count:
        in_count[suffix] += 1
    else:
        in_count[suffix] = 1

start = kmers[0][:k-1]
for node in out_count:
    incoming = 0
    if node in in_count:
        incoming = in_count[node]
    if out_count[node] - incoming == 1:
        start = node

stack = [start]
path = []

while len(stack) > 0:
    node = stack[len(stack)-1]
    if node in graph and len(graph[node]) > 0:
        next_node = graph[node].pop(0)
        stack.append(next_node)
    else:
        path.append(stack.pop())

path.reverse()

text = path[0]
for i in range(1, len(path)):
    node = path[i]
    text = text + node[len(node)-1]

print(text)