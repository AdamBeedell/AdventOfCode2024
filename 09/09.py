### 09.py

diskmap = """2333133121414131402"""

## going to be using that step-by-two function from yesterday

### doing a defrag kinda

### the string of numbers above alternates between digits saying the used blocks and the free blocks, 2 used, 3 free, 3 used, 3 free etc.

### we're to condense out the free space on the left by moving items from the right one at a time

### two pointer block loop?

### then checksum - result = 0, for each int(char) in string, result += i*char