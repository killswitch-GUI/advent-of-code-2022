elf_to_ask = 0
fat_elf = 0
elves = {}

with open("day-1-input.txt", "r") as f:
    for count, elf in enumerate(f.read().split("\n\n")):
        elves[sum([eval(i) for i in elf.splitlines()])] = count
        if sum([eval(i) for i in elf.splitlines()]) > fat_elf:
            elf_to_ask = count
            fat_elf = sum([eval(i) for i in elf.splitlines()])
    print(f"Elf to ask {elf_to_ask+1} - {fat_elf}")
    print(f"Top three elves are Cal: {sum(sorted(elves)[-3:])}")
