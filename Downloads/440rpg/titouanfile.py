import engine,random,functions

class Titouan:
    def __init__(self,name,moveset,temporarystats,subjects,health,maxhealth,attack,defense,speed,intelligence,charisma,
                alcoholtolerance,weedtolerance,critical,guardbreak,blunt,bluntattribute,highstate,defazzcheck,):
        self.name = name
        self.moveset = moveset
        self.temporarystats = temporarystats
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
        self.blunt = blunt
        self.bluntattribute = bluntattribute
        self.highstate = highstate
        self.defazzcheck = defazzcheck

    def combatmenu(self):
        print("-----------------------------------------------------------------")
        print(f"{self.name} STATS:                            {self.name} MOVES:")
        print("")
        print(f"HEALTH: {self.health}                                   1. ATTACK")
        print(f"ATTACK: {self.attack}                                    2. DEFEND")
        print(f"DEFENSE: {self.defense}                                    3. CHUG BEER")
        print(f"SPEED: {self.speed}                                      4. SMOKE WEED")
        print(f"INTELLGENCE: {self.intelligence}                                5. STUDY")
        print(f"CHARISMA: {self.charisma}                                   6. {self.moveset[0]}")                                 
        print(f"ALCOHOL TOLERANCE: {self.alcoholtolerance}                          7. {self.moveset[1]}")
        print(f"WEED TOLERANCE: {self.weedtolerance}                            8. {self.moveset[2]}")
        print(f"                                              9. {self.moveset[3]}")
        print(f"                                              10. {self.moveset[4]}") 
        print("")

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
        elif choice == "2" or choice == "3" or choice == "4":
            options[choice](self)
        elif choice == "5":
            options[choice](self,self.subjects)
        elif choice == "6" or choice == "10":
            options[choice](enemy)
        else:
            options[choice]()

    def crossover(self,enemy):
        engine.display(f"{self.name} attempts to break {enemy.name}'s ankles!")
        engine.waitresult()
        if self.speed > enemy.speed:
            engine.display(f"{enemy.name} got sauced on expeditiously...")
            engine.display(f"{enemy.name}'s CHARISMA and INTELLIGENCE are reduced by 2!")
            functions.charismadecrease(enemy,2)
            functions.intelligencedecrease(enemy,2)
        elif self.speed == enemy.speed:
            engine.display(f"{enemy.name} challenges the crossover!")
            coinchoice = engine.display(f"{self.name}, choose heads or tails(1 or 2): ",get=1)  
            engine.waitresult()      
            cointoss = random.choice(["1","2"])
            if cointoss == coinchoice and coinchoice == "1":
                engine.display("Heads!")
                engine.display(f"{self.name} wins the cointoss")
                engine.display(f"{enemy.name}'s SPEED is reduced by 1!")
                functions.speeddecrease(enemy,1)
            elif cointoss == coinchoice and coinchoice == "2":
                engine.display("Tails!")
                engine.display(f"{self.name}wins the cointoss")
                engine.display(f"{enemy.name}'s SPEED is reduced by 1!")
                functions.speeddecrease(enemy,1)                
            elif cointoss == "1" :
                engine.display("Heads!")
                engine.display(f"{enemy.name} wins the cointoss")
                engine.display(f"{self.name}'s SPEED is reduced by 1!")
                functions.speeddecrease(self,1) 
            else:
                engine.display("Tails!")
                engine.display(f"{enemy.name} wins the cointoss")
                engine.display(f"{self.name}'s SPEED is reduced by 1!")
                functions.speeddecrease(self,1) 
        else:
            engine.display(f"{enemy.name} is on you with the quickness lmao...")
            engine.display(f"{self.name} got catastrophically clowned on :P")
            engine.display("He takes 5 DAMAGE!")
            functions.takedamage(self,enemy,5)
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
        engine.display(f"{self.name} rolls a fatty BLUNT...")
        engine.waitresult()
        engine.display("The BLUNT has been prepped!")
        engine.display(f"It appears to be {self.bluntattribute}-tier quality...")

    def sesh(self):
        if self.blunt == True:
            engine.display(f"{self.name} smokes his {self.bluntattribute} BLUNT!")
            if self.bluntattribute == "SHIT":
                engine.display("It's pretty SHIT...")
                engine.display(f"Nevertheless, {self.name} is now SUPER HIGH")
                self.highstate = "SUPER HIGH"
                engine.display("He will take 10 less DAMAGE for the next 5 TURNS...")
                functions.statincrease(self,"DEFENSE",10)
                self.temporarystats["DEFENSE"] = [10,5]
            elif self.bluntattribute == "MEH":
                engine.display("It's pretty MEH...")
                engine.display(f"Who cares though lol, {self.name} is now HIGH AF")
                self.highstate = "SUPER HIGHSTATE"
                engine.display("He will take 10 less DAMAGE for the next 5 TURNS,\nAnd his ATTACK will be increased by 10 for the next 5 TURNS")
                functions.statincrease(self,"DEFENSE",10)
                functions.statincrease(self,"ATTACK",10)
                self.temporarystats["DEFENSE"] = [10,5]
                self.temporarystats["ATTACK"] = [10,5]
            else:
                engine.display("It is absolutely GOD-tier!")
                engine.display(f"{self.name} becomes STUPID HIGH!")
                self.highstate = "SUPER HIGH"
                engine.highstate = "A new plane of understanding has been unlocked!"
                engine.display("He will take 10 less DAMAGE for the next 5 TURNS,\nHis ATTACK will be increased by 10 for the next 5 TURNS\nAnd he unlocks his DEFAZZ SPECIAL MOVE!")
                functions.statincrease(self,"DEFENSE",10)
                functions.statincrease(self,"ATTACK",10)
                self.temporarystats["DEFENSE"] = [10,5]
                self.temporarystats["ATTACK"] = [10,5]    
                self.defazzcheck = True   
            self.blunt = False 
        else:
            engine.display("Roll a blunt first, bozo LMAO")
            engine.display("Lose a turn.")

    def freshfade(self):
        engine.display(f"self.name obtains the freshest of FADES!")
        engine.display("His HEALTH increases by 5,\nAnd his CHARISMA increases by 1!")
        functions.statincrease(self,"CHARISMA",1)
        functions.healthincreasecheck(self,100,5)

    def defazz(self,enemy):
        if self.defazzcheck == True:
            engine.display("Prepare...")
            engine.pause()
            engine.display(f"{enemy.name}!")
            engine.pause()
            engine.display(f"You are about to face {self.name}'s ultimate ATTACK!")
            engine.pause()
            engine.display("DEFAZZ! Go!")
            engine.display(f"{enemy.name}, you have been hit by a rude DEFAZZ!")
            engine.display(f"You take a whopping 50 DAMAGE,\nAnd {self.name} nizes your next TURN...")
            engine.display("Wouldn't wanna be ya lmao XD")
            functions.takedamage(enemy,self,50)
            self.defazzcheck = False
            self.combatmenu()
            self.movechoice(enemy)
        else:
            engine.display("You aren't HIGH enough to do that lol")
            engine.display("Lose a turn.")
    
titouan = Titouan(
    "Titouan",  #name
    ["CROSSOVER","ROLL BLUNT","SESH","FRESH FADE","DEFAZZ"], #moveset
    {},      #temporarystats
    ["KINESIOLOGY"], #subjects
    100,        #health
    100,        #maxhealth
    10,         #attack
    7,          #defense
    5,          #speed
    6,          #intelligence
    4,          #charisma
    3,          #alcoholtolerance
    10,         #weedtolerance
    8,          #critical
    8,          #guardbreak
    False,      #blunt
    "SHIT",         #bluntaatribute
    "SUPER HIGH",         #highstate
    False      #defazzcheck
    )
