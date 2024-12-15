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

input = """<^^>>>vv<v>>v<<"""

## recycle code for robot position lookup

def findguard(map):
    for y, line in enumerate(map):
        for x, spot in enumerate(line):
            if spot in ('^','v','>','<'):
                coords = [y,x] ### I want to pass in/out what the spot's location is within the original map
                return True, coords
    return False, None            


## recycle code for input dir dict translation

nextdirections = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1)
}



## if no obstruction, update location with coord deltas




