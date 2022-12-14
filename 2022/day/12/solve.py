import string

# Your current position (S) has elevation a,
#  the location that should get the best signal (E) has elevation z.
def get_map():
    start_point = [0,0]
    end_point = [0,0]
    char_map = []
    height_map = []
    visited_map = []
    f = open('input.txt')
    lines = f.readlines()
    y = 0
    for l in lines:
        x = 0
        line_arr = l.strip().replace('\n', '')
        row = []
        visited_row = []
        char_row = []
        for r in line_arr:
            char_row.append(r)
            visited_row.append(False)
            if r == 'S':
                start_point = [y,x]
                row.append(string.ascii_lowercase.index('a'))
            elif r == 'E':
                end_point = [y,x]
                row.append(string.ascii_lowercase.index('z'))
            else: 
                row.append(string.ascii_lowercase.index(r))
            x += 1
        char_map.append(char_row)
        height_map.append(row)
        visited_map.append(visited_row)
        y += 1
    # mark the starting point as visited
    visited_map[start_point[0]][start_point[1]] = True
    return [start_point, end_point, height_map, visited_map, char_map]

def path_contains_point(path, point):
    for p in path:
        if p[0] == point[0] and p[1] == point[1]:
            return True
    return False


# fork from the next point, return empty if there are no possible paths
def get_possible_points(point, height_map, visited_map, char_map):
    point_height = height_map[point[0]][point[1]]
    char = char_map[point[0]][point[1]]
    possible_points = []
    print(' get_possible_paths for: ' + char + ' (' + str(point[1]) + ', ' + str(point[0])  + ') : ' + str(point_height))
    # check the cardinal directions
    for [dx, dy] in [[-1, 0],[1, 0],[0, 1],[0, -1]]:
        check_point = [point[0] + dy, point[1] + dx] 
        # print('  check (' + str(check_point[1]) + ', ' + str(check_point[0])  + ')')
        if (check_point[0] < 0 or check_point[1] < 0 or len(height_map) <= check_point[0] or len(height_map[0]) <= check_point[1]) == False: 
            check_point_char = char_map[check_point[0]][check_point[1]]
            # no backtracking / loops
            check_point_unvisited = visited_map[check_point[0]][check_point[1]] == False
            # must be climbable
            check_point_height = height_map[check_point[0]][check_point[1]]
            dist = check_point_height - point_height
            check_point_within_range = dist <= 1
            if check_point_unvisited and check_point_within_range:
                possible_points.append(check_point)

                # visited_map[check_point[0]][check_point[1]] = True

            elif check_point_within_range == False:
                print('  not in range (' + str(check_point[1]) + ', ' + str(check_point[0])  + ') ' + check_point_char)
            elif check_point_unvisited == False:
                print('  already visited (' + str(check_point[1]) + ', ' + str(check_point[0])  + ') ' + check_point_char)
    print('  found ' + str(len(possible_points)) + ' ways out')
    for p in possible_points:
        p_h = height_map[p[0]][p[1]]
        c = char_map[p[0]][p[1]]
        d = abs(point_height - p_h)
        print('   (' + str(p[1]) + ', ' + str(p[0])  + ') : ' + str(c))
 
    return possible_points


def arrived(points, char_map):
    for point in points:
        char = char_map[point[0]][point[1]]
        if char == 'E':
            return point
    return None

def print_path(path, char_map=None):
    print('path:')
    for point in path:
        if char_map != None:
            char = char_map[point[0]][point[1]]
            print(' ' + char + ' (' + str(point[1]) + ', ' + str(point[0])  + ')')
        else: 
            print(' (' + str(point[1]) + ', ' + str(point[0])  + ')')

def deduplicate_list_of_points(points):
    dict_of_points = {}
    points_list = []
    for p in points:
        dict_of_points[str(p[1]) +','+str(p[0])] = 1
    for k in dict_of_points.keys():
        [x_raw, y_raw] = k.split(',')
        points_list.append([int(y_raw), int(x_raw)])
    return points_list



def day12_part1():
    [start_point, end_point, height_map, visited_map, char_map] = get_map()
    points = [start_point]
    walking = True
    steps = 0
    while walking:
        steps += 1
        print('step ' + str(steps))
        new_points = []
        for p in points:
            new_points_for_p = get_possible_points(p, height_map, visited_map, char_map)
            new_points.extend(new_points_for_p)
        points = deduplicate_list_of_points(new_points)
        for point in points:
            visited_map[point[0]][point[1]] = True


        if len(points) == 0:
            print('out of paths!')
            walking = False            
        if steps > len(height_map[0]) * len(height_map):
            print('traversed entire map!')
            walking = False
        path_arrived = arrived(points, char_map)
        if path_arrived is not None:
            print('arrived: ' + str(steps))
            # print_path(path_arrived, char_map)
            walking = False
    return steps


def get_map_of_a():
    start_points = []
    end_point = None
    char_map = []
    height_map = []
    visited_map = []
    f = open('input.txt')
    lines = f.readlines()
    y = 0
    for l in lines:
        x = 0
        line_arr = l.strip().replace('\n', '')
        row = []
        visited_row = []
        char_row = []
        for r in line_arr:
            char_row.append(r)
            visited_row.append(False)
            if r == 'S' or r == 'a':
                start_points.append([y,x])
                row.append(string.ascii_lowercase.index('a'))
            elif r == 'E':
                end_point = [y,x]
                row.append(string.ascii_lowercase.index('z'))
            else: 
                row.append(string.ascii_lowercase.index(r))
            x += 1
        char_map.append(char_row)
        height_map.append(row)
        visited_map.append(visited_row)
        y += 1
    # mark the starting points as visited
    for start_point in start_points:
        visited_map[start_point[0]][start_point[1]] = True
    return [start_points, end_point, height_map, visited_map, char_map]


def day12_part2():
    [start_points, end_point, height_map, visited_map, char_map] = get_map_of_a()
    points = start_points
    walking = True
    steps = 0
    while walking:
        steps += 1
        print('step ' + str(steps))
        new_points = []
        for p in points:
            new_points_for_p = get_possible_points(p, height_map, visited_map, char_map)
            new_points.extend(new_points_for_p)
        points = deduplicate_list_of_points(new_points)
        for point in points:
            visited_map[point[0]][point[1]] = True


        if len(points) == 0:
            print('out of paths!')
            walking = False            
        if steps > len(height_map[0]) * len(height_map):
            print('traversed entire map!')
            walking = False
        path_arrived = arrived(points, char_map)
        if path_arrived is not None:
            print('arrived: ' + str(steps))
            # print_path(path_arrived, char_map)
            walking = False
    return steps

day12_part2()