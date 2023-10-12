import sys


files = [1, 2, 4, 5, 6]

for num in files:
    with open(f"files/figure{num}.txt", 'r') as file:
        data = file.readlines()

    data = [(line.strip()) for line in data]
    max_size_mm = int(data[0])
    data = data[2:]
    data = [list(map(int, line.strip().split())) for line in data[2:]]

    min_w = sys.maxsize
    max_w = -sys.maxsize - 1

    for line in range(len(data)):

        if 1 in data[line]:
            for j in range(len(data[0])):
                if data[line][j] == 1:
                    if min_w > j:
                        min_w = j
                    break
                
            for k in range(len(data[0])-1, -1, -1):
                if data[line][k] == 1:
                    if max_w < k:
                        max_w = k
                    break

    if min_w == sys.maxsize or max_w == -sys.maxsize - 1:
        nominal_size = 0
    else:
        width_px = max_w - min_w + 1
        nominal_size = max_size_mm/width_px

    print(f"figure{num}: {nominal_size}")

