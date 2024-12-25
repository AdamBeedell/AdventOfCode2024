#24.py

## it is very close to christmas, time+energy at a minimum

### oh hey a monitoring device

### there are AND, OR and XOR gates

## gates wait until they've recieved both signals before outputting

## wires can carry 0, 1, null - Yay nulls.

inputa = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0"""

inputa = inputa.splitlines()


inputb = """x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

inputb = inputb.splitlines()


#The question is very wordy, basically we're simulating basic logic gates, but also the layout of the question breaks my brain a bit

## in order to be able to simulate the gates waiting i'd need to set the gates up first I think?

## each wire should be a key, and it's value should be the value,

#ops = {
#    'AND': &,
#    'OR': |,
#    'XOR': ^
#}

## leaving house for xmas soon

def doOps(string):   ### each reference to string[0] and [2] need to be replaced with a lookup
    strings = string.split(' ')
    if string[1] == 'XOR':
        return int(string[0]) ^ int(string[2])
    if string[1] == 'OR':
        return int(string[0]) | int(string[2])
    if string[1] == 'AND':
        return int(string[0]) & int(string[2])


gates = {}
wires = {}

for wire in inputa:
    line = wire.split(': ')
    wires[line[0]] = line[1]

for gate in inputb:
    gate = gate.split(' ') ### not sure if best to split here or have this as the whole key
    gates.setdefault().add()### something here
    doOps(gate)




## then each gate should also be a key in another structure?


    
