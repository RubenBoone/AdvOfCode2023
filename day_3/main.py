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

def add_to_dict(number_locations, number, full_list, symbol_locations, symbol):
    string_nr = ""
    for char in number_locations[number]:
        string_nr += full_list[char]

    try:
        if int(string_nr) not in symbol_locations[symbol]:
            symbol_locations[symbol].append(int(string_nr))
    except KeyError:
        pass

def main():

    answer = 0
    full_list, line_length = create_list()

    number_locations = [[]]
    symbol_locations = {}

    for item in range(len(full_list)):

        try:
            int(full_list[item])
            number_locations[len(number_locations) - 1].append(item)
        except:
            if len(number_locations[len(number_locations) - 1]) != 0:
                number_locations.append([])
            if full_list[item] == "*":
                symbol_locations[item] = []

    # Last is always empty because of above implementation
    number_locations.pop()

    for number in range(len(number_locations)):
        found = False
        last_value = -1
        for value in range(len(number_locations[number])):
            for symbol in list(symbol_locations.keys()):
                last_value = symbol

                # Under number
                if number_locations[number][value] + line_length == symbol:
                    found = True

                    add_to_dict(number_locations, number, full_list, symbol_locations, symbol)

                    break

                # Above number
                if number_locations[number][value] - line_length == symbol:
                    found = True

                    add_to_dict(number_locations, number, full_list, symbol_locations, symbol)

                    break

                # Left of number
                if number_locations[number][value] - 1 == symbol:
                    found = True

                    add_to_dict(number_locations, number, full_list, symbol_locations, symbol)

                    break

                # Right of number
                if number_locations[number][value] + 1 == symbol:
                    found = True

                    add_to_dict(number_locations, number, full_list, symbol_locations, symbol)

                    break

                # Diagonal of number
                if (number_locations[number][value] + (line_length + 1) == symbol or 
                    number_locations[number][value] - (line_length + 1) == symbol or 
                    number_locations[number][value] + (line_length - 1) == symbol or 
                    number_locations[number][value] - (line_length - 1) == symbol):

                    add_to_dict(number_locations, number, full_list, symbol_locations, symbol)

                    break

    for value_list in symbol_locations.values():
        if len(value_list) == 2:
            answer += value_list[0] * value_list[1]

    print(answer)

if __name__ == "__main__":
    main()