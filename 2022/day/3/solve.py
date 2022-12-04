def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def inputToArray(should_split = False):
    f = open('input.txt')
    lines = f.readlines()
    # Each rucksack has two large compartments.
    #  All items of a given type are meant to go into exactly one of the two compartments.
    rucksacks = []
    for l in lines:
        print(l)
        # The list of items for each rucksack is given as characters all on a single line. 
        # A given rucksack always has the same number of items in each of its two compartments, 
        # so the first half of the characters represent items in the first compartment, 
        # while the second half of the characters represent items in the second compartment.
        items = l.replace('\n', '')
        if should_split:
            compartmentA, compartmentB = split_list(items)
            rucksacks.append([compartmentA, compartmentB])
        else: 
            rucksacks.append(items)
    return rucksacks

# The Elf that did the packing failed to follow 
# this rule for exactly one item type per rucksack.
def find_shared_item(left, right):
    for l in left:
        if l in right:
            return l
    return None

abcABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Every item type can be converted to a priority:
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
def item_priority(i):
    return abcABC.index(i) + 1

def day3_part1():
    rucksacks = inputToArray()
    #  What is the sum of the priorities of those moved item types?
    sum = 0
    for r in rucksacks:
        [left, right] = r
        sum = sum + (item_priority(find_shared_item(left, right)))
    print(sum)

def find_badges(first, second, third):
    for l in first:
        if l in second and l in third:
            return l
    return None
            
# cluster rucksacks into groups of three 
def make_triplets(array):
    triplets = []
    triplet = []
    for a in array:
        triplet.append(a)
        if len(triplet) == 3:
            triplets.append(triplet)
            triplet = []
    return triplets


def day3_part2():
    rucksacks = inputToArray(False)
    triplets = make_triplets(rucksacks)
    #  What is the sum of the priorities of those moved item types?
    sum = 0
    for t in triplets:
        [first, second, third] = t
        b = find_badges(first, second, third)
        print(b)
        sum = sum + item_priority(b)
    print(sum)


day3_part2()