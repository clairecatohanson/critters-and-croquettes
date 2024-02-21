from slithering import BoaConstrictor, Copperhead, Cottonmouth, KingSnake, Python
from swimming import Angelfish, BettaFish, Goldfish, Koi, Zebrafish
from walking import Donkey, Goat, Llama, Pony, Sheep

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "Llama chow")
george = Goat("George", "domestic goat", "morning", "Goat chow")
doug = Donkey("Doug", "domestic donkey", "morning", "Donkey chow")
sally = Sheep("Sally", "domestic sheep", "afternoon", "Sheep chow")
penelope = Pony("Penelope", "domestic pony", "midday", "Pony chow")

karen = KingSnake("Karen", "kingsnake", "king snake snacks")
cooper = Copperhead("Cooper", "copperhead snake", "copperhead snake snacks")
peter = Python("Peter", "python", "python snake snacks")
carter = Cottonmouth("Carter", "cottonmouth snake", "cottonmouth snake snacks")
bobby = BoaConstrictor("Bobby", "boa constrictor", "boa constrictor snake snacks")

gary = Goldfish("Gary", "goldfish", "goldfish food")
alan = Angelfish("Alan", "angelfish", "angelfish food")
benny = BettaFish("Benny", "betta fish", "betta fish food")
kayla = Koi("Kayla", "koi fish", "koi fish food")
zoe = Zebrafish("Zoe", "zebrafish", "zebrafish food")

print(f"{miss_fuzz.name} is available to pet during the {miss_fuzz.shift} shift.")
miss_fuzz.feed()
doug.feed()
george.feed()
bobby.feed()
print(bobby)
print(gary)
print(alan)
print(benny)
print(kayla)
print(zoe)
