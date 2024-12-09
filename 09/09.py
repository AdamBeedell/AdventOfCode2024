### 09.py

diskmap = """2333133121414131402"""

## going to be using that step-by-two function from yesterday

### doing a defrag kinda

### the string of numbers above alternates between digits saying the used blocks and the free blocks, 2 used, 3 free, 3 used, 3 free etc.

## IDs are incremental on the 0,2.., ie, each file descriptor

def expand(string):
    i=0
    result = []
    id = 0
    for char in string:
        if i % 2 != 0:  ## is odd
            for x in range(0,int(char)):
                result.append(".")
        else: ## is even
            for y in range(0,int(char)):
                result.append(id)
            id += 1
        i += 1
    return result, "".join(map(str, result)) #### list ver and str ver not sure which i'll need yet



doubs = expand(diskmap)
listver = doubs[0]
stringver = doubs[1]


### we're to condense out the free space on the left by moving items from the right one at a time

### two pointer block loop?

leftpointer = 0
rightpointer = len(listver) - 1 ### length counts from 1 index counts from 0. Starts far right

while leftpointer < rightpointer: ## when the pointers meet problem should be solved
    if listver[leftpointer] == ".":  ### if spare, start swap
        while listver[rightpointer] == "." and rightpointer > leftpointer: ### right-to-left
            rightpointer -= 1  # move right-to-left
        
        if leftpointer < rightpointer:  # Perform the swap if pointers havnt met
            listver[leftpointer], listver[rightpointer] = listver[rightpointer], listver[leftpointer]

    leftpointer += 1  # move left-to-right

print(listver)


### then checksum - result = 0, for each int(char) in string, result += i*char


result = 0
i=0
for char in listver:
   if char != ".":
       result += i*int(char)
   i += 1

print(result)


#### validates correctly on test set