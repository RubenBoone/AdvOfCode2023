def create_list():

    full_list = []
    length = 0
    max_length = False    


    file = open("./day_3/puzzle_input.txt", "r")

    for line in file.readlines():
        for char in line.rstrip("\n"):
            if not max_length:
                length += 1
            full_list.append(char)
        max_length = True    
    file.close()

    return (full_list, length)

def main():

    answer = 0
    full_list, line_length = create_list()

    number_locations = [[]]
    symbol_locations = []

    for item in range(len(full_list)):

        try:
            int(full_list[item])
            number_locations[len(number_locations) - 1].append(item)
        except:
            if len(number_locations[len(number_locations) - 1]) != 0:
                number_locations.append([])
            if full_list[item] != ".":
                symbol_locations.append(item)

    # Last is always empty because of above implementation
    number_locations.pop()

    for number in range(len(number_locations)):
        found = False
        for value in range(len(number_locations[number])):

            # Under number
            if number_locations[number][value] + line_length in symbol_locations:
                found = True
                break

            # Above number
            if number_locations[number][value] - line_length in symbol_locations:
                found = True
                break

            # Left of number
            if number_locations[number][value] - 1 in symbol_locations:
                found = True
                break

            # Right of number
            if number_locations[number][value] + 1 in symbol_locations:
                found = True
                break

            # Diagonal of number
            if (number_locations[number][value] + (line_length + 1) in symbol_locations or 
                number_locations[number][value] - (line_length + 1) in symbol_locations or 
                number_locations[number][value] + (line_length - 1) in symbol_locations or 
                number_locations[number][value] - (line_length - 1) in symbol_locations):
                found = True
                break

        if found:
            string_nr = ""
            for value in number_locations[number]:
                string_nr += full_list[value]
            
            print(answer, "+", string_nr)
            answer += int(string_nr)
            found = False

    print(answer)

if __name__ == "__main__":
    main()