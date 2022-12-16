import string
from functools import cmp_to_key


def parse_line(in_line, full_array=False):
    to_ret = []
    x = 0
    array_open_count = 0
    array_start = 0
    array_end = 0
    if len(in_line) == 0:
        return to_ret
    if in_line[0] == '[' and not full_array:
        # print(' look for array: ' + in_line)
        # array container parsing
        while x < len(in_line):
            if in_line[x] == '[':
                if array_open_count == 0:
                    array_start = x
                array_open_count += 1
            if in_line[x] == ']':
                array_open_count -= 1
                if array_open_count == 0:
                    array_end = x
                    array_string = in_line[array_start+1:array_end]
                    # print(' full array found: ' + array_string)
                    return parse_line(array_string, True)
            x += 1
    elif ',' in in_line or full_array: 
        # print(' naked array: ' + in_line)
        to_ret = []
        # assume we're in an array
        # we can't in_line.split(',') because nested arrays
        last_comma = 0
        while x < len(in_line):
            if in_line[x] == ',' and array_open_count == 0:
                item = in_line[last_comma: x]
                last_comma = x+1
                to_ret.append(parse_line(item))
            if in_line[x] == '[':
                if array_open_count == 0:
                    array_start = x
                array_open_count += 1
            if in_line[x] == ']':
                array_open_count -= 1
                if array_open_count == 0:
                    array_end = x
                    array_string = in_line[array_start+1:array_end]
                    # print(' sub array found: ' + array_string)
            x += 1
        item = in_line[last_comma: x]
        to_ret.append(parse_line(item))
        return to_ret
    elif ',' not in in_line and full_array:
        # print(' parse again as a non-array: ' + in_line)
        return parse_line(in_line)
    else:
        if full_array:
            return [int(in_line)]
        # print(' number: ' + in_line)
        return int(in_line)



def get_signal():
    pairs = []
    f = open('input.txt')
    lines = f.readlines()
    left = None
    right = None
    for l in lines:
        line = l.strip().replace('\n', '')
        if left == None:
            left = parse_line(line)
        elif right == None:
            right = parse_line(line)
        else: 
            pairs.append([left, right])
            left = None
            right = None
    pairs.append([left, right])
    return pairs


def count_sum_of_indices(indices):
    sum = 0
    for i in indices:
        sum += i
    return sum 

def print_d(stmt, debug):
    if debug:
        print(stmt) 


# conclusion can either be "in order", "out of order", or "inconclusive" 

# If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
# If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
# If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
def is_in_right_order(left, right, debug):
    conclusion = 0 # 'inconclusive'
    if isinstance(left, int) or isinstance(right, int):
        print('ERROR: Neither left nor right should be ints')
        return -100
    elif isinstance(left, list) and isinstance(left, list):
        # both are lists, so iterate
        x = 0 
        max_x = max(len(left),len(right))
        while conclusion == 0 and x < max_x:
            left_val = None
            if x < len(left):
                left_val = left[x]
            right_val = None
            if x < len(right):
                right_val = right[x]  
            if left_val is None:
                print_d('left list ran out first: in order', debug)
                # If the left list runs out of items first, the inputs are in the right order.
                conclusion = 1 # 'in order'
            elif right_val is None:
                print_d('right list ran out first: out of order', debug)
                #  If the right list runs out of items first, the inputs are not in the right order.
                conclusion = -1 # 'out of order'
            elif left_val is not None and right_val is not None:
                # print_d('comparing non-none values: ' + str(left_val) + ', ' + str(right_val), debug)
                if isinstance(left_val, int) and isinstance(right_val, int):
                    # print_d(str(left_val) + ' compare ' + str(right_val), debug)
                    if left_val < right_val:
                        conclusion = 1 # 'in order'
                    elif left_val > right_val:
                        conclusion = -1 # 'out of order'
                    else: 
                        conclusion = 0
                elif isinstance(left_val, list) and isinstance(right_val, int):
                    # print_d(' cast ' + str(right_val) + ' to list', debug)
                    conclusion = is_in_right_order(left_val, [right_val], debug)
                elif isinstance(left_val, int) and isinstance(right_val, list):
                    # print_d(' cast ' + str(left_val) + ' to list', debug)
                    conclusion = is_in_right_order([left_val], right_val, debug)
                elif isinstance(left_val, list) and isinstance(right_val, list):
                    # print_d(' compare lists ' + str(left_val) + ' and ' + str(right_val), debug)
                    conclusion = is_in_right_order(left_val, right_val, debug)
            # If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
            x += 1
        print_d(' loop ended ' + str(left) + ' and ' + str(right) + ':' +  str(conclusion), debug)
        return conclusion
    elif isinstance(left, list):
        # cast to lists and iterate
        print_d(' cast ' + str(right) + ' to list and iterate', debug)
        return is_in_right_order(left, [right], debug)
    else:
        # cast to lists and iterate
        print_d(' cast ' + str(left) + ' to list and iterate', debug)
        return is_in_right_order([left], right, debug)


def day13_part1():
    signal_pairs = get_signal()
    indices = []
    pairs = 0
    for [left, right] in signal_pairs:
        pairs += 1
        print('comparing pair # ' + str(pairs))
        print(left)
        print(right)
        if is_in_right_order(left, right, True) == 1:
            print('pair in right order: # ' + str(pairs))
            indices.append(pairs) 
    print(count_sum_of_indices(indices))



def compare(x, y):
    return is_in_right_order(x, y, False)


# locate indices of divider packets
# order all signals
def day13_part2():
    signal_pairs = get_signal()
    all_messages = [] 
    for pair in signal_pairs:
        all_messages.extend(pair)
    
    all_messages.append([[2]])
    all_messages.append([[6]])

    print('all_messages')
    for m in all_messages:
        print(str(m))

    print('\nwhen sorted')
    sorted_messages = sorted(all_messages, key=cmp_to_key(compare), reverse=True)
    sorted_messages_strings = []
    for m in sorted_messages:
        print(str(m))
        sorted_messages_strings.append(str(m))
    first_index= sorted_messages_strings.index('[[2]]') + 1
    second_index= sorted_messages_strings.index('[[6]]') + 1
    print('\n[[2]] : ' + str(first_index))
    print('[[6]] : ' + str(second_index))
    print('decoder key: ' + str(first_index * second_index))




day13_part2()