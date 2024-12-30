#12.py

input="""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

### we're figuring out area and perimeter of areas on the map as defined by boundaries between contiguous letters 


## bound A = area (4) * perimeter (4+4+1+1)
## bound B = area (4) * perimeter (2+2+2+2)
## bound C = area (3) * perimeter (2+1+1+1+1+2+1+1+1)
## bound D = area (1) * perimeter (1+1+1+1)
## bound E = area (3) * perimeter (3+3+1+1)


## area is count of letters in shape or len(shape) or whatever. Easy.

## is perimeter per line equal to count of non-matching neighbours?

##  FFF- adds 8-1 = 7
##   F - adds 4-1 = 3


## seems like an OK approach. Need to add a perimeter to the whole map so i can count without out-of-index errors

## is perimeter per char equal to count of non-matching neighbours?

#  AAAA   3+1+1+3
#   AA    1+2
#   A     3      = 14

## also seems legit.

### parse the map

themap = input.splitlines()


### pad the map to avoid dealing with index out of range

for y, line in enumerate(themap):
    line = f" {line} "
    themap[y] = line

topntail=""
for i in range(0,len(themap[0])):
    topntail += " "
themap.append(topntail)
themap.append(topntail)
themap = [themap[-1]]+themap[:-1]

for line in themap:
    print(line)


### process the map into baskets per letter

from collections import defaultdict   ### a regular dict would work but this gives less errors it seems

coords = defaultdict(list)

for y, line in enumerate(themap):
    for x, char in enumerate(line):
        if char != ' ':
            coords[char].append((y,x))


### get area of all baskets

areas = defaultdict(list)
for letter in coords:
    areas[letter].append(len(coords[letter]))


### get perimeter

perimeters = defaultdict(list)

def getperimeter(c,y,x,themap):
    cardinalneighbors = 0
    if themap[y-1][x] != c:
        cardinalneighbors +=1
    if themap[y+1][x] != c:
        cardinalneighbors +=1
    if themap[y][x-1] != c:
        cardinalneighbors +=1
    if themap[y][x+1] != c:
        cardinalneighbors +=1
    return cardinalneighbors

for letter in coords:
    for y,x in coords[letter]:
        #print(y)
        #print(x)        
        perimeters[letter].append(getperimeter(letter,y,x,themap))


### get prices

prices = defaultdict(list)

for letter in coords:
    price = 0
    price = int(sum(areas[letter]))*int(sum(perimeters[letter]))
    prices[letter].append(price)

#sum and output price

totalprice = 0
for price in prices:
    totalprice += sum(prices[price])

print(totalprice)


## validates working on the small set

## fails on the larger set because you can have multiple sets of plants with the same letter

## this breaks a good deal of the logic...
