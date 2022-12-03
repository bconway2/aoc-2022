import string

def get_input(infile):
    with open(infile) as file:
        output = [line.strip() for line in file]
    return output

def split_sack(rucksack):
    compartments = []
    compartments.append(rucksack[0:int(len(rucksack)/2)])
    compartments.append(rucksack[int(len(rucksack)/2):])
    return compartments

def gen_priorities():
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index + 27
    return values

def compare_compartments(compartments):
    return list(set(compartments[0]) & set(compartments[1]))

def search_rucksacks(rucksacks):
    return list(set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2]))

def part_one(rucksacks):
    priority_dict = gen_priorities()
    sum_priority = 0
    for rucksack in rucksacks:
        compartments = split_sack(rucksack)
        common_item = compare_compartments(compartments)[0]
        sum_priority += priority_dict[common_item]
    return sum_priority

def part_two(rucksacks):
    priority_dict = gen_priorities()
    sum_priority = 0
    for i in range(2, len(rucksacks), 3):
        ruckgroup = [rucksacks[i-2], rucksacks[i-1], rucksacks[i]]
        common_item = search_rucksacks(ruckgroup)[0]
        sum_priority += priority_dict[common_item]
    return sum_priority

def main():
    sg = get_input('input.txt')
    print(part_one(sg))
    print(part_two(sg))
    return

if __name__ == "__main__":
    main()    