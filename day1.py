
test_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".split('\n')


def solve(input):
    # Remove the end-line characters and any white space from the lines in the input.
    lines = [line.strip() for line in input]

    # Used to store the running total number of calories for the current elf.
    current_total = 0

    # This is a list, we'll store the totals for each elf here.
    calorie_totals = []

    for i in range(len(lines)):
        if len(lines[i]) == 0:
            # This is a blank line. Append the current total to the list and reset it to zero.
            calorie_totals.append(current_total)
            current_total = 0
        else:
            # This line must contain a number
            current_total += int(lines[i])

    # Now find the index associated with the biggest value in calorie totals
    # Enumerate is a function that gives us two things (a counter, and the value) for each value in a list.
    max_cals = -1  # store the largest number of calories found so far
    max_elf = -1  # store the number of the elf with those calories (remember i starts at 0)

    for i, calories in enumerate(calorie_totals):
        if calories > max_cals:
            max_cals = calories
            max_elf = i + 1

    print('Part 1:')
    print(max_elf, max_cals)

    # For part 2, well just sort the list of calorie_totals, and sum the last 3 elements
    print('Part 2:')
    print(sum(sorted(calorie_totals)[-3:]))


if __name__ == '__main__':
    print('--- TEST ---')
    solve(test_data)

    print('--- SOLUTION ---')
    with open('day1.in') as f:
        input = f.readlines()
    solve(input)
