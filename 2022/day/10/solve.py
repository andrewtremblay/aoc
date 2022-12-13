import math


def get_series_of_instructions():
    ins = []
    f = open('input.txt')
    lines = f.readlines()
    for l in lines:
        line_arr = l.replace('\n', '').split(' ')
        # noop takes one cycle to complete. It has no other effect.
        if line_arr[0] == 'noop':
            ins.append([1, 0, 'noop'])
        elif line_arr[0] == 'addx':
            # addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
            ins.append([2, int(line_arr[1]), l.replace('\n', '')])
    return ins

cycle_values = { 
    20: None,
    60: None, 
    100: None, 
    140: None, 
    180: None, 
    220: None, 
}

def day10_part1():
    instructions = get_series_of_instructions()
    cycles = 0
    x = 1 # starts with the value 1
    for i in instructions:
        cycles += i[0]
        old_x = x
        x += i[1]
        print(i[2])
        print('value at cycle ' + str(cycles) + ': ' + str(x) + ' (was ' + str(old_x) + ')' )
        for c in cycle_values.keys():
            if cycle_values[c] == None:
                if cycles > c:
                    cycle_values[c] = old_x * c
                    print(str(old_x) + ' * ' + str(c) + ' ±= ' + str(cycle_values[c]))
                elif cycles == c:
                    cycle_values[c] = old_x * c
                    print(str(old_x) + ' * ' + str(c) + ' = ' + str(cycle_values[c]))
    sum_vals = 0
    for c in cycle_values.keys():
        sum_vals += cycle_values[c]
    print(sum_vals) # 13180

def debug_crt(crt):
    start = ''
    for row in crt:
        start += ''.join(row) + '\n'
    print(start)


def day10_part2():
    instructions = get_series_of_instructions()
    CRT_ROW = list('.' * 40)
    CRT = [CRT_ROW.copy(), CRT_ROW.copy(), CRT_ROW.copy(), CRT_ROW.copy(), CRT_ROW.copy(), CRT_ROW.copy()]
    debug_crt(CRT)
    sprite_pos = 1 # starts with the value 1
    pixel_index = 0
    cycle = 1
    sprite_index_range = [sprite_pos - 1, sprite_pos, sprite_pos + 1]
    print('starting sprite pos: [' + ', '.join(str(i) for i in sprite_index_range) + ']') 
    # cycles from instructions
    for i in instructions:
        sprite_index_range = [sprite_pos - 1, sprite_pos, sprite_pos + 1]
        print('begin executing ' + i[2]) 
        for j in range(0, i[0]):
            print(' cycle ' + str(cycle) + ':')
            # print('  pixel_index ' + str(pixel_index))
            pixel_x_pos = pixel_index % 40
            pixel_y_pos = math.floor(pixel_index / 40)
            # print('  check pixel: (' + str(pixel_x_pos) + ',' + str(pixel_y_pos) + ')')
            if pixel_x_pos in sprite_index_range:
                print('**  SPRITE HIT: (' + str(pixel_x_pos) + ' in [' + ', '.join(str(i) for i in sprite_index_range) + ']) **')
                CRT[pixel_y_pos][pixel_x_pos] = '#'
            # print('  row ' + str(pixel_y_pos) + ': ' + ''.join(CRT[pixel_y_pos][0:pixel_x_pos+1]))
            pixel_index += 1
            cycle += 1
            debug_crt(CRT)
        sprite_pos += i[1]
        sprite_index_range = [sprite_pos - 1, sprite_pos, sprite_pos + 1]
        # print('finished executing ' + i[2] + ': Register X is now '+ str(sprite_pos))
        # print('[' + ', '.join(str(i) for i in sprite_index_range) + ']') 
    debug_crt(CRT)

day10_part2()