import math, sys
sys.set_int_max_str_digits(100000000)

def get_monkeys():
    monkeys = {}
    f = open('input.txt')
    lines = f.readlines()
    current_monkey_name = -1
    for l in lines:
        line_arr = l.strip().replace('\n', '').split(' ')
        # noop takes one cycle to complete. It has no other effect.
        if line_arr[0] == 'Monkey':
            current_monkey_name = int(line_arr[1].replace(':', ''))
            monkeys[current_monkey_name] = { 'name': current_monkey_name, 'inspection_count': 0 }
        elif line_arr[0] == 'Starting':
            items = [int(i.replace(',', '')) for i in  line_arr[2:]]
            monkeys[current_monkey_name]['items'] = items
        elif line_arr[0] == 'Operation:':
            monkeys[current_monkey_name]['operation'] = {
                'left': line_arr[1:][2],
                'op': line_arr[1:][3],
                'right': line_arr[1:][4],
            }
        elif line_arr[0] == 'Test:':
            divisible_by = int(line_arr[3])
            monkeys[current_monkey_name]['test_divisible_by'] = divisible_by
        elif line_arr[0] == 'If' and line_arr[1] == 'true:':
            monkeys[current_monkey_name]['if_true'] = int(line_arr[5])
        elif line_arr[0] == 'If' and line_arr[1] == 'false:':
            monkeys[current_monkey_name]['if_false'] = int(line_arr[5])
    return monkeys

def get_worry_level_part1(item_worry_level, operation):
    left = 0
    right = 0
    new_worry_level = 0
    # Operation shows how your worry level changes as that monkey inspects an item. 
    if operation['left'] == 'old':
        left = item_worry_level
    else: 
        left = int(operation['left'])
    if operation['right'] == 'old':
        right = item_worry_level
    else: 
        right = int(operation['right'])
    if operation['op'] == '*':
        new_worry_level = left * right
    elif operation['op'] == '+': 
        new_worry_level = left + right
    else:
        print('bad monkey, unhandled operator')
    # After each monkey inspects an item but before 
    # it tests your worry level, your relief that the monkey's
    #  inspection didn't damage the item causes your worry level
    #  to be divided by three and rounded down to the nearest integer.
    return math.floor(new_worry_level / 3)

# Test shows how the monkey uses your worry level to decide where to throw an item next.
def get_next_monkey(item_worry_level, current_monkey):
    if item_worry_level % current_monkey['test_divisible_by'] == 0:
        return int(current_monkey['if_true'])
    return int(current_monkey['if_false'])
        
def get_monkey_business(monkeys):
    i_counts = [monkeys[m]['inspection_count'] for m in monkeys.keys()]
    i_counts.sort()
    i_counts.reverse()
    total_monkey_business = i_counts[0] * i_counts[1]
    print(total_monkey_business)


def day11_part1():
    monkeys = get_monkeys()
    # Chasing all of the monkeys at once is impossible; 
    # you're going to have to focus on the two most active monkeys 
    # if you want any hope of getting your stuff back. 
    # Count the total number of times each monkey inspects items 
    # over 20 rounds:
    for monkey_round in range(0, 20):
        print('******* ROUND ' + str(monkey_round) + ' *******')
        # the process of each monkey taking a single turn is called a round
        # starts with monkey 0
        for current_monkey in monkeys.keys():
            m = monkeys[current_monkey]
            print(' MONKEY ' + str(current_monkey) + ' inspects ' + str(len(m['items'])) + ' items')
            items = [i for i in m['items']]
            items.reverse()
            m['items'] = []
            while len(items) > 0:
                item = items.pop()
                # print('  monkey looks at item with worry level ' + str(item))
                m['inspection_count'] += 1 
                worry_level = get_worry_level_part_1(item, m['operation'])
                # print('  item new worry level ' + str(worry_level))
                next_monkey_name = get_next_monkey(worry_level, m)
                next_monkey = monkeys[next_monkey_name]
                next_monkey['items'].append(worry_level)
                # print('  throw to -> ' + str(next_monkey_name))
    total_monkey_business = get_monkey_business(monkeys)


def get_worry_level_part2(item_worry_level, operation, common_maximum):
    left = 0
    right = 0
    new_worry_level = 0
    # Operation shows how your worry level changes as that monkey inspects an item. 
    if operation['left'] == 'old':
        left = item_worry_level
    else: 
        left = int(operation['left'])
    if operation['right'] == 'old':
        right = item_worry_level
    else: 
        right = int(operation['right'])
    if operation['op'] == '*':
        new_worry_level = left * right
    elif operation['op'] == '+':
        new_worry_level = left + right
    else:
        print('bad monkey, unhandled operator')
    print('new_worry_level: ' + str(new_worry_level))
    return new_worry_level % common_maximum


def get_common_maximum(monkeys):
    common = 1
    for m in monkeys.keys():
        current_monkey = monkeys[m]
        common = common * current_monkey['test_divisible_by']
    return common

def day11_part2():
    monkeys = get_monkeys()
    common_maximum = get_common_maximum(monkeys)
    # Chasing all of the monkeys at once is impossible; 
    # you're going to have to focus on the two most active monkeys 
    # if you want any hope of getting your stuff back. 
    # Count the total number of times each monkey inspects items 
    # over 20 rounds:
    for monkey_round in range(0, 10000):
        print('******* ROUND ' + str(monkey_round) + ' *******')
        # the process of each monkey taking a single turn is called a round
        # starts with monkey 0
        for current_monkey in monkeys.keys():
            m = monkeys[current_monkey]
            print(' MONKEY ' + str(current_monkey) + ' inspects ' + str(len(m['items'])) + ' items')
            items = [i for i in m['items']]
            items.reverse()
            m['items'] = []
            while len(items) > 0:
                item = items.pop()
                # print('  monkey looks at item with worry level ' + str(item))
                m['inspection_count'] += 1 
                worry_level = get_worry_level_part2(item, m['operation'], common_maximum)
                # print('  item new worry level ' + str(worry_level))
                next_monkey_name = get_next_monkey(worry_level, m)
                next_monkey = monkeys[next_monkey_name]
                next_monkey['items'].append(worry_level)
                # print('  throw to -> ' + str(next_monkey_name))
    total_monkey_business = get_monkey_business(monkeys)

day11_part2()