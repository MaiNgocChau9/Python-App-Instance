class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} {self.sound}")


animals = [
    Animal("Hổ mang", "Bò sát", "rít"),
    Animal("Sư tử", "Có vú", "gầm gừ"),
    Animal("Vẹt", "Chim", "hót"),
]


for animal in animals:
  print(f"Tên: {animal.name}")
  print(f"Giống loài: {animal.species}")
  print(f"Âm thanh: {animal.sound}")
  animal.make_sound()
  print("--------------------\n")