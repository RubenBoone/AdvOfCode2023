def main():
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    multiplication_per_grab = []

    file = open("./day_2/puzzle_input.txt", "r")

    for line in file.readlines():
        id, grabs = line.split(": ")
        id = int(id.split(" ")[1])
        grabs = grabs.rstrip("\n").split("; ")

        for grab in grabs:
            piece = grab.split(", ")
            for cube in piece:
                amount, color = cube.split(" ")
                if int(amount) > max_cubes[color]:
                    max_cubes[color] = int(amount)
        
        
        multiplication = 1
        for color in max_cubes.values():
            multiplication *= color

        multiplication_per_grab.append(multiplication)

        max_cubes = {"red": 0, "green": 0, "blue": 0}

    file.close()

    answer = 0
    for number in multiplication_per_grab:
        answer += number

    print(answer)


if __name__ == "__main__":
    main()