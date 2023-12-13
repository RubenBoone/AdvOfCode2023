def part1():
    file = open("./puzzle_input.txt", "r")
    numbers_spelled_out = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    answer = 0

    line_nr = 1

    for line in file.readlines():
        possible_word = ""
        first_number = 0
        last_number = 0
        number = 0

        for char in line:
            try:
                number = int(char)
            except ValueError:
                possible_word += char
                for word in numbers_spelled_out:
                    if word in possible_word:
                        number = numbers_spelled_out.index(word) + 1
                        possible_word = possible_word[-1:]
                        break

            if first_number == 0:
                first_number = number
            else:
                last_number = number
        
        answer += int(str(first_number) + str(last_number))
        line_nr += 1

    print(answer)

if __name__ == "__main__":
    part1()
