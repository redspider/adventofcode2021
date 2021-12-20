import copy
import itertools
from collections import namedtuple
import numpy as np

INPUT = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""


INPUT = open('19.input').read()

beacon_sets = []

Point = namedtuple('Point', ['x','y','z'])

Matrix = namedtuple('Matrix', ['x1','y1','z1','x2','y2','z2','x3','y3','z3'])


def sub_point(a, b):
    return Point(a.x - b.x, a.y - b.y, a.z - b.z)

def add_point(a, b):
    return Point(a.x + b.x, a.y + b.y, a.z + b.z)

for line in INPUT.split("\n"):
    line = line.strip()
    if not line:
        continue
    if line.startswith('---'):
        beacon_sets.append(set())
        continue
    beacon_sets[-1].add(Point(*map(int, line.split(','))))

rot = []

def print_matrix(m):
    for r in m:
        print(f"{r[0]:<3}{r[1]:<3}{r[2]:<3}")
    print()

for x in range(0, 3):
    for xs in [1, -1]:
        for y in range(0, 3):
            for ys in [1, -1]:
                for z in range(0, 3):
                    for zs in [1, -1]:
                        if x != y and y != z and x != z:
                            r = [0] * 9
                            r[x * 3] = xs
                            r[y * 3 + 1] = ys
                            r[z * 3 + 2] = zs
                            rot.append(
                                Matrix(*r)
                            )

print(len(set(rot)))


def matrix_multiply(a, m):
    return Point(
        sum([a[0] * m.x1, a[1] * m.x2, a[2] * m.x3]),
        sum([a[0] * m.y1, a[1] * m.y2, a[2] * m.y3]),
        sum([a[0] * m.z1, a[1] * m.z2, a[2] * m.z3]),
    )

assert matrix_multiply(Point(5,4,3), rot[0]).x == 5
assert matrix_multiply(Point(5,4,3), rot[1]).z == -3


def find_overlap(a: set, b: set):
    # For every point in a
    for ap in a:
        # for every rotation of b
        for r in rot:
            br = set(
                matrix_multiply(p, r) for p in b
            )
            # For every point in b
            for bp in br:
                # Assume bp = ap, find the offset between them
                offset = sub_point(ap, bp)

                # Transform b to the a coordinate frame
                tb = set()
                for p in br:
                    tb.add(add_point(offset, p))

                # Look for an intersection of 12 or more
                if len(a.intersection(tb)) >= 12:
                    # Return the offset and rotation
                    return offset, r, tb
    return None


current = beacon_sets.pop()



scanners = []

while beacon_sets:
    for i, bs in enumerate(list(beacon_sets)):
        result = find_overlap(current, bs)
        if result:
            beacon_sets.remove(bs)
            offset, r, tb = result
            print(offset)
            current = current.union(tb)
            scanners.append(offset)

print("Part 1:", len(current))

distance = 0

for p1, p2 in itertools.permutations(scanners, 2):
    d = abs(p2.x-p1.x)+abs(p2.y-p1.y)+abs(p2.z-p1.z)
    if d > distance:
        distance = d


print("Part 2:", distance)