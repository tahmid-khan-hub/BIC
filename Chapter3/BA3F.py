graph = {}
start = ""

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
    if start == "":
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