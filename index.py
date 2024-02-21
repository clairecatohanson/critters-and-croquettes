from slithering import BoaConstrictor, Copperhead, Cottonmouth, KingSnake, Python
from swimming import Angelfish, BettaFish, Goldfish, Koi, Zebrafish
from walking import Donkey, Goat, Llama, Pony, Sheep

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday")
george = Goat("George", "domestic goat", "morning")
doug = Donkey("Doug", "domestic donkey", "morning")
sally = Sheep("Sally", "domestic sheep", "afternoon")
penelope = Pony("Penelope", "domestic pony", "midday")

karen = KingSnake("Karen", "kingsnake")
cooper = Copperhead("Cooper", "copperhead snake")
peter = Python("Peter", "python")
carter = Cottonmouth("Carter", "cottonmouth snake")
bobby = BoaConstrictor("Bobby", "boa constrictor")

gary = Goldfish("Gary", "goldfish")
alan = Angelfish("Alan", "angelfish")
benny = BettaFish("Benny", "betta fish")
kayla = Koi("Kayla", "koi fish")
zoe = Zebrafish("Zoe", "zebrafish")

print(f"{miss_fuzz.name} is available to pet during the {miss_fuzz.shift} shift.")
