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

gates = {}
for gate in inputb:
    gate = gate.split(' ') ### not sure if best to split here or have this as the whole key
    gates.add()### something here


## leaving house for xmas soon

