# 13.py


input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

input = input.splitlines()

## need to parse the input into 3s, then split out the colons, then trim, then stick in vars

## not sure if best to store at buttonA[1:4] or machine[1:4]. I'm leaning toward the latter

## have been using Y,X all through AoC because of how splitlines and split tend to line up

buttona=[34, 94]
buttonb=[67,22]
prize=[5400, 8400]


## the puzzle has been constructed for there to be less than 100 button presses to reach the prize coord.

#assuming we start at 0,0
for prizedir, in prize: 
    #for i in range(0,100):
    maxa = prizedir//buttona[0]
    maxb = prizedir//buttona[0]
    maxa = min(maxa, 100)
    maxb = min(maxb, 100)
    for i in range(0, max(maxa,maxb)):
        maxa-i * buttona[0]
