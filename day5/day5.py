#Brian decided to cheat and code in the crate initial positions

def initialize_crates():
    crates = []
    crates.append(['R','P','C','D','B','G'])
    crates.append(['H','V,','G'])
    crates.append(['N','S','Q','D','J','P','M'])
    crates.append(['P','S','L','G','D','C','N','M'])
    crates.append(['J','B','N','C','P','F','L','S'])
    crates.append(['Q','B','D','Z','V','G','T','S'])
    crates.append(['B','Z','M','H','F','T','Q'])
    crates.append(['C','M','D','B','F'])
    crates.append(['F','C','Q','G'])
    return crates

def get_instructions(infile):
    n = 0
    output = []
    with open(infile) as file:
        for line in file:
            n = n + 1
            if n >10:
                temp = line.strip().split(' ')
                output.append([int(temp[1]), int(temp[3]) - 1, int(temp[5]) -1])
    return output

def move_crates(crates,instructions):
    for i in range(0,instructions[0]):
       last = crates[instructions[1]].pop()
       crates[instructions[2]].append(last)
    return crates

def move_crates2(crates, instructions):
    for i in range(instructions[0],0,-1):
       last = crates[instructions[1]].pop(-i)
       crates[instructions[2]].append(last)
    return crates

def part_one(crates, instructions):
    for instruction in instructions:
        crates = move_crates(crates, instruction)
    top_crates = []
    for crate in crates:
        top_crates.append(crate.pop())
    return top_crates

def part_two(crates, instructions):
    for instruction in instructions:
        crates = move_crates2(crates, instruction)
    top_crates = []
    for crate in crates:
        top_crates.append(crate.pop())
    return top_crates

def main():
    crates = initialize_crates()
    instructions = get_instructions('input.txt')
    print(part_one(crates,instructions))
    crates = initialize_crates()
    print(part_two(crates,instructions))
    return

if __name__ == "__main__":
    main()   