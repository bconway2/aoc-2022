def get_input(infile):
    with open(infile) as file:
        output = [line.strip().split(',') for line in file][0]
    return output[0]

def part_one(input_code):
    for i in range(4,len(input_code)):
        if (len(set(input_code[i-4:i]))) == 4: return i
    return 'Fail'

def part_two(input_code):
    for i in range(14,len(input_code)):
        if (len(set(input_code[i-14:i]))) == 14: return i
    return 'Fail'

def main():
    scanner_output = get_input('input.txt')
    print(part_one(scanner_output))
    print(part_two(scanner_output))
    return

if __name__ == "__main__":
    main()     