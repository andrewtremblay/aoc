# mjqjpqmgbljsphdztnvjfqwrcgsmlb = 7 because
# mjq[jpqm]gbljsphdztnvjfqwrcgsmlb is first unique
def has_full_window(window, size):
    return len(window) >= size

def no_repeating(window):
    prev = []
    search = []
    search.extend(window)
    while len(search) > 0:
        char = search.pop()
        if char in prev:
            return False
        prev.append(char)
    return True


def walk_window(signal, size=4): 
    i = 0
    window = []
    while i < len(signal):
        char = signal[i]
        window.append(char)
        window = window[-size:]
        if has_full_window(window, size) and no_repeating(window):
            print(window)
            print(i + 1) # first character AFTER the window
            return
        i = i + 1


def day6_part1():
    f = open('input.txt')
    lines = f.readlines()
    walk_window(lines[0])


# four characters that are all different
# day6_part1()

# fourteen characters that are all different
def day6_part2():
    f = open('input.txt')
    lines = f.readlines()
    walk_window(lines[0], 14)

day6_part2()