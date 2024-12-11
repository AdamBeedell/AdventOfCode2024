### 10.py

themap = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

#with open("input.txt", "r") as file:
#    input = file.read().strip()


### today we're doing a grid based search process

## have not done searches before

### goal is to find there 0's (trailheads), then walk in valid increments of 1 (0->1->2...) towards 9's. each 9 is one point, sum the points

#parse input
themap = themap.splitlines()

#find trailheads
trailheads = []

for y, line in enumerate(themap):
    for x, spot in enumerate(line):
        if spot == "0":
            trailheads.append([y,x])

def is_within_bounds(y, x, themap):
    return 0 <= y < len(themap) and 0 <= x < len(themap[0])

def checkincrementing(y,x, y2,x2, themap):
    if is_within_bounds(y,x,themap) and is_within_bounds(y2,x2,themap):
        if (int(themap[y2][x2]) - int(themap[y][x])) == 1:
            return True
        else: 
            return False
    else:
        return False

directions = [
    [0,-1], ## left
    [1,0], ## down
    [-1,0], ## up
    [0,1], ## right
    ] ## no diagonals


#y = trailheads[0][0]
#x = trailheads[0][1]

trails = set()
searched = set()


for trailhead in trailheads:
    y=trailhead[0]
    x=trailhead[1]
    for direction in directions:
        y2 = y+direction[0]
        x2 = x+direction[1]
        if checkincrementing(y,x, y2,x2, themap):
            trails.add(((y,x), (y2,x2)))
    searched.add((y,x))
#for looptrail in looptrails



### got to around here and had some thoughts about structure and whatnot. I think the problem is trying to teach me to do depth or breadth first search or something like that.

### if i continue the way i've started I end up with a long list of connections. A connectome perhaps. 
### I think it would be possible to approach this problem by going through the connectome and concat/listing together the connections.
### looping shouldnt be possible because i've set it to only hold connections as valid if the values increment which is nice
### the list could be purged of anything with length less than 8, and then counted where the trailhead is the same
### This is a sqley kinda solution and doesnt really search at all. i think it works though.





### post break

### this finds all the connections in the map which we may care about
tosearch = set()

while True:
    tosearch = {trail[1] for trail in trails if trail[1] not in searched} ### took a steer here, but one asked for in explicit terms

    if len(tosearch) == 0:
        break

    for coords in tosearch:
        y=coords[0]
        x=coords[1]
        for direction in directions:
            y2 = y+direction[0]
            x2 = x+direction[1]
            if checkincrementing(y,x, y2,x2, themap):
                trails.add(((y,x), (y2,x2)))
        searched.add((y,x))



### this needs to knit them up right pair to left pair

connected = set()
toconnect = set()
leftstuff = set()

##incomplete
while True:
    toconnect = {trail[0] for trail in trails if trail[1] == trails[0]}
    if len(tosearch) == 0:
        break
##/incomplete

## get a right touple
for connection in trails:
    y=connection[0][0]
    x=connection[0][1]
    y2=connection[1][0]
    x2=connection[0][1]
    leftstuff.add(y,x)
    

working = []
trails2={}
for (left, right) in trails:
    trails2.setdefault(left, set()).add(right)
    connections = trails2.get(left, set())
#    for (left2, right2) in trails:
#        if right == left2:
#            working.append(((left,right), (left2, right2)))





### Failed

### next time need to just find BFS/DFS code