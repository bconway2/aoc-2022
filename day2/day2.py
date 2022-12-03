def get_input(infile):
    with open(infile) as file:
        output = [line.strip().split(' ') for line in file]
    return output

def score_round1(round):
    if round[0] == 'A':
        if round[1] == 'X': return 4
        elif round[1] == 'Y': return 8 
        else: return 3
    elif round[0] == 'B':
        if round[1] == 'X': return 1
        elif round[1] == 'Y': return 5
        else: return 9
    else:
        if round[1] == 'X': return 7
        elif round[1] == 'Y': return 2
        else: return 6

def score_round2(round):
    if round[0] == 'A':
        if round[1] == 'X': return 3
        elif round[1] == 'Y': return 4 
        else: return 8
    elif round[0] == 'B':
        if round[1] == 'X': return 1
        elif round[1] == 'Y': return 5
        else: return 9
    else:
        if round[1] == 'X': return 2
        elif round[1] == 'Y': return 6
        else: return 7

def part_one(strategy_guide):
    total_score = 0
    for entry in strategy_guide:
        total_score += score_round1(entry)
    return total_score

def part_two(strategy_guide):
    total_score = 0
    for entry in strategy_guide:
        total_score += score_round2(entry)
    return total_score

def main():
    sg = get_input('input.txt')
    print(part_one(sg))
    print(part_two(sg))
    return

if __name__ == "__main__":
    main()    