import engine,random,functions

class John:
    def __init__(self,name,moveset,temporarystats,passiveeffects,subjects,health,maxhealth,attack,defense,speed,intelligence,charisma,
                alcoholtolerance,weedtolerance,critical,guardbreak,allisongreen,money,tipstatus):
        self.name = name
        self.moveset = moveset
        self.temporarystats = temporarystats
        self.passiveeffects = passiveeffects
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
        self.allisongreen = allisongreen
        self.money = money
        self.tipstatus = tipstatus

    def combatmenu(self):
        print("-----------------------------------------------------------------")
        print(f"{self.name} STATS:                            {self.name} MOVES:")
        print("")
        print(f"HEALTH: {self.health}                                   1. ATTACK")
        print(f"ATTACK: {self.attack}                                    2. DEFEND")
        print(f"DEFENSE: {self.defense}                                   3. CHUG BEER")
        print(f"SPEED: {self.speed}                                    4. SMOKE WEED")
        print(f"INTELLGENCE: {self.intelligence}                               5. STUDY")
        print(f"CHARISMA: {self.charisma}                                  6. {self.moveset[0]}")                                 
        print(f"ALCOHOL TOLERANCE: {self.alcoholtolerance}                        7. {self.moveset[1]}")
        print(f"WEED TOLERANCE: {self.weedtolerance}                            8. {self.moveset[2]}")
        print(f"MONEY: {self.money}                                   9. {self.moveset[3]}")
        print(f"                                             10. {self.moveset[4]}") 
        print("")

    def movechoice(self,enemy):
            options = {
                "1":functions.basicattack,
                "2":functions.basicdefend,
                "3":functions.chugbeer,
                "4":functions.smokeweed,
                "5":functions.study,
                "6":self.customerservice,
                "7":self.gourmetmeal,
                "8":self.greygoose,
                "9":self.ohmygodjohn,
                "10":self.extravaganttip
                }
            choice = engine.display("What will you do?: ",get=2,amount=len(self.moveset))
            if choice == "1":
                options[choice](self,enemy)
            elif choice == "2" or choice == "3" or choice == "4":
                options[choice](self)
            elif choice == "5":
                options[choice](self,self.subjects)
            else: 
                options[choice](enemy)
           
    def customerservice(self,enemy):
        engine.display("...*ring*...*ring*...")
        engine.pause()
        engine.display(f"{self.name} is on the phone with customer service rep {enemy.name}!")
        engine.display("...*ring*...*ring*...")
        engine.pause()
        if self.charisma > enemy.charisma:
            engine.display(f"{enemy.name} is no match for his assertiveness!")   
            engine.display(f"{self.name} STUNS {enemy.name} for 1 turn!")
            engine.display(f"But {self.name}'s CHARISMA decreases by 2 due to self reflection...")
            functions.statdecrease(self,"CHARISMA",2)
            functions.singleturn(self,enemy)
        else:
            engine.display(f"{enemy.name} is shackled by corporate policy!")
            engine.display("They are unable to accomodate him! :(")
            engine.display(f"{self.name} loses 10 HEALTH, and {enemy.name} gains 10 HEALTH!")
            functions.takedamage(self,enemy,10)
            functions.healthincreasecheck(enemy,enemy.maxhealth,10)

    def gourmetmeal(self,enemy):
        meal = random.choice(["HOOD STEW","STEAK FRITES","RATATOUILLE","FETTUCINE ALFREDO","BURNED SHIT"])
        engine.display(f"{self.name} chefs it up with some {meal}!")
        if meal == "HOOD STEW":
            engine.display("Devious!")
            functions.statincrease(self,"ATTACK",20)
            functions.statdecrease(self,"DEFENSE",20)
            self.temporarystats["ATTACK"] = [20,2]
            self.temporarystats["DEFENSE"] = [-20,2]
            engine.display("His ATTACK increases by 20 for two turns and his DEFENSE decreases by 20 for two TURNS...")
        elif meal == "STEAK FRITES":
            functions.healthincreasecheck(self,90,10)
            engine.display("How refined!")
            engine.display(f"{self.name} gains 10 HEALTH!")
        elif meal == "RATATOUILLE":
            engine.display("Exquisite!")
            engine.display(f"{enemy.name} takes a series of backhand chef slaps out of jealousy :P")
            self.slap(enemy)
            self.slap(enemy)
            self.slap(enemy)
        elif meal == "FETTUCINE ALFREDO":
            engine.display("This shit lowkey unhealthy...")
            engine.display(f"{self.name}'s MAX HEALTH increased by 20!")
            self.maxhealth += 20
        else:
            engine.display("The toxic fumes are incredibly DAMAGING!")
            engine.display(f"{self.name} takes 30 DAMAGE!")
            functions.takedamage(self,enemy,30)

    def slap(self,enemy):
        slapdamage = random.randint(1,7)
        engine.display(f"{enemy.name} got SLAPPED for {slapdamage} DAMAGE!")
        functions.takedamage(enemy,self,slapdamage)

    def greygoose(self,enemy):
        functions.statincrease(self,"CHARISMA",2)
        engine.display(f"{self.name} takes a shot of the good stuff...")
        engine.display("His CHARISMA increases by 2,")
        engine.display("But he takes 5 DAMAGE in his drunken stupor.")
        functions.takedamage(self,enemy,5)
        engine.display(f"{self.name} swings blindly at {enemy.name}!")
        engine.waitresult()
        choice = random.randint(1,2) 
        if choice == 1:
            engine.display(f"{self.name} takes 1 DAMAGE from punching himself in the face!")
            functions.takedamage(self,enemy,1)
        else:
            engine.display(f"{self.name} grazes {enemy.name} for a whopping 1 DAMAGE!")
            functions.takedamage(enemy,self,1)

    def ohmygodjohn(self,enemy):
        if self.allisongreen == False and self.money > 150:
            engine.display(f"OH MY GOD {self.name}!")
            engine.display(f"{self.name} is joined by ALLISON GREEN!")
            engine.display(f"ALLISON GREEN will fight alongside him against {enemy.name}!...")
            self.allisongreen = True
        else:
            engine.display("Invalid choice muchacho...")
            engine.display("Lose one turn.")

    def extravaganttip(self,enemy):
        if self.money > 0:
            engine.display(f"{self.name} tips {enemy.name} outrageously!")
            tipchoice = -1
            while True:
                tipchoice = input("What tip do you want to leave?($): ")
                try: 
                    int(tipchoice)
                except ValueError:
                    print("")
                    engine.display("Tip an actual number, bozo.")
                else:
                    tipchoice = int(tipchoice)
                    if tipchoice <= self.money and tipchoice > 0:
                        break
                    else:
                        print("")
                        engine.display("That aint in da budget, bozo lmao. Try again.")
            john.money -= tipchoice
            turnamount = random.randint(6,10)
            self.tipstatus["TIP"] = [tipchoice,turnamount]
            print("")
            engine.display(f"In {turnamount} turns, {enemy.name} will take {tipchoice} DAMAGE!")
            engine.display(f"And {self.name} will gain {tipchoice} HEALTH!")
            engine.display("But. He is exhausted from all this tipping, and loses a TURN.")
        functions.singleturn(enemy,self)

    def getdividend(self):
        dividend = random.randint(1,20)
        engine.display(f"{self.name} collects ${dividend} in DIVIDENDS!")
        self.money += dividend

    def tipdelivery(self,enemy):
        for i in self.tipstatus:
            self.tipstatus[i][1] -= 1
            if self.tipstatus[i][1] <= 0:
                engine.display(f"TIP delivery...")
                engine.display(f"{self.name} rains cash all over {enemy.name}!")
                engine.display(f"{enemy.name} is so shocked that they take {self.tipstatus[i][0]} DAMAGE!")
                engine.display(f"And {self.name}, just for shits and giggles, GAINS {self.tipstatus[i][0]} HEALTH!")
                functions.takedamage(enemy,self,self.tipstatus[i][0])
                functions.healthincreasecheck(self,self.maxhealth,self.tipstatus[i][0])
                del self.tipstatus[i]

    def personalchecks(self,enemy):
        self.getdividend()
        self.tipdelivery(enemy)
        if self.allisongreen == True and self.money >= 150:
            engine.display(f"{allisongreen.name} heals {self.name} for 5 HEALTH!")
            functions.healthincreasecheck(self,self.maxhealth,5)
            engine.display(f"{self.name}'s HEALTH is increased to {self.health}!")
            engine.display(f"{allisongreen.name} does 5 DAMAGE to {enemy.name}!")
            functions.takedamage(enemy,self,5)
            allisongreen.movechoice(enemy)

john = John(
    "John",  #name
    ["CUSTOMER SERVICE","GOURMET MEAL","GREY GOOSE","OH MY GOD JOHN","EXTRAVAGANT TIP"], #moveset
    {},      #temporarystats
    {},       #passiveeffects
    ["GEOGRAPHY"], #subjects
    90,        #health
    90,         #maxhealth
    6,         #attack
    5,          #defense
    10,          #speed
    5,          #intelligence
    8,          #charisma
    10,          #alcoholtolerance
    3,         #weedtolerance
    8,          #critical
    8,          #guardbreak
    False,       #allisongreen
    100,        #money
    {},         #tipstatus
    )

class AllisonGreenNPC:
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
            options[choice](john,enemy)
        elif choice == "2" or choice == "3" or choice == "4":
            options[choice](john)
        else:
            options[choice](john,john.subjects)

    def personalchecks(self,enemy):
        None

allisongreen = AllisonGreenNPC(
    "Allison Green",  #name
    [], #moveset
    {},      #temporarystats
    {},  #passiveeffects
    ["GEOGRAPHY"], #subjects
    50,        #health
    50,         #maxhealth
    7,         #attack
    3,          #defense
    6,          #speed
    5,          #intelligence
    7,          #charisma
    6,          #alcoholtolerance
    4,         #weedtolerance
    8,          #critical
    8,          #guardbreak
)