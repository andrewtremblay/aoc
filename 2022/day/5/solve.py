# move 1 from 2 to 1
# move 3 from 3 to 2
def adjustStacks(stacks, sourceIndex, destIndex, count):
    if count == 0:
        return stacks
    source_stack = stacks[sourceIndex]
    dest_stack = stacks[destIndex]
    new_stacks = stacks
    item = source_stack.pop()
    dest_stack.append(item)
    new_stacks[sourceIndex] = source_stack
    new_stacks[destIndex] = dest_stack
    return adjustStacks(new_stacks, sourceIndex, destIndex, count - 1)

def adjustStacksMultiple(stacks, sourceIndex, destIndex, amount):
    source_stack = stacks[sourceIndex]
    dest_stack = stacks[destIndex]
    new_stacks = stacks
    items = [] 
    i = 0
    while i < amount:
        item = source_stack.pop()
        items.append(item)
        i += 1 
    dest_stack.extend(reversed(items))
    new_stacks[sourceIndex] = source_stack
    new_stacks[destIndex] = dest_stack
    return new_stacks

def topStacks(stacks):
    toRet = ''
    for s in stacks:
        if len(s) > 0:
            toRet = toRet + s[-1]
    return toRet


def inputToArray():
    f = open('input.txt')
    lines = f.readlines()
    # Each rucksack has two large compartments.
    #  All items of a given type are meant to go into exactly one of the two compartments.
    movements = []
    # move 1 from 2 to 1
    # move 3 from 3 to 2
    for l in lines:
        # move 1 from 2 to 1
        [_, moveStr, _, sourceStr, _, destStr] = l.replace('\n', '').split(' ')
        # sourceIndex, destIndex, count
        movements.append([int(sourceStr), int(destStr), int(moveStr)]) 
    return movements

# [T] [V]                     [W]    
# [V] [C] [P] [D]             [B]    
# [J] [P] [R] [N] [B]         [Z]    
# [W] [Q] [D] [M] [T]     [L] [T]    
# [N] [J] [H] [B] [P] [T] [P] [L]    
# [R] [D] [F] [P] [R] [P] [R] [S] [G]
# [M] [W] [J] [R] [V] [B] [J] [C] [S]
# [S] [B] [B] [F] [H] [C] [B] [N] [L]
#  1   2   3   4   5   6   7   8   9 



initial_state = [[], # empty zero index
['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T'],
['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V'],
['B', 'J', 'F', 'H', 'D', 'R', 'P'],
['F', 'R', 'P', 'B', 'M', 'N', 'D'],
['H', 'V', 'R', 'P', 'T', 'B'],
['C', 'B', 'P', 'T'],
['B', 'J', 'R', 'P', 'L'],
['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W'],
['L', 'S', 'G']
]


def day5_part1():
    movements = inputToArray()
    #  What is the sum of the assignments that perfectly overlap?
    crates = []
    for m in movements:
        [source, dest, move_count] = m
        crates = adjustStacks(initial_state, source, dest, move_count)
    print(topStacks(crates))

def day5_part2():
    movements = inputToArray()
    #  What is the sum of the assignments that perfectly overlap?
    crates = []
    for m in movements:
        [source, dest, move_count] = m
        crates = adjustStacksMultiple(initial_state, source, dest, move_count)
    print(topStacks(crates))

day5_part2()