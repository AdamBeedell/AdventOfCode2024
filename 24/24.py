#24.py

## it is very close to christmas, time+energy at a minimum

### oh hey a monitoring device

### there are AND, OR and XOR gates

## gates wait until they've recieved both signals before outputting

## wires can carry 0, 1, null - Yay nulls.

inputa = """x00: 1
x01: 1
x02: 0
x03: 0
x04: 0
x05: 1
x06: 0
x07: 1
x08: 1
x09: 0
x10: 1
x11: 0
x12: 0
x13: 0
x14: 1
x15: 1
x16: 1
x17: 1
x18: 1
x19: 0
x20: 0
x21: 0
x22: 0
x23: 0
x24: 0
x25: 1
x26: 0
x27: 0
x28: 0
x29: 0
x30: 0
x31: 1
x32: 0
x33: 0
x34: 1
x35: 0
x36: 0
x37: 1
x38: 0
x39: 1
x40: 1
x41: 0
x42: 0
x43: 0
x44: 1
y00: 1
y01: 0
y02: 1
y03: 1
y04: 0
y05: 0
y06: 1
y07: 1
y08: 0
y09: 1
y10: 1
y11: 1
y12: 1
y13: 0
y14: 1
y15: 0
y16: 0
y17: 0
y18: 0
y19: 1
y20: 0
y21: 1
y22: 1
y23: 0
y24: 1
y25: 0
y26: 1
y27: 1
y28: 0
y29: 1
y30: 1
y31: 0
y32: 1
y33: 0
y34: 0
y35: 1
y36: 1
y37: 0
y38: 0
y39: 1
y40: 0
y41: 0
y42: 0
y43: 1
y44: 1"""

inputa = inputa.splitlines()


inputb = """y24 XOR x24 -> jhj
y00 AND x00 -> ksw
rmj OR khc -> cqp
y22 AND x22 -> pdf
fsb AND thf -> brr
y02 AND x02 -> jmb
y07 AND x07 -> fpb
x35 AND y35 -> mkv
hgm XOR jvd -> z12
hkv OR kmk -> gcm
x13 AND y13 -> vnf
tkg AND sjq -> pjh
x38 XOR y38 -> bjr
y23 XOR x23 -> wdg
bct OR ggp -> chn
hhw AND ccp -> snp
fpp AND jdw -> cfb
x21 AND y21 -> z21
y36 AND x36 -> whb
hpt XOR jkc -> z31
fbs AND bjj -> fwm
tgt OR nrg -> rkk
x42 AND y42 -> kgq
x25 AND y25 -> hkw
kpt OR fgv -> bkq
y04 AND x04 -> fnh
x19 XOR y19 -> hwf
y30 AND x30 -> wrk
rcb OR prp -> bbr
gds OR vqn -> fsh
fpk XOR bkq -> z13
y03 XOR x03 -> kpp
wkh OR pmj -> tqk
grk AND gpr -> bwv
x33 AND y33 -> qwt
gcm AND pfd -> rgn
y12 XOR x12 -> hgm
x06 XOR y06 -> fsb
x40 XOR y40 -> gfd
y28 XOR x28 -> vnn
hdt XOR wcc -> z43
gnp OR qgm -> ccp
y36 XOR x36 -> pjs
y14 XOR x14 -> shm
y05 AND x05 -> vjt
gwv XOR rkk -> z11
cqp XOR psh -> z25
y18 XOR x18 -> sgs
hjm OR jrs -> hpt
vjt OR swv -> thf
fwm OR mkv -> nmb
sgm XOR tsj -> z08
tmr XOR kpp -> z03
ccp XOR hhw -> fph
x10 AND y10 -> tgt
x26 AND y26 -> nkc
cbg AND fph -> bsb
chn XOR gfd -> z40
hmn AND jkv -> ght
rsj AND bbr -> ncn
vmf AND vwd -> nrg
brr OR wcw -> twm
gsg XOR twm -> z07
y09 XOR x09 -> sjq
x24 AND y24 -> rmj
pdf OR nns -> nsj
y44 AND x44 -> wcr
wrk XOR dwm -> z30
gpv AND wjj -> swv
y08 AND x08 -> jbk
y17 AND x17 -> gmg
x26 XOR y26 -> sjk
vpj XOR dcm -> z42
x29 AND y29 -> tqc
x15 XOR y15 -> hhw
x12 AND y12 -> fgv
x10 XOR y10 -> vmf
rwc OR nkc -> fpp
vwd XOR vmf -> z10
y32 AND x32 -> hbq
x20 XOR y20 -> sbs
x43 XOR y43 -> wcc
y11 AND x11 -> gnb
wqv XOR jvv -> z37
cqk OR dfq -> bjj
nsp XOR tqh -> gds
fbs XOR bjj -> z35
ksw AND kgn -> kmk
x01 AND y01 -> hkv
shm AND kds -> gnp
x31 XOR y31 -> jkc
gmm OR qbr -> ptm
jkv XOR hmn -> z04
x21 XOR y21 -> tqh
sjk AND btt -> rwc
ncn OR bck -> vpj
x29 XOR y29 -> dcn
y09 AND x09 -> drj
ght OR fnh -> wjj
tsj AND sgm -> vsq
vpj AND dcm -> ttq
vnf OR wmm -> kds
y08 XOR x08 -> tsj
rfw AND fsh -> nns
x03 AND y03 -> npd
bsb OR dcw -> msb
gwv AND rkk -> srh
hjq XOR pjj -> z39
kgn XOR ksw -> z01
gjd XOR dcn -> z29
pjs XOR nmb -> z36
fvv OR hkw -> btt
x35 XOR y35 -> fbs
khs AND sms -> qkf
y00 XOR x00 -> z00
ptm XOR smj -> z44
y11 XOR x11 -> gwv
y13 XOR x13 -> fpk
nrd OR nss -> bbt
jhj XOR tqk -> z24
x42 XOR y42 -> dcm
x33 XOR y33 -> grk
x34 AND y34 -> dfq
y43 AND x43 -> gmm
x19 AND y19 -> fcw
sgs AND qcf -> vsk
y14 AND x14 -> qgm
y44 XOR x44 -> smj
gnb OR srh -> jvd
hjq AND pjj -> ggp
y16 AND x16 -> dcw
wcr OR swb -> z45
x39 XOR y39 -> hjq
thf XOR fsb -> z06
rgn OR jmb -> tmr
y30 XOR x30 -> jrs
pfd XOR gcm -> z02
x05 XOR y05 -> gpv
y31 AND x31 -> hqj
smj AND ptm -> swb
shm XOR kds -> z14
wdg XOR nsj -> z23
x32 XOR y32 -> sms
y34 XOR x34 -> fcv
mkc AND vnn -> jjs
jkc AND hpt -> pct
pjh OR drj -> vwd
x06 AND y06 -> wcw
wqv AND jvv -> nrd
jbk OR vsq -> tkg
sgs XOR qcf -> z18
vsk OR hpw -> mch
snp OR mnh -> z15
ksm AND fcv -> z34
gsg AND twm -> nfb
x04 XOR y04 -> jkv
y27 XOR x27 -> jdw
mkc XOR vnn -> z28
y25 XOR x25 -> psh
rjb OR tqc -> dwm
sjk XOR btt -> z26
fcw OR nsq -> fjh
y37 XOR x37 -> wqv
y41 AND x41 -> bck
y02 XOR x02 -> pfd
dcn AND gjd -> rjb
y40 AND x40 -> rcb
jhj AND tqk -> khc
fsh XOR rfw -> z22
y22 XOR x22 -> rfw
fng OR gmg -> qcf
hqj OR pct -> khs
fjh XOR sbs -> z20
y17 XOR x17 -> ckk
y07 XOR x07 -> gsg
fpk AND bkq -> wmm
mch AND hwf -> nsq
x20 AND y20 -> frw
whb OR jbc -> jvv
mch XOR hwf -> z19
bbr XOR rsj -> z41
kgq OR ttq -> hdt
jjs OR nbd -> gjd
x38 AND y38 -> cjr
y39 AND x39 -> bct
chn AND gfd -> prp
wrk AND dwm -> hjm
ckk AND msb -> fng
sms XOR khs -> z32
y37 AND x37 -> nss
bwv OR qwt -> ksm
fjh AND sbs -> pvq
ksm XOR fcv -> cqk
x18 AND y18 -> hpw
cqp AND psh -> fvv
pvq OR frw -> nsp
fcc OR npd -> hmn
y27 AND x27 -> pks
kpp AND tmr -> fcc
fpb OR nfb -> sgm
x41 XOR y41 -> rsj
wdg AND nsj -> wkh
y28 AND x28 -> nbd
pks OR cfb -> mkc
y23 AND x23 -> pmj
msb XOR ckk -> z17
tqh AND nsp -> vqn
chp OR cjr -> pjj
hgm AND jvd -> kpt
x15 AND y15 -> mnh
nmb AND pjs -> jbc
bbt AND bjr -> chp
jdw XOR fpp -> z27
x01 XOR y01 -> kgn
x16 XOR y16 -> cbg
wjj XOR gpv -> z05
bjr XOR bbt -> z38
cbg XOR fph -> z16
hbq OR qkf -> gpr
grk XOR gpr -> z33
sjq XOR tkg -> z09
hdt AND wcc -> qbr"""

inputb = inputb.splitlines()


#The question is very wordy, basically we're simulating basic logic gates, but also the layout of the question breaks my brain a bit

## in order to be able to simulate the gates waiting i'd need to set the gates up first I think?

## each wire should be a key, and it's value should be the value,

## then each gate should also be a key in another structure?

#ops = {
#    'AND': &,
#    'OR': |,
#    'XOR': ^
#}

## leaving house for xmas soon

def doOp(a, op, b, c, gate):
    if op == 'XOR':
        wires[c] = int(wires[a]) ^ int(wires[b])
        print(f"{wires[a]} {op} {wires[b]} = {wires[c]} output to {c}")
    elif op == 'OR':
        wires[c] = int(wires[a]) | int(wires[b])
        print(f"{wires[a]} {op} {wires[b]} = {wires[c]} output to {c}")
    elif op == 'AND':
        wires[c] = int(wires[a]) & int(wires[b])
        print(f"{wires[a]} {op} {wires[b]} = {wires[c]} output to {c}")
    # Mark the gate as processed
    gate[5] = True



gates = []
wires = {}

for wire in inputa:
    line = wire.split(': ')
    wires[line[0]] = line[1]

##gate initialization
for gate in inputb:
    gate = gate.split(' ') ### not sure if best to split here or have this as the whole key
    gate.append(False)
    gates.append(gate)
    if wires.get(gate[0]) is None:
        wires[gate[0]] = None
    if wires.get(gate[2]) is None:
        wires[gate[2]] = None
    if wires.get(gate[4]) is None:
        wires[gate[4]] = None
    

def timetick(gates):
    actioned = 0
    for gate in gates:
        if not gate[5]:  # Only process unresolved gates
            if wires.get(gate[0]) is not None and wires.get(gate[2]) is not None:
                # Perform operation and update the gate status
                doOp(gate[0], gate[1], gate[2], gate[4], gate)
    # Count unresolved gates
    for gate in gates:
        if gate[5]:
            actioned += 1
    return len(gates) - actioned  # Gates left to resolve        


# Simulate until all gates are resolved
while timetick(gates) > 0:
    pass

# Final state of wires
print("Final Wires State:")
for wire, value in wires.items():
    print(f"{wire}: {value}")


# Final state of Zwires
binary = ""
print("Final ZWires State:")
for wire in sorted(wires.keys()):
    if wire[0] == 'z':
        print(f"{wire}: {wires[wire]}")
        binary+=(str(wires[wire]))
print(binary)

print(int(binary, 2))