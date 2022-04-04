import sys

argc = len(sys.argv) - 1
argv = sys.argv[1:]

if argc < 2:
    print("Usage:   detection.py [CODES...]")
    print("Example: detection.py 01010100 01001011 10110111 10101000")
    print("Error:   At least two codes are required.")
    exit(1)

a = argv
result = []

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        temp = 0
        for k in range(len(a[i])):
            if a[i][k] != a[j][k]:
                temp += 1
        result.append(temp)

d = len(a[0])

for x in result:
    if x < d:
        d = x

print("d(V) =", d)
