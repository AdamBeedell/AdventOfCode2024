##18.py

## problem today involves writing a map from coords, then running a pathing search over the resultant map

## input

input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

input = input.splitlines()

### build map

testmap = []

for y in range(0,7):
    line = []
    for x in range(0,7):
        line.append(".")
    testmap.append(line)

len(testmap)
len(testmap[0])


actualmap = []

for y in range(0,70):
    line = []
    for x in range(0,70):
        line.append(".")
    actualmap.append(line)


len(actualmap)
len(actualmap[0])

### populate map

for i in input:
    x, y = i.split(',')
    testmap[int(y)][int(x)] = '#' 

### DFS

