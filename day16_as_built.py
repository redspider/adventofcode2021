
MAP = {
'0': '0000',
'1': '0001',
'2': '0010',
'3': '0011',
'4': '0100',
'5': '0101',
'6': '0110',
'7': '0111',
'8': '1000',
'9': '1001',
'A': '1010',
'B': '1011',
'C': '1100',
'D': '1101',
'E': '1110',
'F': '1111',
}

INPUT = """9C0141080250320F1802104A08"""

INPUT = open('16.input').read()

TYPE_LITERAL = 4
TYPE_SUM = 0
TYPE_PRODUCT = 1
TYPE_MIN = 2
TYPE_MAX = 3
TYPE_GT = 5
TYPE_LT = 6
TYPE_EQ = 7

versions = 0

def parse(br):
    global versions
    (n, remaining) = (br[:3], br[3:])
    version = int(n, 2)
    (n, remaining) = (remaining[:3], remaining[3:])
    type = int(n, 2)

    versions += version

    if type == TYPE_LITERAL:
        found_last = False
        value = ""
        while not found_last:
            (segment, remaining) = (remaining[:5], remaining[5:])
            if segment[0] == '0':
                found_last = True
            value += segment[1:]
        return (version, TYPE_LITERAL, int(value, 2), remaining)
    else:
        # Operator type
        (n, remaining) = (remaining[0], remaining[1:])
        length_type = n
        if length_type == '0':
            (n, remaining) = (remaining[:15], remaining[15:])
            length_bits = int(n, 2)
        else:
            (n, remaining) = (remaining[:11], remaining[11:])
            length_packets = int(n, 2)

        sub_packets = []
        count_packets = 0
        count_bits = 0
        while remaining and '0'*len(remaining) != remaining:
            if length_type == '1' and count_packets >= length_packets:
                break
            if length_type == '0' and count_bits >= length_bits:
                break
            count_packets += 1
            pre_count = len(remaining)
            result = parse(remaining)
            remaining = result[-1]
            count_bits += pre_count - len(remaining)
            sub_packets.append(result)


        if type == TYPE_SUM:
            return (version, TYPE_SUM, sum(r[2] for r in sub_packets), remaining)
        elif type == TYPE_PRODUCT:
            v = sub_packets[0][2]
            for p in sub_packets[1:]:
                v = v * p[2]
            return (version, TYPE_SUM, v, remaining)
        elif type == TYPE_MAX:
            return (version, TYPE_MAX, max(r[2] for r in sub_packets), remaining)
        elif type == TYPE_MIN:
            return (version, TYPE_MIN, min(r[2] for r in sub_packets), remaining)
        elif type == TYPE_GT:
            return (version, TYPE_GT, 1 if sub_packets[0][2] > sub_packets[1][2] else 0, remaining)
        elif type == TYPE_LT:
            return (version, TYPE_LT, 1 if sub_packets[0][2] < sub_packets[1][2] else 0, remaining)
        elif type == TYPE_EQ:
            return (version, TYPE_EQ, 1 if sub_packets[0][2] == sub_packets[1][2] else 0, remaining)

def pr(hr):
    return parse(''.join([MAP[c] for c in hr]))

print(pr('38006F45291200'))



assert pr('C200B40A82')[2] == 3
assert pr('04005AC33890')[2] == 54
assert pr('880086C3E88112')[2] == 7
assert pr('CE00C43D881120')[2] == 9
assert pr('D8005AC2A8F0')[2] == 1
assert pr('F600BC2D8F')[2] == 0
assert pr('9C005AC2F8F0')[2] == 0
assert pr('9C0141080250320F1802104A08')[2] == 1

print(pr(INPUT))
