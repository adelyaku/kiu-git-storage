animals = input()
animals_list = []
for animal in animals.split(","):
    animals_list.append(str(animal).strip())
human = len(animals_list)+1
if animals_list[-1].strip() == "wolf":
    print("Pls go away and stop eating my sheep")
else:
    animals_position = len(animals_list) - animals_list.index("wolf")-1
    print("Oi! Sheep number {animal_position}! You are about to eaten by a wolf!")
