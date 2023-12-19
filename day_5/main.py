import time


def main():
    file = open("puzzle_input.txt", "r")

    # Get wanted seeds for the end
    wanted_seeds = file.readline().rstrip("\n").split(": ")[1].split(" ")
    wanted_seeds = array_values_to_int(wanted_seeds)
    max_seed = 0

    # Skip empty line
    file.readline().rstrip("\n")

    # Get map blocks
    map_blocks = [[]]
    for line in file.readlines():

        if line != "\n":
            map_blocks[-1].append(line.rstrip("\n"))
        else:
            map_blocks.append([])

    for block in map_blocks:
        for line in block:

            if len(line.split(" ")) < 3:
                continue

            for number in line.split(" "):
                if int(number) > max_seed:
                    max_seed = int(number)

    dics = []
    for block in map_blocks:
        dics.append({})
        for line in block:

            if len(line.split(" ")) < 3:
                continue

            for number in line.split(" "):
                if int(number) > max_seed:
                    max_seed = int(number)


        for line in block:
            print("running", time.time())
            # if line is not splittable in 2 parts, skip it
            if len(line.split(" ")) < 3:
                continue

            work_line = [int(x) for x in line.split(" ")]
            destination_range = work_line[0]
            source_range = work_line[1]
            range_length = work_line[2]

            mapping(dics[-1], destination_range, source_range, range_length) 

        need_adding = []
        for i in range(0, max_seed + 1):
            if i not in dics[-1].keys():
                need_adding.append(i)

        for seed in need_adding:
            dics[-1][seed] = seed
        
    file.close()

    lowest_location = max_seed
    for seed in wanted_seeds:
        next_lookup = seed
        last_lookup = -1
        for dic in dics:
            next_lookup = dic[next_lookup]
            last_lookup = next_lookup
        
        if last_lookup < lowest_location:
            lowest_location = last_lookup

    print("Lowest location:", lowest_location)
        
def array_values_to_int(array):
    new_array = []

    for item in array:
        new_array.append(int(item))

    return new_array

def mapping(dic, dest, source, r_length):
    for length in range(r_length):
        dic[source + length] = dest + length

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("Execution time:", end_time - start_time, "seconds")