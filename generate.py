from random import uniform
from PIL import Image
from numpy import array
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('iterations', type=int)
parser.add_argument('smoothness', type=float)
args = parser.parse_args()

iterations = args.iterations
smoothness = args.smoothness

height_map = [[uniform(0, 1), uniform(0, 1)],
              [uniform(0, 1), uniform(0, 1)]]

for _ in range(iterations):

    horizontal = []
    for y in range(len(height_map)):
        arr = []

        for x in range(len(height_map) - 1):
            bias = abs(height_map[x][y] - height_map[x + 1][y]) / smoothness
            arr.append((height_map[x][y] + height_map[x + 1][y]) / 2 + uniform(-bias, bias))

        horizontal.append(arr)

    vertical = []
    for x in range(len(height_map)):
        arr = []

        for y in range(len(height_map) - 1):
            bias = abs(height_map[x][y] - height_map[x][y + 1]) / smoothness
            arr.append((height_map[x][y] + height_map[x][y + 1]) / 2 + uniform(-bias, bias))

        vertical.append(arr)

    middle = []
    for x in range(len(height_map) - 1):
        arr = []
        for y in range(len(height_map) - 1):
            bias = (abs(height_map[x][y] - height_map[x + 1][y + 1])
                    + abs(height_map[x + 1][y] - height_map[x][y + 1])) / (2 * smoothness)
            arr.append((height_map[x][y] + height_map[x + 1][y + 1] + height_map[x + 1][y] + height_map[x][y + 1]) / 4
                       + uniform(-bias, bias))
        middle.append(arr)

    new_height_map = []
    for line in range(len(height_map) + len(horizontal[0])):
        if line % 2 == 0:
            arr = []
            for index in range(len(height_map) + len(horizontal[0])):
                if index % 2 == 0:
                    arr.append(height_map[index // 2][line // 2])
                else:
                    arr.append(horizontal[line // 2][index // 2])
            new_height_map.append(arr)
        else:
            arr = []
            for index in range(len(height_map) + len(horizontal[0])):
                if index % 2 == 0:
                    arr.append(vertical[index // 2][line // 2])
                else:
                    arr.append(middle[index // 2][line // 2])
            new_height_map.append(arr)
    height_map = new_height_map

mx = max(max(e) for e in height_map)
mn = min(min(e) for e in height_map)

height_map = [[int(((e - mn) / (mx - mn)) * 255) for e in row] for row in height_map]

for x in range(len(height_map)):
    for y in range(len(height_map)):
        if height_map[x][y] <= 127:
            height = height_map[x][y] / (127 * 2)
            height_map[x][y] = (112 * height,
                                146 * height,
                                190 * height)
        else:
            height = height_map[x][y] / (255 * 2)
            height_map[x][y] = (160 * ((height + 0.75) ** 1.7 - 0.75),
                                160 * ((height + 0.75) ** 1.7 - 0.75),
                                60 * ((height + 0.75) ** 2 - 0.75))

im = Image.fromarray(array(height_map).astype('uint8')).convert('RGB')
im.save('generated.png', 'PNG')
