#16.py

## getting harder to get the time with christmas nearing

## 2d map problem today (tomorrow really) with a depth first search to impliment

## can reuse code blocks for next directions

nextdirections = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1)
}


## can reuse code block for finding start (and/or end)

def finddeer(themap):
    for y, line in enumerate(themap):
        for x, spot in enumerate(line):
            if spot == 'S':
                coords = [y,x] ### I want to pass in/out what the spot's location is within the original map
                return True, coords
    return False, None            


## not trying to write my own backdoored DFS this time, will be finding a codeblock that searches properly.

# parse input
themap="""###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

themap = [list(row) for row in themap.splitlines()]

finddeer(themap)

