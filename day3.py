test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split('\n')

# Build a dictionary so we can "look up" the priority of a given character.
# A dictionary stores key:value pairs.
# You get the value associated with a key with square brackets
# So for instance, priority_dict['A'] would return a value of 27.

lc = 'abcdefghijklmnopqrstuvwxyz'
priority_dict = {}

# Put the lower case priorities to the dictionary.
for i, char in enumerate(lc):
    priority_dict[char] = i + 1

# Put the upper case priorities in the dictionary.
for i, char in enumerate(uc.upper()):
    priority_dict[char] = i + 27

# A running total for the priority values
total = 0

for line in test_input:
    # How long is the line?
    line_len = len(line)
    if line_len % 2 != 0:
        raise ValueError('Uh oh, odd number of characters')
    # The length of a compartment is half the length of the line.
    # In modern python, division returns a float, we need an integer, so use //
    len_comp = line_len // 2

    # The first "compartment"
    comp1 = line[:len_comp]

    # The second "compartment"
    comp2 = line[-len_comp:]

    # Turn the compartments into sets.
    # Sets provide fast, consise ways of looking for duplicates.
    set1 = set(comp1)
    set2 = set(comp2)

    # The set method "intersection" returns the elements common to both sets.
    isect = set1.intersection(set2)

    # isect is itself a set.
    # It's slightly less straight forward to get the element of the set.
    # Sets are unordered, so we can't get isect[0].
    # But since it's only a single element, convert it to a list and then
    # get element 0 of that.
    duplicate = list(isect)[0]

    # Now look up the priority of the duplicate character
    priority = priority_dict[duplicate]

    total += priority

print(total)
