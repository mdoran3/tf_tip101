class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types.append(new_type)

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()