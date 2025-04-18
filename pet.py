class Pet:
    def __init__(self, name, hunger, energy, happiness):
        self.name = name
        self.hunger = max(0, min(10, hunger)) 
        self.energy = max(0, min(10, energy))
        self.happiness = max(0, min(10, happiness))
        self.tricks = []
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        return f"{self.name} ate. Hunger ↓, Happiness ↑"
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        return f"{self.name} slept. Energy ↑↑"
    
    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            return f"{self.name} played happily!"
        return f"{self.name} is too tired to play!"
    
    def get_status(self):
        return (f"\n{self.name}'s Status:\n"
                f"Hunger: {self.hunger}/10 (0 = full)\n"
                f"Energy: {self.energy}/10 (10 = energetic)\n"
                f"Happiness: {self.happiness}/10")
    
    def train(self, trick):
        if self.energy >= 3:
            self.energy -= 3
            self.tricks.append(trick)
            return f"{self.name} learned: {trick}!"
        return f"{self.name} needs more energy to train!"
    
    def show_tricks(self):
        if not self.tricks:
            return f"{self.name} hasn't learned any tricks yet."
        return "Known tricks:\n" + "\n".join(f"- {trick}" for trick in self.tricks)

def create_pet():
    print("Let's create your pet!")
    name = input("Pet name: ").strip()
    
    while True:
        try:
            hunger = int(input("Starting hunger (0-10 where 0=full): "))
            energy = int(input("Starting energy (0-10 where 10=energetic): "))
            happiness = int(input("Starting happiness (0-10): "))
            
            if all(0 <= x <= 10 for x in (hunger, energy, happiness)):
                return Pet(name, hunger, energy, happiness)
            print("Please enter values between 0-10!")
        except ValueError:
            print("Please enter whole numbers only!")