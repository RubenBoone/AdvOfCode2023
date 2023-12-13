def part1():
    file = open("./puzzle_input.txt", "r")

    answer = 0

    for line in file.readlines():
        
        first_number = 0
        last_number = 0

        for char in line:
            try:
                if first_number == 0:
                    first_number = int(char)
                else:
                    last_number = int(char)
            except ValueError:
                pass

        if last_number == 0:
            last_number = first_number
        
        answer += int(str(first_number) + str(last_number))

    print(answer)


if __name__ == "__main__":
    part1()