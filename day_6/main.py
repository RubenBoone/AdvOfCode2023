def main():
    file = open('day_6/puzzle_input.txt', "r")
    data = file.read().splitlines()

    time = line_to_array(data[0])
    distance = line_to_array(data[1])

    lowest_press_win = time
    higest_press_win = 0
    for i in range(time + 1):
        speed = i
        time_left = time - i
        distance_travelled = speed * time_left

        if distance_travelled > distance:
            lowest_press_win = i
            break

    for i in reversed(range(time + 1)):
        speed = i
        time_left = time - i
        distance_travelled = speed * time_left

        if distance_travelled > distance:
            higest_press_win = i
            break
    answer = higest_press_win - lowest_press_win
    
    print(answer + 1)

    file.close()

def line_to_array(line):
    temp = ""
    numbers = line.split(": ")[-1].split(" ")
    for i in numbers:
        if i != "":
            temp += i
    return int(temp)


if __name__ == '__main__':
    main()