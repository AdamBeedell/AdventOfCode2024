#21.py


## robotics problem


keypad = """+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+"""


robokeypad = """    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+"""


### there is a keypad that must be pressed, but you cant interact with it, instead you use a robot with robokeypad to move it's arm to press the first one

## so there's a translation thing to do between 1 and 2

## actually there's 2 additional layers of transformation

## oh god...