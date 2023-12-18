def format_data(line):
        line = line.rstrip("\n")
        card_number = line.split(": ")[0].split(" ")[-1]
        winning_numbers, my_numbers = line.split("|")
        winning_numbers = winning_numbers.split(": ")[1].rstrip(" ").lstrip(" ")
        my_numbers = my_numbers.lstrip(" ").rstrip(" ")
        winning_numbers = winning_numbers.split(" ")
        my_numbers = my_numbers.split(" ")

        return (int(card_number), winning_numbers, my_numbers)

def main():
    file = open("puzzle_input.txt", "r")
    cards = {}

    for line in file.readlines():
        card_number, winning_numbers, my_numbers = format_data(line)

        try:
            cards[card_number] += 1
        except KeyError:
            cards[card_number] = 1

        total = 0
        for number in my_numbers:
            if number in winning_numbers and number != "":
                total += 1

        for i in range(1, total+1):
            for j in range(0, cards[card_number]):
                try:
                    cards[card_number + i] += 1
                except KeyError:
                    cards[card_number + i] = 1

    file.close()

    total_cards = 0
    for card in cards.values():
        total_cards += card

    print(total_cards)
              

if __name__ == "__main__":
    main()