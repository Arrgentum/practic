import sys

data = sys.stdin.buffer.read()
N = int(data.decode()[0])
data = data[1:]

L = len(data)
Z = sorted(data[i * L // N: (i + 1) * L // N] for i in range(N))

for z in Z:
    sys.stdout.buffer.write(z)