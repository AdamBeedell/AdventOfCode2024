#25.py

### i've got some christmas to go do

### this one seem pretty easy actually, but I'll need to attempt on the 26th

## pins and locks

eglock = """
#####
.####
.####
.####
.#.#.
.#...
....."""


egkey = """
.....
#....
#....
#...#
#.#.#
#.###
#####
"""

eglock = eglock.trim()
egkey = egkey.trim()

eglocksandkeys=""".....
#...#
#.#.#
#.###
#.###
#.###
#####

#####
#.###
#..##
#..##
#..##
#..#.
.....

#####
####.
#.##.
#.#..
#.#..
#.#..
.....

.....
.....
..#..
..#..
#.#.#
#.###
#####"""

## Seperate by double line breaks
## then seperate by line breaks
## add all to new var keylocks

### locks and keys are colum heights

#maxhight = len(keylock[0]) # == 7

## if they overlap, not a good key/lock



#def sortintokeysandlocks
#if keylock[0] == "#####":
    #return lock
#if keylock[-1] == "#####"
    #return key

## for keylock in keylocks
    # seperate into keys and locks



## for lock in locks and key in keys:
    #translate diagram to [x,y,a,b,c] where each of those are ints representing height/depth from the home row to the max index set to #



## def trykey(lock, key)
    #  for apin, bpin in lock, key
    #      checks = ""
    #      if apin + bpin == maxheight:
    #         checks+= "1"
    #   if checks == "11111"
    #        return True
    #    else:
    #        return False
    

##for lock in locks


### def checkoverlap, add successful pairIDs to a list, print len(list)


input=""".....
#...#
#.#.#
#.###
#.###
#.###
#####

#####
#.###
#..##
#..##
#..##
#..#.
.....

#####
####.
#.##.
#.#..
#.#..
#.#..
.....

.....
.....
..#..
..#..
#.#.#
#.###
#####

#####
.####
.##.#
.##.#
.#..#
.....
.....

#####
##.##
#..#.
...#.
...#.
...#.
.....

#####
#####
#####
##.#.
.#...
.....
.....

.....
.....
.#..#
.#.##
#####
#####
#####

.....
.#...
.#.#.
.#.#.
.#.#.
####.
#####

#####
#####
###.#
###.#
###.#
.#..#
.....

.....
.#...
.#...
.##..
###..
####.
#####

#####
.##.#
.##.#
..#..
..#..
.....
.....

#####
.###.
.#.#.
.#.#.
.#.#.
...#.
.....

#####
.####
.#.##
.#.##
.#.##
...#.
.....

#####
#.###
..###
..##.
...#.
...#.
.....

#####
#.#.#
#.#.#
#.#.#
#....
#....
.....

#####
#####
###.#
.##.#
..#.#
.....
.....

.....
...#.
.#.#.
.###.
####.
####.
#####

.....
..#..
..##.
..##.
.###.
#####
#####

.....
...#.
#..#.
#..#.
#.##.
#.##.
#####

.....
....#
..#.#
#.#.#
#####
#####
#####

.....
..#..
#.#..
#.#.#
#.###
#.###
#####

#####
#.###
#.###
#.##.
#..#.
...#.
.....

#####
####.
.#.#.
.#.#.
.....
.....
.....

.....
#....
#...#
#...#
#..##
#.###
#####

#####
#.###
#.###
...##
....#
....#
.....

.....
.....
...#.
#..#.
##.#.
####.
#####

.....
.....
.....
#.#.#
#.#.#
#.###
#####

.....
....#
..#.#
#.###
#.###
#.###
#####

.....
.....
.#...
.##..
.##..
###.#
#####

#####
.####
.#.##
.#.##
...#.
.....
.....

.....
..#..
..#.#
..###
#.###
#####
#####

.....
..#.#
..#.#
..#.#
..###
.####
#####

.....
.....
...#.
.#.#.
.#.#.
.#.#.
#####

#####
#.###
#.###
..##.
..#..
.....
.....

.....
.....
.....
.#...
.#..#
.#.##
#####

#####
###.#
#.#.#
#.#.#
#.#.#
#.#.#
.....

.....
....#
..#.#
..#.#
..#.#
#.#.#
#####

#####
#####
##.#.
.#.#.
.#...
.....
.....

.....
..#..
..#..
.##..
.###.
#####
#####

#####
####.
##.#.
##.#.
#....
#....
.....

.....
....#
#...#
##..#
###.#
###.#
#####

#####
#####
#####
###.#
.##.#
..#.#
.....

#####
##.##
##.##
##..#
##..#
.#...
.....

#####
.##.#
.##.#
.##..
..#..
.....
.....

.....
....#
....#
.#..#
###.#
###.#
#####

#####
#####
#####
.###.
..#..
.....
.....

#####
##.##
##.##
.#.##
.#.##
...#.
.....

.....
.....
...#.
#..#.
##.##
##.##
#####

#####
#####
#.###
..##.
..#..
..#..
.....

#####
#####
####.
####.
.#.#.
...#.
.....

.....
.#...
.##.#
###.#
#####
#####
#####

#####
#####
####.
#.##.
#..#.
#....
.....

#####
#.###
...##
...##
....#
.....
.....

.....
...#.
.#.#.
.#.##
.#.##
.####
#####

.....
.#.#.
.#.#.
.#.##
.####
.####
#####

#####
#####
#.###
#.#.#
..#.#
....#
.....

#####
####.
##.#.
##.#.
#..#.
...#.
.....

.....
#.#..
#.##.
#.##.
#.##.
#.##.
#####

#####
####.
####.
##.#.
##.#.
.#.#.
.....

#####
#.##.
..#..
..#..
.....
.....
.....

.....
#...#
##.##
##.##
##.##
#####
#####

#####
#####
.###.
..##.
...#.
...#.
.....

#####
#####
#####
.#.##
.#.#.
...#.
.....

#####
##.##
#...#
#...#
#...#
....#
.....

.....
.....
.....
....#
#.#.#
###.#
#####

#####
#.###
#.###
#..##
#..##
...#.
.....

#####
###.#
##..#
##..#
##..#
#....
.....

#####
#.#.#
#.#.#
#.#..
#.#..
#.#..
.....

#####
##.##
#..##
#..#.
...#.
.....
.....

#####
#.###
#.###
...##
...##
....#
.....

.....
...#.
..##.
.###.
#####
#####
#####

#####
##.##
##.##
#...#
#....
.....
.....

.....
.....
#....
#.#..
#.#.#
###.#
#####

#####
###.#
.##.#
..#.#
..#..
.....
.....

#####
#####
##.##
.#.#.
.#...
.....
.....

.....
.#...
###..
###..
###..
####.
#####

.....
.#.#.
.#.#.
.#.#.
##.##
#####
#####

#####
#.###
#.##.
#..#.
#..#.
#....
.....

#####
##.##
.#.##
.#.##
...#.
.....
.....

.....
#...#
#...#
##..#
###.#
#####
#####

#####
#####
#####
.###.
..##.
...#.
.....

.....
.#...
.#...
.#...
##..#
###.#
#####

#####
#####
#####
#.###
..#.#
....#
.....

#####
#.###
..###
..##.
..##.
...#.
.....

.....
.....
...#.
...#.
#..#.
##.#.
#####

.....
.#...
.#.#.
.###.
.###.
#####
#####

.....
..#..
..#..
..##.
#.##.
#.##.
#####

.....
...#.
...#.
.#.##
##.##
#####
#####

#####
#####
#.###
..###
..##.
...#.
.....

#####
#####
#####
###.#
#.#..
.....
.....

.....
.#...
.##..
.##..
.##..
###.#
#####

#####
####.
.###.
..##.
...#.
.....
.....

#####
##.#.
#..#.
#..#.
...#.
.....
.....

#####
####.
#.##.
#.##.
#.##.
#..#.
.....

.....
..#..
..#.#
#.#.#
###.#
###.#
#####

#####
.#.##
.#..#
.#...
.....
.....
.....

.....
.#...
.#...
.##.#
.####
.####
#####

.....
..#..
#.#..
#.#..
####.
####.
#####

#####
#####
.####
.#.#.
.#.#.
.....
.....

.....
#....
#....
##...
###.#
###.#
#####

.....
.....
..#..
#.#..
#.#.#
#.###
#####

.....
.....
...#.
...##
.#.##
#####
#####

.....
.#.#.
.#.#.
.#.#.
.#.##
.#.##
#####

#####
#####
###.#
###.#
#.#.#
#.#..
.....

.....
..#..
..#..
..##.
#.###
#.###
#####

#####
##.##
#...#
....#
.....
.....
.....

.....
.....
...#.
..##.
#.###
#.###
#####

.....
..#..
..#..
..#..
.###.
.####
#####

#####
#####
####.
##.#.
##.#.
.#.#.
.....

#####
.#.#.
.#.#.
...#.
.....
.....
.....

.....
...#.
#..#.
#.###
#####
#####
#####

.....
#....
#....
#.#..
#.#..
###.#
#####

.....
..#..
..##.
..###
.####
.####
#####

.....
.....
.....
#...#
##.##
##.##
#####

#####
####.
#.##.
#.##.
#..#.
.....
.....

#####
#####
#####
#####
#.##.
#.#..
.....

#####
###.#
###..
###..
###..
#.#..
.....

#####
##.#.
##.#.
##.#.
##.#.
.#.#.
.....

.....
.....
...#.
..##.
.###.
.###.
#####

.....
.....
.....
.#.#.
##.#.
####.
#####

.....
#..#.
#..#.
##.#.
##.##
#####
#####

.....
.#...
.##..
.##.#
###.#
#####
#####

.....
.....
#..#.
#..#.
#.##.
#.##.
#####

.....
.#..#
.#.##
.#.##
.#.##
#####
#####

#####
.###.
..##.
..#..
.....
.....
.....

.....
.#...
.#...
.##.#
.##.#
.####
#####

#####
.####
.##.#
.##.#
.##..
..#..
.....

#####
.###.
.###.
.#.#.
...#.
...#.
.....

#####
##.##
#...#
#...#
#...#
.....
.....

.....
.....
..#.#
..#.#
.##.#
###.#
#####

#####
#.##.
#..#.
...#.
...#.
...#.
.....

#####
###.#
.#..#
.#...
.#...
.#...
.....

#####
##.##
##.##
#..##
#...#
#....
.....

#####
#####
###.#
###..
#.#..
..#..
.....

#####
#####
####.
#.##.
...#.
...#.
.....

.....
#..#.
#..#.
#..#.
##.#.
####.
#####

#####
.##.#
..#.#
..#.#
....#
....#
.....

#####
.###.
.#.#.
.#.#.
...#.
...#.
.....

#####
###.#
#.#.#
..#..
.....
.....
.....

.....
.....
..#.#
#.###
#.###
#####
#####

#####
#####
##.##
.#.##
.#.#.
.....
.....

.....
...#.
#..#.
#..#.
#..#.
##.#.
#####

.....
..#..
..#..
.##.#
###.#
#####
#####

.....
#....
#....
#....
#...#
##.##
#####

.....
..#..
..#..
..##.
#.###
#####
#####

.....
...#.
#..#.
#..##
#.###
#####
#####

.....
#....
#..#.
#.##.
#.##.
#####
#####

#####
##.##
##.#.
.#...
.#...
.....
.....

#####
#####
####.
####.
.##..
..#..
.....

.....
..#.#
.##.#
.##.#
#####
#####
#####

.....
...#.
...##
..###
.####
.####
#####

.....
.....
#....
#....
#.#.#
###.#
#####

.....
.....
#...#
#.#.#
#.###
#####
#####

.....
#.#..
#.##.
#####
#####
#####
#####

#####
#####
#####
.#.##
.#.##
.#..#
.....

.....
....#
#..##
#..##
#..##
##.##
#####

.....
....#
....#
.#.##
.####
.####
#####

.....
..#..
..#..
..##.
.####
#####
#####

#####
#.###
#.###
#.#.#
#.#.#
.....
.....

.....
...#.
..##.
#.##.
#.###
#####
#####

#####
#.###
..###
..#.#
..#..
.....
.....

.....
#...#
#...#
#..##
#.###
#.###
#####

.....
#....
##.#.
##.#.
####.
####.
#####

#####
.##.#
.##.#
.#..#
....#
.....
.....

#####
#####
.###.
.#.#.
.#...
.#...
.....

#####
#####
#####
.#.##
.#.#.
.#...
.....

#####
#####
##.##
##.##
.#..#
.#...
.....

#####
#.###
#.###
#.###
...##
....#
.....

.....
.....
.#...
###..
####.
####.
#####

#####
#####
#####
##.##
.#.##
.#.#.
.....

#####
##.##
##..#
##..#
#...#
#....
.....

.....
#....
#....
#.#..
###.#
###.#
#####

#####
.####
.####
.#.##
...##
...#.
.....

.....
.....
..#.#
#.#.#
#.###
#####
#####

.....
....#
.#..#
.#..#
.##.#
###.#
#####

#####
####.
.###.
.##..
..#..
..#..
.....

.....
.....
...#.
...#.
.#.#.
##.##
#####

#####
##.##
##.##
#...#
.....
.....
.....

.....
....#
....#
..#.#
..###
.####
#####

.....
.#...
.#.#.
##.#.
##.##
##.##
#####

#####
#####
#.###
#.###
..##.
...#.
.....

.....
#..#.
#..#.
#.##.
#.##.
#####
#####

#####
#####
##.##
##.#.
#..#.
...#.
.....

#####
#####
#####
#.#.#
#.#.#
#....
.....

.....
.....
#....
#..#.
#..#.
##.##
#####

#####
#####
##.##
.#.##
...##
....#
.....

#####
.####
.####
.####
..###
...#.
.....

.....
...#.
..##.
..##.
.###.
.####
#####

.....
...#.
.#.#.
.#.#.
##.##
#####
#####

#####
#####
####.
#.#..
#....
#....
.....

.....
...#.
#..#.
#.##.
####.
#####
#####

#####
####.
##.#.
##.#.
##.#.
.#...
.....

.....
..#.#
.##.#
###.#
###.#
#####
#####

#####
####.
####.
#.##.
..##.
...#.
.....

#####
#.###
#..#.
#..#.
...#.
.....
.....

#####
##.##
#..##
#...#
....#
.....
.....

.....
....#
....#
....#
..#.#
#.###
#####

#####
##.##
##.#.
.#.#.
...#.
.....
.....

.....
...#.
#..#.
##.##
##.##
#####
#####

#####
#.##.
#.##.
...#.
...#.
...#.
.....

.....
....#
....#
..#.#
#.#.#
#.#.#
#####

#####
##.##
##.##
##.##
.#..#
.#..#
.....

.....
.#...
##...
##..#
##.##
#####
#####

.....
#....
#....
#....
##...
##.#.
#####

#####
###.#
#.#.#
#.#..
#....
#....
.....

#####
#####
#####
#####
##.#.
#....
.....

#####
###.#
###.#
.#...
.....
.....
.....

.....
.#...
.#...
.#.#.
.#.#.
####.
#####

.....
.#...
.##.#
###.#
###.#
#####
#####

#####
###.#
#.#.#
#...#
#...#
....#
.....

#####
#.##.
..#..
..#..
..#..
.....
.....

#####
####.
####.
.##..
.#...
.....
.....

#####
#####
###.#
###.#
.##.#
.#...
.....

.....
..#..
#.##.
#.##.
#.###
#.###
#####

#####
#####
###.#
##..#
##..#
#...#
.....

.....
.....
.#...
.#..#
.##.#
###.#
#####

.....
...#.
...#.
...##
...##
.#.##
#####

.....
..#..
..#..
#.#..
#.#.#
###.#
#####

#####
#####
###.#
##..#
##...
.#...
.....

.....
#....
#..#.
#..##
##.##
#####
#####

.....
..#..
.##..
.##..
###.#
###.#
#####

.....
..#..
#.##.
#.##.
####.
####.
#####

.....
.#..#
.#.##
.####
.####
#####
#####

#####
#.###
#..##
#..##
...#.
...#.
.....

#####
#####
#####
#.###
#.#.#
....#
.....

.....
.....
....#
....#
..#.#
#.#.#
#####

#####
#.#.#
#.#.#
#.#..
#.#..
#....
.....

.....
.....
..#.#
#.#.#
###.#
###.#
#####

#####
###.#
###.#
.##.#
..#..
..#..
.....

#####
#####
.###.
..#..
..#..
..#..
.....

#####
###.#
###..
##...
##...
#....
.....

#####
#.###
#.##.
#..#.
#..#.
#..#.
.....

#####
##.##
.#..#
.#..#
.#..#
.....
.....

#####
#####
.####
.####
..###
..#.#
.....

.....
.....
.....
#....
##..#
###.#
#####

.....
....#
....#
..#.#
.####
.####
#####

.....
...#.
...#.
...#.
..##.
.###.
#####

.....
.....
#....
#.#.#
#.###
#####
#####

.....
#....
#..#.
#..##
##.##
##.##
#####

#####
.###.
.###.
.###.
.#.#.
.#.#.
.....

.....
.....
....#
..#.#
.##.#
###.#
#####

.....
#.#.#
#.#.#
#.#.#
#.#.#
###.#
#####

.....
.....
.....
.#...
##..#
###.#
#####

.....
..#..
.##..
.##.#
.####
#####
#####

.....
.#..#
##.##
##.##
##.##
##.##
#####

#####
.####
.####
.###.
.###.
..#..
.....

#####
#####
.#.##
.#.##
....#
....#
.....

#####
####.
#.##.
#.##.
...#.
...#.
.....

#####
#####
.####
.####
.##.#
..#..
.....

#####
.####
.#.#.
.#.#.
.#.#.
.#...
.....

#####
###.#
##..#
#....
.....
.....
.....

#####
#####
###.#
.##.#
.##.#
.#..#
.....

.....
.....
...#.
.#.#.
.#.#.
#####
#####

.....
....#
..#.#
..#.#
.##.#
.##.#
#####

.....
#...#
#.#.#
#.#.#
###.#
#####
#####

.....
...#.
#.##.
#.###
#.###
#####
#####

.....
..#..
..#..
.##..
.###.
####.
#####

#####
#####
###.#
#.#.#
..#..
.....
.....

#####
#####
.####
.####
..#.#
.....
.....

#####
#####
###.#
###.#
###..
.#...
.....

#####
#####
#.###
#.###
#.#.#
#.#..
.....

.....
.#..#
##.##
#####
#####
#####
#####

#####
###.#
###..
.##..
..#..
..#..
.....

#####
#####
.####
..###
...#.
...#.
.....

#####
#####
#.#.#
#.#.#
#.#.#
..#.#
.....

#####
#####
.####
..##.
..##.
...#.
.....

#####
.####
.#.##
.#.##
...#.
...#.
.....

.....
...#.
.#.#.
.#.##
#####
#####
#####

#####
.####
.#.#.
.#.#.
.#.#.
.....
.....

.....
.#..#
.#..#
.##.#
.##.#
###.#
#####

#####
####.
.###.
.##..
.#...
.#...
.....

.....
.....
#....
#....
##.#.
##.##
#####

.....
#.#.#
#.#.#
#.#.#
#####
#####
#####

.....
#....
#....
#....
##..#
###.#
#####

.....
.#...
###..
###.#
#####
#####
#####

#####
.#.##
.#..#
.#..#
....#
....#
.....

#####
###.#
.##..
.##..
.##..
.#...
.....

#####
##.##
##.##
##..#
.#...
.#...
.....

#####
#.###
...##
...##
....#
....#
.....

#####
#.###
#.###
#.###
..###
...#.
.....

.....
.#...
.##..
.##..
.###.
#####
#####

.....
.#..#
.#..#
.#..#
.#.##
##.##
#####

.....
...#.
...#.
...#.
#..#.
#.###
#####

.....
.#...
##...
##..#
##..#
###.#
#####

#####
#.###
#..##
...#.
.....
.....
.....

#####
###.#
###.#
###.#
.##..
..#..
.....

#####
#####
.##.#
..#.#
..#.#
..#..
.....

.....
.....
.#.#.
.#.#.
##.#.
##.#.
#####

.....
.....
.#...
.#...
.#.#.
.#.#.
#####

#####
.##.#
.##.#
.##..
..#..
..#..
.....

#####
.##.#
.##..
..#..
..#..
..#..
.....

.....
....#
....#
.#.##
#####
#####
#####

#####
#.###
#.###
..#.#
..#.#
..#..
.....

.....
.....
.#...
.#..#
###.#
###.#
#####

#####
###.#
###.#
.##.#
.##.#
.#...
.....

.....
.#.#.
.#.#.
.#.#.
.#.#.
.#.#.
#####

.....
.....
...#.
...#.
..##.
#.##.
#####

.....
..#..
..##.
..##.
.####
.####
#####

#####
###.#
.##.#
.#..#
.#..#
.....
.....

#####
#.###
#.#.#
#.#.#
#.#.#
#...#
.....

#####
##.##
.#..#
.#...
.....
.....
.....

#####
##.##
##.##
.#.##
.#.#.
.#.#.
.....

#####
#####
.####
.##.#
.##.#
.#..#
.....

#####
####.
####.
##.#.
#..#.
...#.
.....

#####
#####
.####
.#.##
.#.#.
...#.
.....

.....
.....
.....
..#.#
#.#.#
#####
#####

.....
.....
#...#
##..#
###.#
###.#
#####

.....
....#
...##
#..##
#..##
#.###
#####

.....
#..#.
#..#.
##.#.
#####
#####
#####

.....
.#...
.##..
.##..
.##..
####.
#####

.....
...#.
...#.
#..#.
#..#.
#.##.
#####

#####
#.###
#..##
#...#
#...#
.....
.....

.....
.....
#...#
##..#
##..#
###.#
#####

#####
##.##
.#.##
.#.#.
.#...
.#...
.....

.....
#..#.
#..#.
#..#.
#..##
##.##
#####

.....
#....
#....
#....
#.#..
#.#.#
#####

.....
.....
...#.
#.###
#.###
#####
#####

#####
####.
.###.
..##.
...#.
...#.
.....

.....
#...#
#...#
#...#
#..##
#.###
#####

#####
#.###
#.###
#.#.#
#...#
.....
.....

#####
#.##.
#.#..
#....
#....
#....
.....

#####
.###.
.###.
.###.
.##..
.#...
.....

#####
###.#
##..#
##..#
.#...
.....
.....

.....
..#..
.###.
#####
#####
#####
#####

#####
##.##
#..##
#..##
...#.
.....
.....

#####
#####
.###.
.###.
.##..
.#...
.....

#####
##.##
##.##
##.#.
#....
.....
.....

#####
#####
###.#
.#...
.#...
.....
.....

.....
.....
.....
#....
#.#.#
#.###
#####

#####
####.
#.#..
#.#..
..#..
..#..
.....

.....
.....
#....
#...#
#..##
#.###
#####

#####
###.#
#.#.#
#.#.#
#.#.#
#...#
.....

.....
.....
.....
.#...
.#...
.#.#.
#####

.....
.....
.#.#.
.#.#.
##.##
#####
#####

#####
#.###
..###
...#.
.....
.....
.....

.....
...#.
.#.#.
.#.#.
.###.
.###.
#####

.....
#....
##.#.
##.#.
##.#.
####.
#####

.....
.....
.....
..#..
..#..
#.#.#
#####

#####
#.#.#
#.#.#
#.#.#
..#..
..#..
.....

#####
#####
.##.#
.##.#
.#..#
.#...
.....

.....
.....
#...#
#..##
##.##
##.##
#####

.....
.....
.#...
##.#.
##.#.
##.##
#####

.....
..#..
..#..
.##.#
.####
#####
#####

#####
####.
##.#.
.#.#.
...#.
...#.
.....

#####
##.##
##..#
##...
#....
.....
.....

#####
#####
.##.#
.##..
.#...
.....
.....

.....
....#
....#
..#.#
..#.#
#.#.#
#####

.....
.#.#.
.#.#.
.#.#.
.#.##
.####
#####

#####
##.##
##.##
##..#
.#...
.....
.....

#####
#####
###.#
##...
.#...
.....
.....

#####
##.##
#..##
#..##
#...#
.....
.....

.....
...#.
#..##
#..##
#.###
#.###
#####

.....
.#..#
.#..#
##..#
##.##
##.##
#####

.....
.....
.....
.#..#
###.#
###.#
#####

.....
.....
.....
....#
..#.#
.####
#####

#####
#.##.
#.##.
#.##.
#.#..
#.#..
.....

.....
.....
.....
#..#.
#.###
#####
#####

.....
..#..
#.#..
#.#..
#.#..
###.#
#####

#####
####.
####.
##.#.
##.#.
.#...
.....

#####
#.###
#..##
#..##
#..##
#...#
.....

#####
#.##.
#.#..
#.#..
#.#..
..#..
.....

.....
..#..
.###.
.###.
.####
#####
#####

#####
.###.
..#..
..#..
.....
.....
.....

.....
....#
.#..#
.#..#
.#.##
.#.##
#####

.....
.#.#.
.#.##
.#.##
.#.##
#####
#####

.....
..#..
#.#..
###..
###.#
#####
#####

.....
#....
#.#..
#.#..
#.#.#
#.###
#####

.....
.....
.....
#..#.
#..#.
#.##.
#####

#####
#####
.#.##
.#.#.
.#...
.#...
.....

#####
#####
###.#
##..#
.#...
.....
.....

.....
.#...
.#...
###..
####.
####.
#####

.....
...#.
...#.
#..#.
#..##
##.##
#####

#####
#.###
#.###
#.##.
...#.
...#.
.....

.....
.....
..#..
.##..
.##..
###.#
#####

.....
.....
..#..
.##..
.##.#
.####
#####

.....
.#...
.#...
##..#
##..#
###.#
#####

.....
.....
.....
.#...
.#.#.
.####
#####

.....
.....
#..#.
##.#.
##.##
##.##
#####

.....
#....
#.#..
#.#..
###..
###.#
#####

.....
.....
..#..
.###.
.####
#####
#####

#####
###.#
#.#.#
#.#..
..#..
.....
.....

#####
.####
.##.#
.#..#
.#..#
.....
.....

.....
...#.
...#.
..##.
#.###
#####
#####

#####
#####
#####
.#.#.
.#...
.#...
.....

.....
.....
..#..
.##..
.##..
####.
#####

.....
..#..
.##..
.###.
.###.
#####
#####

#####
#####
#.###
#.###
#.###
#.#.#
.....

.....
.....
...#.
...#.
...#.
#.###
#####

#####
#####
##.##
##.##
#..##
...#.
.....

.....
..#..
#.#.#
#.#.#
###.#
#####
#####

#####
##.#.
#..#.
...#.
...#.
...#.
.....

.....
.#...
##...
##.#.
##.#.
#####
#####

.....
.....
..#..
..#..
#.##.
#####
#####

.....
#...#
#...#
#.#.#
###.#
#####
#####

.....
.....
....#
...##
#..##
##.##
#####

.....
.#..#
.#..#
.#..#
.#..#
.##.#
#####

#####
#####
#.###
#..##
#..##
#...#
.....

.....
#....
##..#
##..#
##.##
#####
#####

#####
#####
##.##
#..##
#...#
....#
.....

#####
#####
#####
.#.#.
.#.#.
.#.#.
.....

#####
###.#
.##.#
.##.#
..#.#
....#
.....

#####
##.##
#..#.
#..#.
#....
.....
.....

#####
##.##
##.##
#..#.
.....
.....
.....

.....
..#..
..#..
..##.
..##.
#.##.
#####

.....
#.#..
#.#.#
#.#.#
#.#.#
#.###
#####

.....
....#
.#.##
.#.##
.#.##
##.##
#####

#####
#####
#####
####.
##.#.
#....
.....

#####
#.###
#.#.#
#...#
#....
.....
.....

#####
#####
#.#.#
#.#.#
#.#.#
#.#.#
.....

.....
.....
.#...
.#.#.
.###.
#####
#####

.....
.....
...#.
#.###
#####
#####
#####

.....
.#...
##...
###..
####.
#####
#####

#####
#.##.
..##.
..##.
..#..
..#..
.....

.....
#...#
##..#
##.##
##.##
#####
#####

#####
##.##
.#.#.
.#.#.
...#.
...#.
.....

#####
##.##
##..#
#...#
#...#
.....
.....

.....
.....
.#...
.#...
##..#
###.#
#####

#####
####.
#.##.
#..#.
#..#.
...#.
.....

.....
.....
..#..
#.##.
#.##.
####.
#####

#####
#####
##.##
##.##
#..#.
#....
.....

.....
.....
..#..
.##.#
#####
#####
#####

.....
.....
#.#.#
#.#.#
#.#.#
#.###
#####

.....
#...#
#...#
#...#
#.#.#
#.###
#####

#####
##.#.
##.#.
##.#.
##.#.
#....
.....

.....
#....
#...#
#.#.#
#.#.#
#####
#####

#####
#.#.#
#.#..
#.#..
..#..
.....
.....

#####
#.##.
#.##.
#.#..
#.#..
..#..
.....

.....
.#...
.#..#
.#.##
.#.##
.####
#####

.....
.#...
.##..
.##.#
###.#
###.#
#####

.....
.....
.....
.#...
.#.#.
.###.
#####

.....
..#.#
..###
.####
#####
#####
#####

.....
#..#.
##.#.
##.##
#####
#####
#####

#####
.####
.####
.#.##
.#.#.
.#...
.....

.....
.#...
.#...
.#.#.
.#.#.
##.##
#####

#####
###.#
###.#
###.#
##..#
#....
.....

.....
....#
.#..#
.#..#
##..#
###.#
#####

#####
#####
.#.##
.#..#
.#..#
....#
.....

#####
#.###
#.###
#.#.#
#.#.#
#...#
.....

#####
##.##
#..##
#..##
#...#
....#
.....

.....
.....
.#...
.#...
##.#.
####.
#####

#####
#####
#.###
#.#.#
#...#
....#
.....

#####
####.
###..
.##..
.##..
..#..
.....

.....
.....
#....
#.#.#
#.###
#.###
#####

#####
.####
.####
.####
.####
.#.#.
.....

.....
....#
..#.#
..#.#
#.#.#
#.###
#####

.....
..#.#
.##.#
###.#
###.#
###.#
#####

#####
.####
..#.#
..#.#
..#.#
..#.#
.....

#####
####.
.##..
.##..
.##..
.#...
.....

#####
#.###
#.###
#..#.
#..#.
#....
.....

.....
.....
#.#..
#.#.#
#.###
#.###
#####

#####
.###.
.###.
.##..
.##..
.#...
.....

.....
....#
#...#
#...#
##.##
##.##
#####

.....
.....
..#..
#.#..
####.
####.
#####

.....
.#..#
.##.#
.##.#
###.#
###.#
#####

.....
....#
#...#
#..##
#.###
#####
#####

.....
.#...
.#...
.#.#.
.###.
####.
#####

.....
#.#..
#.#..
#.#..
###.#
#####
#####

#####
.##.#
.##.#
..#..
.....
.....
.....

#####
.####
..##.
..#..
..#..
.....
.....

#####
##.##
##.##
.#.##
....#
....#
.....

#####
###.#
.##.#
.##.#
..#.#
..#.#
.....

.....
...#.
...#.
#..#.
#.##.
#.###
#####

#####
#####
#.#.#
#.#.#
..#..
.....
.....

#####
####.
###..
#.#..
.....
.....
.....

.....
.....
.#...
.#...
.##..
.###.
#####

.....
.#..#
.#.##
.#.##
.#.##
##.##
#####

#####
##.##
##.##
##..#
#....
#....
.....

#####
#.##.
#..#.
...#.
...#.
.....
.....

.....
.....
.....
..#..
#.#..
#.##.
#####

.....
.....
.....
...#.
.#.##
.####
#####

#####
.##.#
.##.#
..#.#
....#
.....
.....

.....
.....
.....
....#
..#.#
.##.#
#####

#####
##.##
.#..#
.#..#
.#..#
.#..#
.....

.....
.....
.#..#
.#..#
.##.#
.####
#####

.....
.....
#..#.
#.##.
#.##.
#####
#####

.....
...#.
#..##
##.##
##.##
##.##
#####

.....
.....
.#...
##..#
##..#
##.##
#####

#####
#.###
#.##.
#.#..
.....
.....
.....

#####
#####
####.
##.#.
##...
#....
.....

#####
#.###
#.##.
#.#..
#.#..
#.#..
.....

.....
.#...
.##.#
.##.#
.##.#
.##.#
#####

#####
###.#
.##.#
.##.#
.##.#
.#..#
.....

.....
#....
#.#..
#.#..
####.
####.
#####

#####
.###.
.#.#.
.#.#.
.#...
.#...
.....

#####
#####
.####
.##.#
.#...
.....
.....

.....
..#..
.###.
.###.
.###.
.###.
#####

.....
..#..
..#..
.###.
.####
#####
#####

#####
##.##
.#.##
.#..#
.#...
.#...
.....

.....
...#.
...##
#..##
##.##
#####
#####

#####
#####
#####
#.#.#
#.#.#
.....
.....

.....
#.#..
#.##.
#.##.
#.##.
#####
#####

#####
##.#.
##...
#....
#....
.....
.....

.....
..#..
..##.
#.###
#####
#####
#####

#####
##.##
##.##
##.##
.#.#.
.#...
.....

#####
#.###
#.#.#
#.#.#
..#..
..#..
.....

#####
.#.##
.#.#.
.#.#.
.#.#.
.#.#.
.....

#####
####.
.#.#.
.#...
.#...
.#...
.....

.....
.#..#
.#..#
##..#
###.#
###.#
#####

#####
#####
####.
####.
.#.#.
.#.#.
....."""



# Separate by double line breaks, then separate by line breaks
keylocks = [block.splitlines() for block in input.strip().split("\n\n")]

# Locks and keys are column heights
maxheight = len(keylocks[0])  # Assume all keylocks have the same height

# Separate into keys and locks
def sortintokeysandlocks(keylock):
    if keylock[0] == "#####":
        return "lock"
    elif keylock[-1] == "#####":
        return "key"

keys = []
locks = []

for keylock in keylocks:
    if sortintokeysandlocks(keylock) == "lock":
        locks.append(keylock)
    elif sortintokeysandlocks(keylock) == "key":
        keys.append(keylock)

# Translate diagram to [x, y, a, b, c]
def translate_diagram(diagram):
    result = []
    for column in zip(*diagram):  # Transpose rows to columns
        depth = len(column) - column[::-1].index("#") - 1 if "#" in column else 0
        result.append(depth)
    return result

# Define trykey function
def trykey(lock, key):
    checks = ""
    for apin, bpin in zip(lock, key):
        if apin + bpin == maxheight:
            checks += "1"
    return checks == "11111"

# Check overlap and find successful pair IDs
successful_pairs = []

for lock in locks:
    lock_translated = translate_diagram(lock)
    for key in keys:
        key_translated = translate_diagram(key)
        if trykey(lock_translated, key_translated):
            successful_pairs.append((locks.index(lock), keys.index(key)))

print(len(successful_pairs))