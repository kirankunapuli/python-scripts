lines = []
for i in range(1, 9):
    lines.append([str(2 ** j) for j in range(i)])

b = len(lines[-1])
buffers = [len(x) for x in lines[-1]]

for line in lines:
    l = len(line)
    line = [" "] * (b - len(line)) + line
    out = []
    for x, y in zip(line, buffers):
        out.append(x.rjust(y))
    print(" ".join(out + out[::-1][1:]))
