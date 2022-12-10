# build directory from commands 
# calculate total size of each directory
# Find all of the directories with a total size of at most 100000.

# Find the sum of the total sizes of those directories, excluding children

filesystem_info = {}

def get_dirstring(dirs):
    to_ret = '/'
    for d in dirs:
        if to_ret == '/':
            to_ret = d
        else:
            to_ret = to_ret + '/' + d 
    return to_ret

# adds file size to all parent dirs
def report_file_size(file_size, file_name, filesystem_subinfo, dirs):
    dirstack = dirs.copy()
    while len(dirstack) > 0:
        dirstring = get_dirstring(dirstack)
        if dirstring in filesystem_info.keys():
            filesystem_info[dirstring] = filesystem_info[dirstring] + file_size
        else: 
            filesystem_info[dirstring] = file_size
        dirstack.pop()



def get_files_from_commands():
    commands = []
    f = open('input.txt')
    lines = f.readlines()
    current_dirs = ['']
    filesystem_subinfo = {}
    for l in lines: 
        units = l.replace('\n', '').split(' ')
        if units[0] == '$': # command
            cmd = units[1]
            # if cmd == 'ls':
            #     # parse info until next command
            #     # ignore
            if cmd == 'cd':
                next_dir = units[2]
                # change root filesystem
                if next_dir == '..':
                    current_dirs.pop()
                elif next_dir == '/':
                    current_dirs = ['']
                else:
                    current_dirs.append(next_dir)
        elif units[0] == 'dir':
            dir_name = units[1]
            # we don't need to report dirs until we go into them and find files
            # report_dir(dir_name, filesystem_subinfo, current_dirs)
        else:
            # file
            file_size = int(units[0])
            file_name = units[1]
            report_file_size(file_size, file_name, filesystem_subinfo, current_dirs)


def size_of_dir(dir):
    return filesystem_info[dir]



def find_substring_from_strings(strings, test):
    for s in strings:
        if len(test) > len(s) and s == test[0:len(s)]:
            return s
    return None

def collapse_dirs(di):
    dirs = di.copy()
    dirs.sort()
    to_ret = []
    for d in dirs:
        substring = find_substring_from_strings(to_ret, d) 
        if substring != None:
            print('skipping subdir: ' + d + ' (existing dir: ' + substring + ')')
        else:
            to_ret.append(d)
    return to_ret

def day7_part1():
    get_files_from_commands()
    dirs = list(filesystem_info)
    dirs_by_size = dirs.copy()
    dirs_by_size.sort(key=size_of_dir) 
    eligible_dirs = []
    for d in dirs_by_size:
        size = size_of_dir(d)
        if size < 100000:
            eligible_dirs.append(d)
    # eligible_dirs = collapse_dirs(eligible_dirs)
    print('all dirs under 100000 by size:')
    total = 0
    for d in eligible_dirs: 
        size = size_of_dir(d)
        print(d + ' (' + str(size) + ')')
        total = total + size
    print('total: ' + str(total))


# day7_part1()

# 70000000 - 1454188 = 68545812
# 70.000.000 - 43.837.783 = 26.162.217 open space
# 30.000.000 - 26.162.217 =  3.837.783 space needed
# The total disk space available to the filesystem is 70000000. 
# To run the update, you need unused space of at least 30000000. 
# You need to find a directory you can delete that
#  will free up enough space to run the update.
def day7_part2():
    get_files_from_commands()
    dirs = list(filesystem_info)
    dirs_by_size = dirs.copy()
    dirs_by_size.sort(key=size_of_dir) 
    eligible_dirs = []
    for d in dirs_by_size:
        size = size_of_dir(d)
        if size >= 3837783:
            eligible_dirs.append(d)
    # eligible_dirs = collapse_dirs(eligible_dirs)
    print('all dirs:')
    total = 0
    for d in eligible_dirs: 
        size = size_of_dir(d)
        print(d + ' (' + str(size) + ')')
        total = total + size
    print('total: ' + str(total))

day7_part2()
