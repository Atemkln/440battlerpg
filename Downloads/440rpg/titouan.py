import engine,random

class Titouan:
    def __init__(self,name,health,attack,defense,speed,intelligence,charisma,alcoholtolerance,weedtolerance,blunt):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.intelligence = intelligence
        self.charisma = charisma
        self.alcoholtolerance = alcoholtolerance
        self.weedtolerance = weedtolerance
        self.blunt = blunt

    def crossover(self,enemy):
        engine.display(f"Titouan attempts to break {enemy.name}'s ankles!")
        engine.display("'Lets go motherfucker!'")
        engine.waitresult()
        if self.speed > enemy.speed:
            engine.display(f"{enemy.name} got sauced on expeditiously...")
            engine.display("'Get crossed betch!'")
            engine.display(f"{enemy.name}'s CHARISMA and INTELLIGENCE are reduced by 1!")
            enemy.speed -= 1
            enemy.intelligence -= 1
        elif self.speed == enemy.speed:
            engine.display(f"{enemy.name} challenges the crossover!")
            coinchoice = engine.display(f"Titouan, choose heads or tails(1 or 2): ",get=1)  
            engine.waitresult()      
            cointoss = random.choice(["1","2"])
            if cointoss == coinchoice and coinchoice == "1":
                engine.display("Heads!")
                engine.display("Titouan wins the cointoss")
                engine.display(f"{enemy.name}'s SPEED is reduced by 1!")
            elif cointoss == coinchoice and coinchoice == "2":
                engine.display("Tails!")
                engine.display("Titouan wins the cointoss")
                engine.display(f"{enemy.name}'s SPEED is reduced by 1!")
            elif cointoss == "1" :
                engine.display("Heads!")
                engine.display(f"{enemy.name} wins the cointoss")
                engine.display("Titouan's SPEED is reduced by 1!")
            else:
                engine.display("Tails!")
                engine.display(f"{enemy.name} wins the cointoss")
                engine.display("Titouan's SPEED is reduced by 1!")
        else:
            engine.display(f"{enemy.name} is on you with the quickness lmao...")
            engine.display(f"Titouan got catastrophically clowned on :P")
            engine.display("He takes 5 DAMAGE!")
            self.health -= 5
            engine.display("And his BLUNT is destroyed in the process :(")
            self.blunt == False
        return 0

    def rollblunt(self):
        engine.display("Titouan rolls a fatty BLUNT...")
        engine.waitresult()
        engine.display("'Yo, anybody tryna smoke?'")
        engine.display("The BLUNT has been prepped!")
titouan = Titouan(
    "Titouan",  #name
    100,        #health
    10,         #attack
    7,          #defense
    5,          #speed
    6,          #intelligence
    4,          #charisma
    3,          #alcoholtolerance
    10,          #weedtolerance
    False,       #blunt
    )

test = Titouan(
    "Eric",     #name
    100,        #health
    10,         #attack
    7,          #defense
    5,          #speed
    6,          #intelligence
    4,          #charisma
    3,          #alcoholtolerance
    10,
    False,          #weedtolerance
    )

titouan.crossover(test)