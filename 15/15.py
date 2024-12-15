#15.py


## robots in a warehouse

### Rodent's revenge!

###

themap = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########"""

themap = [list(row) for row in themap.splitlines()]

input = """<^^>>>vv<v>>v<<"""

## recycle code for robot position lookup

def findbot(themap):
    for y, line in enumerate(themap):
        for x, spot in enumerate(line):
            if spot == '@':
                coords = [y,x] ### I want to pass in/out what the spot's location is within the original map
                return True, coords
    return False, None            



def uplookahead(y,x, themap):
    ahead = []
    for i in range(1, y+1):
        ahead.append(themap[y-i])
    return 

#### moving lookahead codeup

def downlookahead(y,x, themap):
    ahead = []
    for i in range(1, len(themap) - y):  # From 1, stop before going out of bounds
        ahead.append(themap[y + i][x])  # Look below the current position
    return ahead

def leftlookahead(y,x, themap):
    ahead = []
    for i in range(1, x+1):  
        ahead.append(themap[y][x - i])  # Look to the left
    return ahead

def rightlookahead(y, x, themap):
    ahead = []
    for i in range(1, len(themap[y]) - x):  # From 1, stop before going out of bounds
        ahead.append(themap[y][x + i])  # Look to the right
    return ahead



## recycle code for input dir dict translation

nextdirections = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1)
}

nextdirendoftheline = {
    "^": uplookahead(y,x, themap),
    "v": downlookahead(y,x, themap),
    ">": rightlookahead(y, x, themap),
    "<": leftlookahead(y,x, themap)
}


def hasspace(lst):
    found_dot = False
    for i, char in enumerate(lst):
        if char == "O" and i > 0:  # Skip the first "O" since it's guaranteed
            if not found_dot:  # If we see an "O" without a preceding "."
                return False
        elif char == ".":  # If we find a ".", mark it as found
            found_dot = True
    return True

## if no obstruction, update location with coord deltas
#dir = '>'

### check if obstruction

def validmove(y,x, dir, themap):
    ndir = nextdirections[dir]
    y2 = int(y)+int(ndir[0])
    x2 = int(x)+int(ndir[1])
    if themap[y2][x2] == ".":
        return True, ".", y2, x2
    else:
        if themap[y2][x2] == "#":
            return False, ""
        else:
            if themap[y2][x2] == "O":
                lst = nextdirendoftheline[dir]
                if hasspace(lst):
                    return True, lst
                ### do dir lookup of function to get to the end of the line
                ### look to the end of the line
            else:
                return False, "error"
#### Note: you can push multiple Os but no #s and Os cannot be "squished"
### i need to lookahead to to the next available . or #. skipping over Os
##I suppose only 2 replacements would ever be needed, though conceptually could involve several more "O"s sliding around. 
# These two being the list[0] to an "@" and the leftmost "." with an "O"

def processlist(lst):
    lst[0] = '@'  # Replace the first element with '@'
    
    # Find the first "." and replace it with "O"
    for i, char in enumerate(lst):
        if char == '.':
            lst[i] = 'O'
            break  # Stop after the first replacement
    return lst


def update_map_with_shunt(y, x, dir, themap, shunt):
    # Translate direction into movement deltas
    delta_y, delta_x = nextdirections[dir]
    
    # Update the map with the new values from shunt
    for i, value in enumerate(shunt):
        current_y = y + i * delta_y
        current_x = x + i * delta_x
        
        # Boundary check
        if 0 <= current_x < len(themap[current_y]):
            themap[current_y][current_x] = value
        else:
            print(f"Error: Index out of bounds at ({current_y}, {current_x})")

start = findbot(themap)

y = start[1][0]
x = start[1][1]

for dir in input:
    nxt = validmove(y, x, dir, themap)
    if nxt[0] == False:
        continue
    else:
        if nxt[0] and nxt[1] == ".": ## free space, move the bot
            themap[y][x] = "."
            y=nxt[2]
            x=nxt[3]
            themap[y][x] = "@"
        else:
            restofline = nxt[1]
            print(f"Rest of line: {restofline}")  # Debug the extracted line

            shunt = processlist(restofline)
            print(f"Shunt after processing: {shunt}")  # Debug processed shunt

            if shunt:
                update_map_with_shunt(y, x, dir, themap, shunt)
            else:
                print("Error: Shunt returned None or invalid list!")
    print(themap)
            


