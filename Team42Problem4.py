def factors(num):
    factors = []
    for i in range(num + 1):
        for j in range(num + 1):
            if i * j == num:
                factors.append(i)
    return factors


def gcd(n1, n2, n3):
    n1_divs = factors(n1)
    n2_divs = factors(n2)
    n3_divs = factors(n3)

    cds = []

    for a in n1_divs:
        for b in n2_divs:
            for c in n3_divs:
                if a == b and b == c:
                    cds.append(a)

    return cds[-1]


def lth(triple):
    triple = triple[0]
    if triple[0] > triple[1] or triple[0] > triple[2] or triple[1] > triple[2]:
        return False
    return True


count = int(input())
numbers = [int(i) for i in input().split(" ")]

triples = []

for index, item in enumerate(numbers):
    for index2, item2 in enumerate(numbers):
        if index == index2:
            continue
        for index3, item3 in enumerate(numbers):
            if index2 == index3 or index == index3:
                continue
            triples.append((item, item2, item3))

triples = [(triple, gcd(triple[0], triple[1], triple[2])) for triple in triples]

triples = [triple for triple in triples if triple[1] == 1 and lth(triple)]


print(len(triples))
