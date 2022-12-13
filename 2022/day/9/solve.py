# a hypothetical series of motions (your puzzle input) 
def get_series_of_motions():
    motions = []
    f = open('input.txt')
    lines = f.readlines()
    for l in lines:
        [direction, distance] = l.replace('\n', '').split(' ')
        motions.append([direction, int(distance)])
    motions.reverse()
    return motions
    
def get_rope_delta(direction):
    delta_y = 0
    delta_x = 0
    if direction == 'U':
        delta_y = 1
    if direction == 'D':
        delta_y = -1
    if direction == 'L':
        delta_x = -1
    if direction == 'R':
        delta_x = 1
    return [delta_x, delta_y]

# Adjusted during Part 2, used external solution https://www.youtube.com/watch?v=CaPabgNS0jo
def move_rope(rope_points, direction):
    new_rope_points = rope_points.copy()
    [mx, my] = get_rope_delta(direction)
    new_rope_points[0][0] += mx
    new_rope_points[0][1] += my
    head_i = 1 # start right behind the head
    while head_i < len(new_rope_points): 
        dx = new_rope_points[head_i][0] - new_rope_points[head_i - 1][0]
        dy = new_rope_points[head_i][1] - new_rope_points[head_i - 1][1]
        if dx < -1 and dy == 0:
            new_rope_points[head_i][0] += 1
        elif dx > 1 and dy == 0:
            new_rope_points[head_i][0] -= 1
        elif dy < -1 and dx == 0:
            new_rope_points[head_i][1] += 1
        elif dy > 1 and dx == 0:
            new_rope_points[head_i][1] -= 1
        elif dy > 1 and dx > 0:
            new_rope_points[head_i][0] -= 1
            new_rope_points[head_i][1] -= 1
        elif dy < -1 and dx > 0:
            new_rope_points[head_i][0] -= 1
            new_rope_points[head_i][1] += 1
        elif dy < -1 and dx < 0:
            new_rope_points[head_i][0] += 1
            new_rope_points[head_i][1] += 1
        elif dy > 1 and dx < 0:
            new_rope_points[head_i][0] += 1
            new_rope_points[head_i][1] -= 1
        elif dy > 0 and dx > 1:
            new_rope_points[head_i][0] -= 1
            new_rope_points[head_i][1] -= 1
        elif dy < 0 and dx > 1:
            new_rope_points[head_i][0] -= 1
            new_rope_points[head_i][1] += 1
        elif dy < 0 and dx < -1:
            new_rope_points[head_i][0] += 1
            new_rope_points[head_i][1] += 1
        elif dy > 0 and dx < -1:
            new_rope_points[head_i][0] += 1
            new_rope_points[head_i][1] -= 1
        head_i += 1
    return new_rope_points

# Simulate your complete series of motions. 
def simulate(state, motions):
    while len(motions) > 0:
        next_motion = motions.pop()
        [direction, step] = next_motion 
        print('direction: ' + direction + ', step ' + str(step))
        next_state = state.copy()
        [segments, tail_unique_history] = state
        new_segments = move_rope(segments, direction)
        new_tail = new_segments[-1]
        next_state[0] = new_segments
        [new_tail_x, new_tail_y] = new_tail
        print(segments)
        # record history of tail
        tail_str = str(new_tail_x) + ',' + str(new_tail_y)
        if tail_str not in tail_unique_history:
            print(' UNIQUE TAIL POS: ' + tail_str)
            tail_unique_history.append(tail_str)
        next_state[1] = tail_unique_history
        new_step = step - 1
        if new_step < 1:
            # no more steps to simulate for this motion
            state = next_state
        else:
            # re-append adjusted motion if steps are not complete
            motions.append([direction, new_step])
            state = next_state
    return state

# How many positions does the tail of the rope visit at least once?
def count_visited(state):
    [_, tail_unique_history] = state
    return len(tail_unique_history)
    

def day9_part1():
    motions = get_series_of_motions()
    # head and tail both start on top of each other
    # zero history
    initial_state = [[[0,0], [0,0]], []] 
    final_state = simulate(initial_state, motions)
    print(count_visited(final_state))

# Simulate your complete series of motions on a larger rope with ten knots.
#  How many positions does the tail of the rope visit at least once?
def day9_part2():
    motions = get_series_of_motions()
    # head and tail both start on top of each other
    # zero history
    initial_state = [[[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]], []] 
    final_state = simulate(initial_state, motions)
    print(count_visited(final_state))

day9_part2()