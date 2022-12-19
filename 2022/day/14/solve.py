

def get_cave_walls():
    walls = []
    f = open('input.txt')
    lines = f.readlines()
    for l in lines:
        wall = []
        line = l.strip().replace('\n', '')
        points = line.split(' -> ')
        for p_raw in points:
            p = p_raw.split(',')
            # x and y coords to int
            wall.append([int(p[0]), int(p[1])])
        walls.append(wall)
    return walls


def debug_spaces(spaces):
    for sy in spaces:
        row = ''
        i = 0
        # the cave is mostly empty on the left
        left_clip = 450
        for sx in sy:
            if i > left_clip:
                row += sx
            i += 1
        print(row)


def get_cave():
    walls = get_cave_walls()
    # find boundaries of the cave
    max_x = 0
    max_y = 0
    for w in walls:
        for p in w:
            if p[0] > max_x:
                max_x = p[0]
            if p[1] > max_y:
                max_y = p[1]
    max_x += 1
    max_y += 1
    print('cave size: ' + str(max_x) + ' x ' + str(max_y + 1))
    spaces = []
    for y in range(0, max_y):
        space = []
        for x in range(0, max_x):
            space.append('.')
        spaces.append(space)
    print('spaces size: ' + str(len(spaces[0])) + ' x ' + str(len(spaces)))
    # walls are a chain of points in space, representing corners of the wall
    for w in walls:
        # all walls have at least two points
        last_p = w[0]
        i = 1
        while i < len(w):
            p = w[i] # next point
            add_wall(last_p, spaces)
            # walk between two points
            while pos_same(p, last_p) is False:
                if p[0] < last_p[0]:
                    last_p[0] -= 1
                if p[0] > last_p[0]:
                    last_p[0] += 1
                if p[1] < last_p[1]:
                    last_p[1] -= 1
                if p[1] > last_p[1]:
                    last_p[1] += 1
                # add a wall piece each step
                add_wall(last_p, spaces)
            # point to the next wall corner
            i += 1
    return [spaces, max_x, max_y]

# The sand is pouring into the cave from point 500,0.


def pos_same(a, b):
    return a[0] == b[0] and a[1] == b[1]

def is_in_bounds(pos, spaces):
    try: 
        spaces[pos[1]][pos[0]]
        return True
    except: 
        return False

def is_empty_space(pos, spaces):
    return spaces[pos[1]][pos[0]] == '.'

def delta_pos(pos, d):
    to_ret = pos.copy()
    to_ret[0] += d[0]
    to_ret[1] += d[1]
    return to_ret
    
below = [0, 1]
left = [-1, 0]
right = [1, 0]
lower_left = [-1, 1]
lower_right = [1, 1]


# returns [new_pos, True if we fell off]
def simulate_step(sand_pos, spaces):
    # A unit of sand always falls down one step if possible. 
    if is_in_bounds(delta_pos(sand_pos, below), spaces) is False:
        return [delta_pos(sand_pos, below), True]

    if is_empty_space(delta_pos(sand_pos, below), spaces):
        return [delta_pos(sand_pos, below), False]
    # If the tile immediately below is blocked (by rock or sand),
    #  the unit of sand attempts to instead move diagonally one step down and to the left. 
    if is_in_bounds(delta_pos(sand_pos, lower_left), spaces) is False:
        return [delta_pos(sand_pos, lower_left), True]

    if is_empty_space(delta_pos(sand_pos, lower_left), spaces):
        return [delta_pos(sand_pos, lower_left), False]
    
    
    # If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right.
    #  Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. 
    if is_in_bounds(delta_pos(sand_pos, lower_right), spaces) is False:
        return [delta_pos(sand_pos, lower_right), True]
    if is_empty_space(delta_pos(sand_pos, lower_right), spaces):
        return [delta_pos(sand_pos, lower_right), False]

    # If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, 
    # at which point the next unit of sand is created back at the source.
    return [sand_pos, False]

def add_wall(pos, spaces):
    # print('adding point : (' + str(pos[0]) + ', ' + str(pos[1]) + ')')
    if is_in_bounds(pos, spaces):
        spaces[pos[1]][pos[0]] = '#'
    else: 
        print('could not place wall: ')
        print('  spaces size: ' + str(len(spaces[0])) + ' x ' + str(len(spaces)))
        print('  too small for point in : (' + str(pos[0]) + ', ' + str(pos[1]) + ')')
    return spaces


def add_sand(pos, spaces):
    if is_in_bounds(pos, spaces):
        spaces[pos[1]][pos[0]] = '0'
    else: 
        print('could not place sand: ')
        print('  spaces size: ' + str(len(spaces[0])) + ' x ' + str(len(spaces)))
        print('  too small for point in : (' + str(pos[0]) + ', ' + str(pos[1]) + ')')
    return spaces

def day14_part1():
    [spaces, max_x, max_y] = get_cave()
    units_of_sand = 0
    fell_off = False
    sand_pos = [500, 0]
    while fell_off == False:
        [new_sand_pos, just_fell_off] = simulate_step(sand_pos, spaces)
        if just_fell_off: 
            print('just fell off: ' + str(new_sand_pos[0]) + ', ' + str(new_sand_pos[1]))
            fell_off = True
        if new_sand_pos[0] < 0 or new_sand_pos[0] > max_x:
            print('fell off left or right edge: ' + str(new_sand_pos[0]) + ' > ' + str(max_y))
            fell_off = True
        elif new_sand_pos[1] > max_y:
            print('fell off bottom edge: ' + str(new_sand_pos[1]) + ' > ' + str(max_x))
            fell_off = True
        elif pos_same(sand_pos, new_sand_pos):
            # print('drip: ' + str(sand_pos[0]) + ', ' + str(sand_pos[1]))
            # sand at rest, solidify
            spaces = add_sand(sand_pos, spaces)
            if sand_pos[0] == 500 and sand_pos[1] == 0:
                print('sand filled to the entry point ')
                fell_off = True
            # drop another sand
            new_sand_pos = [500, 0]
            units_of_sand += 1
        sand_pos = new_sand_pos
        if units_of_sand > 100000:
            print('too much sand: ')
            # debug
            fell_off = True

    print('spaces walked: ')
    debug_spaces(spaces)
    print('units of sand')
    print(str(units_of_sand))



# 1016

def get_cave_part_2():
    walls = get_cave_walls()
    # find boundaries of the cave
    max_x = 0
    max_y = 0
    for w in walls:
        for p in w:
            if p[0] > max_x:
                max_x = p[0]
            if p[1] > max_y:
                max_y = p[1]
    max_x += 1
    max_y += 1
    # add an arbitrarily large floor
    max_y += 2
    max_x = 1000
    walls.append([[0, max_y - 1],[max_x - 1, max_y  - 1]])
    print('cave size: ' + str(max_x) + ' x ' + str(max_y + 1))
    spaces = []
    for y in range(0, max_y):
        space = []
        for x in range(0, max_x):
            space.append('.')
        spaces.append(space)
    print('spaces size: ' + str(len(spaces[0])) + ' x ' + str(len(spaces)))
    # walls are a chain of points in space, representing corners of the wall
    for w in walls:
        # all walls have at least two points
        last_p = w[0]
        i = 1
        while i < len(w):
            p = w[i] # next point
            add_wall(last_p, spaces)
            # walk between two points
            while pos_same(p, last_p) is False:
                if p[0] < last_p[0]:
                    last_p[0] -= 1
                if p[0] > last_p[0]:
                    last_p[0] += 1
                if p[1] < last_p[1]:
                    last_p[1] -= 1
                if p[1] > last_p[1]:
                    last_p[1] += 1
                # add a wall piece each step
                add_wall(last_p, spaces)
            # point to the next wall corner
            i += 1
    return [spaces, max_x, max_y]





# You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point in your scan.
# To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at 500,0, blocking the source entirely and stopping the flow of sand into the cave.
#  In the example above, the situation finally looks like this after 93 units of sand come to rest:
def day14_part2():
    [spaces, max_x, max_y] = get_cave_part_2()
    units_of_sand = 0
    fell_off = False
    sand_pos = [500, 0]
    while fell_off == False:
        [new_sand_pos, just_fell_off] = simulate_step(sand_pos, spaces)
        if just_fell_off: 
            print('just fell off: ' + str(new_sand_pos[0]) + ', ' + str(new_sand_pos[1]))
            fell_off = True
        if new_sand_pos[0] < 0 or new_sand_pos[0] > max_x:
            print('fell off left or right edge: ' + str(new_sand_pos[0]) + ' > ' + str(max_y))
            fell_off = True
        elif pos_same(sand_pos, new_sand_pos):
            # print('drip: ' + str(sand_pos[0]) + ', ' + str(sand_pos[1]))
            # sand at rest, solidify
            spaces = add_sand(sand_pos, spaces)
            if sand_pos[0] == 500 and sand_pos[1] == 0:
                print('sand filled to the entry point ')
                fell_off = True
            # drop another sand
            new_sand_pos = [500, 0]
            units_of_sand += 1
        sand_pos = new_sand_pos
        if units_of_sand > 1000000:
            print('too much sand: ')
            # debug
            fell_off = True

    print('spaces walked: ')
    debug_spaces(spaces)
    print('units of sand')
    print(str(units_of_sand))

# 25402

day14_part2()