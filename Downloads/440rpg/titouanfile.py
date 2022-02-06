import engine,random,functions

class Titouan:
    def __init__(self,name,moveset,health,attack,defense,speed,intelligence,charisma,
                alcoholtolerance,weedtolerance,blunt,bluntattribute,highstate,defazzcheck):
        self.name = name
        self.moveset = moveset
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.intelligence = intelligence
        self.charisma = charisma
        self.alcoholtolerance = alcoholtolerance
        self.weedtolerance = weedtolerance
        self.blunt = blunt
        self.bluntattribute = bluntattribute
        self.highstate = highstate
        self.defazzcheck = defazzcheck

    def crossover(self,enemy):
        engine.display(f"Titouan attempts to break {enemy.name}'s ankles!")
        engine.waitresult()
        if self.speed > enemy.speed:
            engine.display(f"{enemy.name} got sauced on expeditiously...")
            engine.display(f"{enemy.name}'s CHARISMA and INTELLIGENCE are reduced by 1!")
            functions.charismadecrease(enemy,1)
            functions.intelligencedecrease(enemy,1)
        elif self.speed == enemy.speed:
            engine.display(f"{enemy.name} challenges the crossover!")
            coinchoice = engine.display(f"Titouan, choose heads or tails(1 or 2): ",get=1)  
            engine.waitresult()      
            cointoss = random.choice(["1","2"])
            if cointoss == coinchoice and coinchoice == "1":
                engine.display("Heads!")
                engine.display("Titouan wins the cointoss")
                engine.display(f"{enemy.name}'s SPEED is reduced by 1!")
                functions.speeddecrease(enemy,1)
            elif cointoss == coinchoice and coinchoice == "2":
                engine.display("Tails!")
                engine.display("Titouan wins the cointoss")
                engine.display(f"{enemy.name}'s SPEED is reduced by 1!")
                functions.speeddecrease(enemy,1)                
            elif cointoss == "1" :
                engine.display("Heads!")
                engine.display(f"{enemy.name} wins the cointoss")
                engine.display("Titouan's SPEED is reduced by 1!")
                functions.speeddecrease(self,1) 
            else:
                engine.display("Tails!")
                engine.display(f"{enemy.name} wins the cointoss")
                engine.display("Titouan's SPEED is reduced by 1!")
                functions.speeddecrease(self,1) 
        else:
            engine.display(f"{enemy.name} is on you with the quickness lmao...")
            engine.display(f"Titouan got catastrophically clowned on :P")
            engine.display("He takes 5 DAMAGE!")
            self.health -= 5
            functions.deathcheck(enemy,self)
            engine.display("And his BLUNT is destroyed in the process :(")
            self.blunt = False

    def rollblunt(self):
        self.blunt = True
        choice = random.randint(1,10)
        if choice <= 6:
            self.bluntattribute = "SHIT"
        elif choice <= 8:
            self.bluntattribute = "MEH"
        else:
            self.bluntattribute = "GOD"
        engine.display("Titouan rolls a fatty BLUNT...")
        engine.waitresult()
        engine.display("The BLUNT has been prepped!")
        engine.display(f"It appears to be {self.bluntattribute}-tier quality...")

    def sesh(self):
        if self.blunt == True:
            engine.display(f"Titouan smokes his {self.bluntattribute} BLUNT!")
            if self.bluntattribute == "SHIT":
                engine.display("It's pretty SHIT...")
                engine.display("Nevertheless, Titouan is now SUPER HIGH")
                self.highstate = "SUPER HIGH"
                engine.display("He will take 10 less DAMAGE for the next 5 TURNS...")
            elif self.bluntattribute == "MEH":
                engine.display("It's pretty MEH...")
                engine.display("Who cares though lol, Titouan is now HIGH AF")
                self.highstate = "SUPER HIGHSTATE"
                engine.display("He will take 10 less DAMAGE for the next 5 TURNS,\nAnd his ATTACK will be increased by 10 for the next 5 TURNS")
            else:
                engine.display("It is absolutely GOD-tier!")
                engine.display("Titouan becomes STUPID HIGH!")
                self.highstate = "SUPER HIGH"
                engine.highstate = "A new plane of understanding has been unlocked!"
                engine.display("He will take 10 less DAMAGE for the next 5 TURNS,\nHis ATTACK will be increased by 10 for the next 5 TURNS\nAnd he unlocks his DEFAZZ SPECIAL MOVE!")
        else:
            engine.display("Roll a blunt first, bozo LMAO")
            engine.display("Lose a turn.")

    def freshfade(self):
        engine.display("Titouan obtains the freshest of FADES!")
        engine.display("His HEALTH increases by 5,\nAnd his CHARISMA increases by 1!")
        self.charisma += 1
        functions.healthincreasecheck(self,100,5)

    def defazz(self,enemy):
        if self.defazzcheck == True:
            engine.display("Prepare...")
            engine.pause()
            engine.display(f"{enemy.name}!")
            engine.pause()
            engine.display("You are about to face Titouan's ultimate ATTACK!")
            engine.pause()
            engine.display("DEFAZZ! Go!")
            engine.display(f"{enemy.name}, you have been hit by a rude DEFAZZ!")
            engine.display("You take a whopping 50 DAMAGE,\nAnd Titouan nizes your next TURN...")
            enemy.health -= 50
            engine.display("Wouldn't wanna be ya lmao XD")
            functions.deathcheck(self,enemy)
        else:
            engine.display("You aren't HIGH enough to do that lol")
            engine.display("Lose a turn.")
    
    def combatmenu(self):
        print("     -------------     ")
        print(f"{self.name} STATS:")
        print("")
        print(f"HEALTH: {self.health}")
        print(f"ATTACK: {self.attack}")
        print(f"DEFENSE: {self.defense}")
        print(f"SPEED: {self.speed}")
        print(f"INTELLGENCE: {self.intelligence}")
        print(f"CHARISMA: {self.charisma}")
        print(f"ALCOHOL TOLERANCE: {self.alcoholtolerance}")
        print(f"WEED TOLERANCE: {self.weedtolerance}")
        print("     -------------     ")
        print(f"{self.name} MOVE OPTIONS:")
        print("")
        print(f"1. ATTACK")
        print(f"2. DEFEND")
        print(f"3. CHUG BEER")
        print(f"4. SMOKE WEED")
        print(f"5. STUDY")
        for i in range(len(self.moveset)):
            print(f"{i+6}. {self.moveset[i]}")
        print("     -------------     ")

    def movechoice(self,enemy):
        options = {
            "1":functions.basicattack,
            "2":functions.basicdefend,
            "3":functions.chugbeer,
            "4":functions.smokeweed,
            "5":functions.study,
            "6":self.crossover,
            "7":self.rollblunt,
            "8":self.sesh,
            "9":self.freshfade,
            "10":self.defazz
            }
        choice = engine.display("What will you do?: ",get=2,amount=len(self.moveset))
        if choice == "1":
            options[choice](self,enemy)
        elif choice == "2" or choice == "3" or choice == "4" or choice == "5":
            options[choice](self)
        elif choice == "6" or choice == "10":
            options[choice](enemy)
        else:
            options[choice]()


titouan = Titouan(
    "Titouan",  #name
    ["CROSSOVER","ROLL BLUNT","SESH","FRESH FADE","DEFAZZ"], #moveset
    100,        #health
    10,         #attack
    7,          #defense
    5,          #speed
    6,          #intelligence
    4,          #charisma
    3,          #alcoholtolerance
    10,         #weedtolerance
    False,      #blunt
    "SHIT",         #bluntaatribute
    "SUPER HIGH",         #highstate
    False,      #defazzcheck
    )

testenemy = Titouan(
    "Eric",  #name
    ["CROSSOVER","ROLL BLUNT","SESH","FRESH FADE","DEFAZZ"], #moveset
    50,        #health
    10,         #attack
    7,          #defense
    5,          #speed
    6,          #intelligence
    4,          #charisma
    3,          #alcoholtolerance
    10,         #weedtolerance
    False,      #blunt
    "SHIT",         #bluntaatribute
    "SUPER HIGH",         #highstate
    False       #defazzcheck
    )
