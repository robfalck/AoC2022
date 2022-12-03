
test_input = ['A Y', 'B X', 'C Z']


def process_line(them, us):

    if them == 'A' and us == 'X':
        return 3 + 1
    elif them == 'A' and us == 'Y':
        return 6 + 2
    elif them == 'A' and us == 'Z':
        return 0 + 3
    elif them == 'B' and us == 'X':
        return 0 + 1
    elif them == 'B' and us == 'Y':
        return 3 + 2
    elif them == 'B' and us == 'Z':
        return 6 + 3
    elif them == 'C' and us == 'X':
        return 6 + 1
    elif them == 'C' and us == 'Y':
        return 0 + 2
    elif them == 'C' and us == 'Z':
        return 3 + 3
    else:
        print("uh oh")
        print(us, them)
        exit(0)

def process_line2(them, us):

    if them == 'A' and us == 'X':
        # we need to throw scissors
        return 0 + 3
    elif them == 'A' and us == 'Y':  #
        # we need to throw rock
        return 3 + 1
    elif them == 'A' and us == 'Z':
        # we throw paper
        return 6 + 2
    elif them == 'B' and us == 'X':  #
        # we throw rock
        return 0 + 1
    elif them == 'B' and us == 'Y':
        # we throw paper
        return 3 + 2
    elif them == 'B' and us == 'Z':
        # we throw scissors
        return 6 + 3
    elif them == 'C' and us == 'X':
        # we throw paper
        return 0 + 2
    elif them == 'C' and us == 'Y':
        # we throw scissors
        return 3 + 3
    elif them == 'C' and us == 'Z': #
        # we throw rock
        return 6 + 1
    else:
        print("uh oh")
        print(us, them)
        exit(0)


def solve1(input):
    total = 0
    for line in input:
        us, them = line
        score = process_line(us, them)
        total = total + score
    print('--- PART 1 ---')
    print('   Total Score:', total)

def solve2(input):
    total = 0
    for line in input:
        us, them = line
        score = process_line2(us, them)
        total = total + score
    print('--- PART 2 ---')
    print('   Total Score:', total)


if __name__ == '__main__':

    TEST = True

    if TEST:
        with open('day2.in') as f:
            input = [line.split() for line in f.readlines()]
    else:
        input = [line.split() for line in test_input]

    solve1(input)
    solve2(input)
