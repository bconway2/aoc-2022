def get_input(infile):
    with open(infile) as file:
        output = [line.strip() for line in file]
    return output

def part_one(calorie_chart):
    elf_cals = 0
    elves_cals = []
    for entry in calorie_chart:
        if entry != '\n':
            elf_cals += int(entry)
        else:
            elves_cals.append(elf_cals)
            elf_cals = 0
    elves_cals.append(elf_cals)
    return elves_cals

d = get_input('input.txt')
part_one(get_input('input.txt'))
part_two(get_input('input.txt'))