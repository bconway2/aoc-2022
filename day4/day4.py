def get_input(infile):
    with open(infile) as file:
        output = [line.strip().split(',') for line in file]
    return output

def list_assigments(assignments):
    assignments_list = []
    for assignment in assignments:
        seat_range = assignment.split('-')
        assignments_list.append([*range(int(seat_range[0]), int(seat_range[1]) + 1)])
    return assignments_list

def compare_assignments(assignments_list):
    if len(assignments_list[0]) > len(assignments_list[1]):
        longer_list = assignments_list[0]
        shorter_list = assignments_list[1]
    else: 
        longer_list = assignments_list[1]
        shorter_list = assignments_list[0]
    if set(shorter_list) == set(longer_list).intersection(shorter_list):
        return True
    else: return False

def compare_assignments2(assignments_list):
    overlaps =  len(set(assignments_list[0]).intersection(assignments_list[1]))
    if overlaps > 0: return True
    else: return False
    
def part_one(all_assignments):
    overlapping_pairs = 0
    for assignment_pair in all_assignments:
        pair_list = list_assigments(assignment_pair) 
        overlap = compare_assignments(pair_list)
        if overlap == True: overlapping_pairs += 1
    return overlapping_pairs

def part_two(all_assignments):
    total_overlaps = 0
    for assignment_pair in all_assignments:
        pair_list = list_assigments(assignment_pair) 
        any_overlaps = compare_assignments2(pair_list)
        if any_overlaps == True: total_overlaps += 1
    return total_overlaps

def main():
    sg = get_input('input.txt')
    print(part_one(sg))
    print(part_two(sg))
    return

if __name__ == "__main__":
    main()    