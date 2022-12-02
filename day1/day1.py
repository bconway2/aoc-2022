def get_input(infile):
    with open(infile) as file:
        output = [line.strip() for line in file]
    return output

def part_one(calorie_chart):
    elf_cals = 0
    elves_cals = []
    for entry in calorie_chart:
        if entry != '':
            elf_cals += int(entry)
        else:
            elves_cals.append(elf_cals)
            elf_cals = 0
    elves_cals.append(elf_cals)
    return max(elves_cals)

def part_two(calorie_chart):
    elf_cals = 0
    elves_cals = []
    for entry in calorie_chart:
        if entry != '':
            elf_cals += int(entry)
        else:
            elves_cals.append(elf_cals)
            elf_cals = 0
    elves_cals.append(elf_cals)
    elves_cals.sort(reverse=True)
    return sum(elves_cals[0:3])

d = get_input('input.txt')
part_one(get_input('input.txt'))
part_two(get_input('input.txt'))