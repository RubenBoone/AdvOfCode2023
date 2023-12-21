def main():
    file = open("puzzle_input.txt", "r")

    wanted_seed = get_wanted_seeds(file.readline())
    file.readline()

    data = file.readlines()
    file.close()

    blocks = [[]]
    for line in data:
        if len(line.split()) < 2:
            blocks.append([])
            continue

        try:
            work_line = [int(x) for x in line.rstrip("\n").split()]
            blocks[-1].append(work_line)
        except ValueError:
            pass
        
    possible_answer = []
    for seed in wanted_seed:
        lookup_number = seed
        for block in blocks:
            dic = {}
            for line in block:
                destination_range = line[0]
                source_range = line[1]
                range_length = line[2]

                for i in range(range_length):
                    dic[source_range + i] = destination_range + i

            if lookup_number in dic.keys():
                lookup_number = dic[lookup_number]
        possible_answer.append(lookup_number)

    answer = possible_answer[0]
    for number in possible_answer:
        if number < answer:
            answer = number

    print(answer)

def get_wanted_seeds(line):
    line = line.split(": ")[1]
    return [int(x) for x in line.split(" ")]

if __name__ == '__main__':
    main()