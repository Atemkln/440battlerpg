import functions,random

class Generic:
    def __init__(self,name,moveset,temporarystats,passiveeffects,subjects,health,maxhealth,attack,defense,speed,intelligence,charisma,
                alcoholtolerance,weedtolerance,critical,guardbreak):
        self.name = name
        self.moveset = moveset
        self.temporarystats = temporarystats
        self.passiveffects = passiveeffects
        self.subjects = subjects
        self.health = health
        self.maxhealth = maxhealth
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.intelligence = intelligence
        self.charisma = charisma
        self.alcoholtolerance = alcoholtolerance
        self.weedtolerance = weedtolerance
        self.critical = critical
        self.guardbreak = guardbreak

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
        else:
            options[choice](self,self.subjects)

    def personalchecks(self,enemy):
        None
