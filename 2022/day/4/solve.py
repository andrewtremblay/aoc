# 2-4 -> [2, 4]
def numericAssignment(elf):
    [left, right] = elf.split('-')
    return [int(left), int(right)]

def inputToArray():
    f = open('input.txt')
    lines = f.readlines()
    # Each rucksack has two large compartments.
    #  All items of a given type are meant to go into exactly one of the two compartments.
    assignments = []
    for l in lines:
        # 2-4,6-8
        [elf1, elf2] = l.replace('\n', '').split(',')
        # .234.....  2-4
        # .....678.  6-8
        assignments.append([numericAssignment(elf1), numericAssignment(elf2)]) 
        # [[elf1Left, elf1Right],[elf2Left, elf2Right]]
    return assignments

def assignments_fully_overlap(elf1, elf2):
    [elf1Left, elf1Right] = elf1 
    [elf2Left, elf2Right] = elf2 
    # elf1 inside elf2 
    if elf1Left >= elf2Left and elf1Right <= elf2Right:
        return True
    # elf2 inside elf1 
    if elf2Left >= elf1Left and elf2Right <= elf1Right:
        return True
    return False

def day4_part1():
    assignments = inputToArray()
    #  What is the sum of the assignments that perfectly overlap?
    sum = 0
    for a in assignments:
        [elf1, elf2] = a
        if assignments_fully_overlap(elf1, elf2):
            sum = sum + 1
    print(sum)

def assignments_overlap_at_all(elf1, elf2):
    [elf1Left, elf1Right] = elf1 
    [elf2Left, elf2Right] = elf2 
    if assignments_fully_overlap(elf1, elf2):
        return True
    # check left side of elf 1 boundary 
    if elf1Left >= elf2Left and elf1Left <= elf2Right:
        return True
    # check right side of elf 1 boundary 
    if elf1Right >= elf2Left and elf1Right <= elf2Right:
        return True
    return False


def day4_part2():
    assignments = inputToArray()
    #  What is the sum of the assignments that perfectly overlap?
    sum = 0
    for a in assignments:
        [elf1, elf2] = a
        if assignments_overlap_at_all(elf1, elf2):
            sum = sum + 1
    print(sum)

day4_part2()