def abc_to_rps(i):
    if i == 'A':
        return 'R'
    if i == 'B':
        return 'P'
    if i == 'C':
        return 'S'
    return None
def xyz_to_rps(i):
    if i == 'X':
        return 'R'
    if i == 'Y':
        return 'P'
    if i == 'Z':
        return 'S'
    return None
        


def inputToArray():
    f = open('input.txt')
    lines = f.readlines()
    rps = []
    for l in lines:
        # The first column is what your opponent is going to play: 
        # A for Rock, B for Paper, and C for Scissors
        # The second column is what you should play 
        # X for Rock, Y for Paper, and Z for Scissors 
        [them, you] = l.split(" ")
        rps.append([abc_to_rps(them), xyz_to_rps(you.replace('\n', ''))])
    return rps

def findSums(numbersArray):
    sums = []
    sum = 0
    for n in numbersArray:
        if n is None:
            sums.append(sum)
            sum = 0
        else:
            sum = sum + n
    return sums    

def value_of_shape(i):
    if i == 'R':
        return 1
    if i == 'P':
        return 2
    if i == 'S':
        return 3
    return None

def game_outcome(them, you):
    # win
    if (them == 'R' and you == 'P') or (them == 'P' and you == 'S') or (them == 'S' and you == 'R'):
        return 6
    # loss
    if (them == 'P' and you == 'R') or (them == 'S' and you == 'P') or (them == 'R' and you == 'S'):
        return 0
    # draw
    return 3

def day2():
    rps = inputToArray()
    # The winner of the whole tournament is the player with the highest score. 
    # Your total score is the sum of your scores for each round. 
    # The score for a single round is the score for the shape you selected 
    # (1 for Rock, 2 for Paper, and 3 for Scissors) 
    # plus the score for the outcome of the round 
    # (0 if you lost, 3 if the round was a draw, and 6 if you won).
    # part 1
    rounds = []
    out = 0
    for game in rps:
        [them, you] = game
        out = out + value_of_shape(you) + game_outcome(them, you)
    print(out)

def xyz_to_ldw(i):
    if i == 'X':
        return 'L'
    if i == 'Y':
        return 'D'
    if i == 'Z':
        return 'W'
    return None

def inputToArray_part2():
    f = open('input.txt')
    lines = f.readlines()
    rps = []
    for l in lines:
        # The first column is what your opponent is going to play: 
        # A for Rock, B for Paper, and C for Scissors
        # the second column says how the round needs to end: 
        # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. 
        [them, you] = l.split(" ")
        rps.append([abc_to_rps(them), xyz_to_ldw(you.replace('\n', ''))])
    return rps

def rps_from_outcome(them, outcome):
    if outcome == 'W':
        if them == 'R':
            return 'P'
        if them == 'P':
            return 'S'
        if them == 'S':
            return 'R'
    if outcome == 'L':
        if them == 'P':
            return 'R'
        if them == 'S':
            return 'P'
        if them == 'R':
            return 'S'
    # draw means return the same value  
    return them            

def day2_part2():
    rps = inputToArray_part2()
    # The winner of the whole tournament is the player with the highest score. 
    # Your total score is the sum of your scores for each round. 
    # The score for a single round is the score for the shape you selected 
    # (1 for Rock, 2 for Paper, and 3 for Scissors) 
    # plus the score for the outcome of the round 
    # (0 if you lost, 3 if the round was a draw, and 6 if you won).
    # part 1
    rounds = []
    out = 0
    for game in rps:
        [them, outcome] = game
        you = rps_from_outcome(them, outcome)
        out = out + value_of_shape(you) + game_outcome(them, you)
    print(out)


day2_part2()