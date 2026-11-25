graph = {}
out_count = {}
in_count = {}

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    parts = line.split(" -> ")
    node = parts[0]
    nexts = parts[1].split(",")
    graph[node] = nexts

    out_count[node] = len(nexts)

    for n in nexts:
        if n in in_count:
            in_count[n] += 1
        else:
            in_count[n] = 1

start = ""
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
print("->".join(path))