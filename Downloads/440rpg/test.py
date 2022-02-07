import functions,random

class Dummy:
    def __init__(self,name,moveset,subjects,health,attack,defense,speed,intelligence,charisma,
                alcoholtolerance,weedtolerance,temporarystats):
        self.name = name
        self.moveset = moveset
        self.subjects = subjects
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.intelligence = intelligence
        self.charisma = charisma
        self.alcoholtolerance = alcoholtolerance
        self.weedtolerance = weedtolerance
        self.temporarystats = temporarystats

    def combatmenu(self):
        print("-----------------------------------------------------------------")
        print(f"{self.name} STATS:                            {self.name} MOVES:")
        print("")
        print(f"HEALTH: {self.health}                                   1. ATTACK")
        print(f"ATTACK: {self.attack}                                    2. DEFEND")
        print(f"DEFENSE: {self.defense}                                   3. CHUG BEER")
        print(f"SPEED: {self.speed}                                     4. SMOKE WEED")
        print(f"INTELLGENCE: {self.intelligence}                               5. STUDY")
        print("")

    def movechoice(self,enemy):
        choice = random.choice(["1","2","3","4","5"])
        options = {
            "1":functions.basicattack,
            "2":functions.basicdefend,
            "3":functions.chugbeer,
            "4":functions.smokeweed,
            "5":functions.study
        }
        if choice == "1":
            options[choice](self,enemy)
        elif choice == "2" or choice == "3" or choice == "4":
            options[choice](self)
        elif choice == "5":
            options[choice](self,self.subjects)
        elif choice == "6" or choice == "10":
            options[choice](enemy)
        else:
            options[choice]()

dummy = Dummy(
"John",
[""],
[],
80,
7,
6,
8,
6,
7,
10,
2,
{}
)
