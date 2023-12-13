def main():
    max_cubes = {"red": 12, "green": 13, "blue": 14}

    file = open("./day_2/puzzle_input.txt", "r")

    answer = 0

    for line in file.readlines():
        id, grabs = line.split(": ")
        id = int(id.split(" ")[1])
        grabs = grabs.rstrip("\n").split("; ")

        possible = True
        for grab in grabs:
            piece = grab.split(", ")
            for cube in piece:
                amount, color = cube.split(" ")
                if int(amount) > max_cubes[color]:
                    possible = False
                    break
        
        if possible:
            answer += id

    file.close()

    print(answer)

if __name__ == "__main__":
    main()