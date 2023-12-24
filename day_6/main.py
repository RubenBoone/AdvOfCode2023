def main():
    file = open('day_6/puzzle_input.txt', "r")
    data = file.read().splitlines()

    time = line_to_array(data[0])
    distance = line_to_array(data[1])

    new_records = []
    for seconds in range(len(time)):
        new_records.append([])
        for i in range(time[seconds] + 1):
            speed = i
            time_left = time[seconds] - i
            distance_travelled = speed * time_left

            if distance_travelled > distance[seconds]:
                new_records[-1].append(i)

    answer = 1
    for i in range(len(new_records)):
        answer *= len(new_records[i])
    
    print(answer)

    file.close()

def line_to_array(line):
    temp = []
    numbers = line.split(": ")[-1].split(" ")
    for i in numbers:
        if i != "":
            temp.append(int(i))
    return temp


if __name__ == '__main__':
    main()