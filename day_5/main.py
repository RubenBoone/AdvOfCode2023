def main():
    with open('puzzle_input.txt') as file:
        lines = file.read().splitlines()

        wanted_seeds = [int(x) for x in lines[0].split(': ')[1].split(' ')]

        print(f"Wanted seeds: {wanted_seeds}")

        possible_answers = []
        for seed in wanted_seeds:
            next_value = seed
            skip_block = False
            for i in range(2, len(lines)):

                if skip_block:
                    if lines[i] == '':
                        skip_block = False
                    continue

                if len(lines[i].split(' ')) <= 2:
                    continue
                else:
                    work_line = [int(x) for x in lines[i].split(' ')]
                    if next_value >= work_line[1] and next_value <= work_line[1] + work_line[2]:
                        next_value += (work_line[0] - work_line [1])
                        skip_block = True

            possible_answers.append(next_value)
    file.close()

    print("Possible answers:", possible_answers)
    print("Answer:", min(possible_answers))

if __name__ == '__main__':
    main()