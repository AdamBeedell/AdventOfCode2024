#20.py


themap = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

## it's a racetrack from S to E, where .s are good paths and #s are obstacles
## You can pass up to 2 obstacles
## What's the fastest modified path to the end

## kinda no idea how to solve this.

themap = themap.splitlines()

## i suppose it involves DFS and something like the "sheilds" from day 9 or whatever it was

## i guess you could generate a list of valid paths, then iterate over any 1 boundary layers, setting them to .s and rerunning. then going back over 2 item boundary layers.

## or it could be that the use of a "jump" (going over a #) could be treated as a 3d thing perhaps. 
# Maybe any # next to a . could be labled 1, and any # between a . and a 1 could be labled a 2, then .s, 1s and 2s could be in the search space until 2 are expended somehow.