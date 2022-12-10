# 30373
# 25512
# 65332
# 33549
# 35390
# Each tree is represented as a single digit 
# whose value is its height, where
# 0 is the shortest and 9 is the tallest.
def get_tree_matrix():
    trees = []
    f = open('input.txt')
    lines = f.readlines()
    for l in lines:
        treelineStr = l.replace('\n', '')
        treeline = []
        for t in treelineStr:
            treeline.append(int(t))
        trees.append(treeline)
    return trees

def is_tree_on_edge(x, y, trees):
    if x <= 0 or y <= 0:
        return True
    if y >= len(trees) - 1 or x >= len(trees[0]) - 1:
        return True 

# A tree is visible if all of the other trees between it
#  and an edge of the grid are shorter than it. 
#  Only consider trees in the same row or column; 
# that is, only look up, down, left, or right from any given tree.
def tree_is_visible(x, y, trees):
    tree_height = trees[y][x]
    print('checking tree at ('+ str(x) + ',' + str(y) + ') height:' + str(tree_height))
    # All of the trees around the edge of the grid are visible
    if is_tree_on_edge(x, y, trees):
        print(' tree on edge')
        return True
    # first check top and bottom
    tree_y_to_top = y
    while tree_y_to_top >= 0:
        tree_y_to_top = tree_y_to_top - 1
        check_tree_height = trees[tree_y_to_top][x]
        if check_tree_height >= tree_height: 
            # tree blocked, stop looking in this direction
            break
        elif is_tree_on_edge(x, tree_y_to_top, trees):
            print(' tree visible from North')
            return True 
    tree_y_to_bottom = y
    while tree_y_to_bottom <= len(trees):
        tree_y_to_bottom = tree_y_to_bottom + 1
        check_tree_height = trees[tree_y_to_bottom][x]
        if check_tree_height >= tree_height: 
            # tree blocked
            break
        elif is_tree_on_edge(x, tree_y_to_bottom, trees):
            print(' tree visible from South')
            return True
    # check left and right
    tree_x_to_left = x

    while tree_x_to_left >= 0:
        tree_x_to_left = tree_x_to_left - 1
        check_tree_height = trees[y][tree_x_to_left]
        if check_tree_height >= tree_height: 
            # tree blocked
            break
        elif is_tree_on_edge(tree_x_to_left, y, trees):
            print(' tree visible from West')
            return True
    tree_x_to_right = x
    while tree_x_to_right <= len(trees[0]):
        tree_x_to_right = tree_x_to_right + 1
        check_tree_height = trees[y][tree_x_to_right]
        if check_tree_height >= tree_height: 
            # tree blocked
            break
        elif is_tree_on_edge(tree_x_to_right, y, trees):
            print(' tree visible from East')
            return True
    print('hidden tree found at ('+ str(x) + ',' + str(y) + ') height:' + str(tree_height))
    return False


def count_visible_trees(trees):
    num_visible = 0
    y = 0
    while y < len(trees):
        x = 0 
        while x < len(trees[y]):
            if tree_is_visible(x, y, trees):
                num_visible = num_visible + 1 
            x = x + 1
        y = y + 1
    return num_visible
        

# Consider your map; 
# how many trees are visible from outside the grid?
def day8_part1():
    num_visible = count_visible_trees(get_tree_matrix())
    print(num_visible)

def get_highest_tree_score(trees):
    max_tree_score = 0
    y = 0
    while y < len(trees):
        x = 0 
        while x < len(trees[y]):
            tree_score = get_tree_score(x, y, trees)
            if tree_score > max_tree_score:
                max_tree_score = tree_score 
            x = x + 1
        y = y + 1
    return max_tree_score


# A tree's scenic score is found by multiplying together
#  its viewing distance in each of the four directions. 
def get_tree_score(x, y, trees):
    tree_height = trees[y][x]
    print('checking tree at ('+ str(x) + ',' + str(y) + ') height:' + str(tree_height))
    tree_score_up = 0
    tree_score_down = 0
    tree_score_left = 0
    tree_score_right = 0
    # check up left right down
    tree_y_to_top = y
    while tree_y_to_top >= 0:
        if tree_y_to_top == 0:
            print(' tree visible from North')
            break 
        tree_y_to_top = tree_y_to_top - 1
        tree_score_up = tree_score_up + 1
        check_tree_height = trees[tree_y_to_top][x]
        if check_tree_height >= tree_height: 
            # tree blocked, stop looking in this direction
            break
    print(' tree score up ' + str(tree_score_up))
    # check left and right
    tree_x_to_left = x
    while tree_x_to_left > 0:
        if tree_x_to_left == 0:
            print(' tree visible from West')
            break
        tree_x_to_left = tree_x_to_left - 1
        tree_score_left = tree_score_left + 1
        check_tree_height = trees[y][tree_x_to_left]
        if check_tree_height >= tree_height: 
            # tree blocked
            break
    print(' tree score left ' + str(tree_score_left))
    tree_x_to_right = x
    while tree_x_to_right <= len(trees[0]):
        if tree_x_to_right == len(trees[y]) - 1:
            print(' tree visible from East')
            break
        tree_score_right = tree_score_right + 1
        tree_x_to_right = tree_x_to_right + 1
        check_tree_height = trees[y][tree_x_to_right]
        if check_tree_height >= tree_height: 
            # tree blocked
            break
    print(' tree score right ' + str(tree_score_right))
    tree_y_to_bottom = y
    while tree_y_to_bottom <= len(trees):
        if tree_y_to_bottom == len(trees) - 1:
            print(' tree visible from South')
            break
        tree_y_to_bottom = tree_y_to_bottom + 1
        tree_score_down = tree_score_down + 1
        check_tree_height = trees[tree_y_to_bottom][x]
        if check_tree_height >= tree_height: 
            # tree blocked
            break
    print(' tree score down ' + str(tree_score_down))
    tree_score = tree_score_right * tree_score_left * tree_score_up * tree_score_down 
    print('tree at ('+ str(x) + ',' + str(y) + ') score:' + str(tree_score))
    return tree_score



# Consider your map; 
# how many trees are visible from outside the grid?
def day8_part2():
    highest_tree_score = get_highest_tree_score(get_tree_matrix())
    print(highest_tree_score)

day8_part2()
