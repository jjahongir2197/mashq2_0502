class Startup:
    def __init__(self, name, valuation):
        self.name = name
        self.valuation = valuation
        self.investors = []

    def receive_investment(self, investor, amount):
        self.investors.append((investor, amount))
        self.valuation += amount
        print(f"{investor} {amount} so‘m sarmoya kiritdi")

    def info(self):
        return f"{self.name} | Valuation: {self.valuation} | Investors: {len(self.investors)}"


class VentureCapital:
    def __init__(self):
        self.startups = []

    def add_startup(self, s):
        self.startups.append(s)

    def list_startups(self):
        for i, s in enumerate(self.startups):
            print(i, s.info())


vc = VentureCapital()
vc.add_startup(Startup("Techify", 5000000))
vc.add_startup(Startup("EduPro", 3000000))

while True:
    print("\n1.Startup 2.Sarmoya 3.Ro‘yxat 0.Exit")
    c = input(">>> ")

    if c == "1":
        vc.add_startup(Startup(input("Nomi: "), int(input("Bahosi: "))))
    elif c == "2":
        vc.startups[int(input("Index: "))].receive_investment(input("Investor: "), int(input("Summasi: ")))
    elif c == "3":
        vc.list_startups()
    elif c == "0":
        break
