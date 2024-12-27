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


inputa = open("25\\input.txt").read()#.replace("\r\n", "\n")

######### this got bugged out for a while, possibly by input being a builtin?
#keylocks2 = []
# Separate by double line breaks, then separate by line breaks
keylocks = inputa.split("\n\n")
for i, keylock in enumerate(keylocks):
    #keylocks2.append(keylock.splitlines())
    keylocks[i] = keylock.splitlines()



# Locks and keys are column heights
maxheight = len(keylocks[0])  # Assume all keylocks have the same height

# Separate into keys and locks
def sortintokeysandlocks(keylock):
    if keylock[0] == "#####":
        print("lock")
        return "lock"
    elif keylock[-1] == "#####":
        print("key")
        return "key"

keys = []
locks = []

for keylock in keylocks:
    if sortintokeysandlocks(keylock) == "lock":
        locks.append(keylock)
    elif sortintokeysandlocks(keylock) == "key":
        keys.append(keylock)


def translate_keylock(keylock):
    result = [0,0,0,0,0]
    for line in keylock:
        for charno, char in enumerate(line):
            if char == '#':
                result[charno] += 1
    return result

#translate_keylock(keys[0])
#translate_keylock(locks[0])

# Define trykey function
def trykey(lock_translated, key_translated):
    checks = ""
    for apin, bpin in zip(lock_translated, key_translated):
        if apin + bpin == maxheight:
            checks += "1"
    return checks == "11111" ## if all successful, True, else False

# Check overlap and find successful pair IDs
successful_pairs = []

for lock in locks:
    lock_translated = translate_keylock(lock)
    for key in keys:
        key_translated = translate_keylock(key)
        if trykey(lock_translated, key_translated):
            successful_pairs.append((locks.index(lock), keys.index(key)))

print(len(successful_pairs))

#### turns out I'm looking for keys that'd open locks, whereas the question is looking for keys that fit in the lock. WHY. ARGH


def trykeyass(lock_translated, key_translated):
    checks = ""
    for apin, bpin in zip(lock_translated, key_translated):
        if apin + bpin <= maxheight:
            checks += "1"
    return checks == "11111" ## if all successful, True, else False

successful_pairs_ass = []

for lock in locks:
    lock_translated = translate_keylock(lock)
    for key in keys:
        key_translated = translate_keylock(key)
        if trykeyass(lock_translated, key_translated):
            successful_pairs_ass.append((locks.index(lock), keys.index(key)))

print(len(successful_pairs_ass))

