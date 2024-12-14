## 14.py

## the last few days time has been low and I dont have immediate thoughts on ways of solving it.

## bit more time and energy today, but also far outside my usual working space

robots = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

themap = """"...........
...........
...........
...........
...........
...........
..........."""


robots = robots.splitlines

themap = themap.splitlines

for robot in robots:
    robot.split('=')

##parse data