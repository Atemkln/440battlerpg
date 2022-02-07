import engine,random,sys

def basicattack(player,enemy):
    critical = random.randint(1,10)
    guardbreak = random.randint(1,10)
    attackmod = random.randint(1,5)
    attackvalue = player.attack + attackmod 
    if critical > player.critical:
        attackvalue *= 2
        engine.display(f"{player.name} has scored a critical hit!")
    if guardbreak > player.guardbreak:
        engine.display(f"{player.name} has broken through {enemy.name}'s GUARD!")
    else:
        attackvalue -= enemy.defense
    if attackvalue < 0:
        attackvalue = 0
    engine.display(f"{player.name} hits {enemy.name} for {attackvalue} DAMAGE!")
    takedamage(enemy,player,attackvalue)

def basicdefend(player):
    defendmod = random.randint(1,10)
    statincrease(player,"DEFENSE",defendmod) 
    player.temporarystats["DEFENSE"] = [defendmod,1]
    engine.display(f"{player.name} raises his defense by {defendmod} for 1 TURN!")

def chugbeer(player):
    beerchoice = random.choice(["BUDWEISER","MOLSON","MOOSEHEAD","TSING TAO","SLEEMAN","LABATT BLUE"])
    engine.display(f"{player.name} chugs a shtein of {beerchoice}!")
    engine.display("*burp*")
    engine.display("CHARISMA, ATTACK, and DEFENSE all increase by 1...")
    statincrease(player,"CHARISMA",1)
    statincrease(player,"ATTACK",1)
    statincrease(player,"DEFENSE",1)
    drunk = 10 - player.alcoholtolerance
    engine.display(f"But {player.name} loses some brain cells in the process :(")
    engine.display(f"{player.name}'s INTELLIGENCE is reduced by {drunk}!")
    intelligencedecrease(player,drunk)

def smokeweed(player):
    engine.display(f"{player.name} balls up in the foyer...")
    engine.pause()
    engine.display(f"{player.name} is now HIGH,")
    engine.display("CHARISMA and HEALTH increase by 2...")
    statincrease(player,"CHARISMA",2)
    healthincreasecheck(player,100,2)
    high = 10 - player.weedtolerance
    engine.display(f"But {player.name} slows the fuck down in the process :(")
    engine.display(f"{player.name}'s SPEED is reduced by {high}!")
    speeddecrease(player,high)

def study(player,subjects):
    studymod = player.intelligence
    studymod //= 2
    subjectchoice = random.choice(["PHYSICS","GEOGRAPHY","MATH","KINESIOLOGY","BIOLOGY"])
    subjectvalues = {
        "PHYSICS":[f"{player.name} gets down with some {subjectchoice}!","ATTACK"],
        "GEOGRAPHY":[f"{player.name} brushes up on some {subjectchoice}!","SPEED"],
        "MATH":[f"{player.name} grinds out 3 hours of {subjectchoice}!","INTELLIGENCE"],
        "KINESIOLOGY":[f"{player.name} gets up to date on their {subjectchoice}!","DEFENSE"],
        "BIOLOGY":[f"{player.name} delves into some {subjectchoice}!","ALCOHOL TOLERANCE"]
    }
    engine.display(f"{player.name} heads to Stauff for a study sesh...")
    engine.pause()
    for i in subjectvalues:
        if i == subjectchoice:
            engine.display(subjectvalues[i][0])
            if subjectchoice in subjects:
                engine.display(f"{player.name} gets a +3 bonus to STUDYING this SUBJECT!")
                studymod += 3
            statincrease(player,subjectvalues[i][1],studymod)
            engine.display(f"{subjectvalues[i][1]} increases by {studymod}!")

def deathcheck(winner,loser):
    if loser.health <= 0:
        engine.display(f"{loser.name} has been DEFEATED!")
        engine.display(f"{winner.name} is now smoking that {loser.name} pack")
        engine.pause()
        engine.display("#PACKWATCH")
        engine.pause()
        engine.display("#RIPBOZO")
        sys.exit()

def healthincreasecheck(player,maxhealth,healthincrease):
    player.health += healthincrease
    check = player.health - maxhealth
    if check > 0:
        player.health = maxhealth

def defensedecrease(player,statdecrease):
    player.defense -= statdecrease
    if player.defense < 0:
        player.defense = 0

def intelligencedecrease(player,statdecrease):
    player.intelligence -= statdecrease
    if player.intelligence < 0:
        player.intelligence = 0

def speeddecrease(player,statdecrease):
    player.speed -= statdecrease
    if player.speed < 0:
        player.speed = 0

def charismadecrease(player,statdecrease):
    player.charisma -= statdecrease
    if player.charisma < 0:
        player.charisma = 0

def attackdecrease(player,statdecrease):
    player.attack -= statdecrease
    if player.attack < 0:
        player.attack = 0

def alcoholtolerancedecrease(player,statdecrease):
    player.alcoholtolerance -= statdecrease
    if player.alcoholtolerance < 0:
        player.alcoholtolerance = 0

def weedtolerancedecrease(player,statdecrease):
    player.weedtolerance -= statdecrease
    if player.weedtolerance < 0:
        player.weedtolerance = 0

def statincrease(player,stat,increase):
    if stat == "ATTACK":
        player.attack += increase
    elif stat == "DEFENSE":
        player.defense += increase
    elif stat == "SPEED":
        player.speed += increase
    elif stat == "INTELLIGENCE":
        player.intelligence += increase
    elif stat == "CHARISMA":
        player.charisma += increase
    elif stat == "ALCOHOL TOLERANCE":
        player.alcoholtolerance += increase
    else:
        player.weedtolerance += increase

def statdecrease(player,stat,decrease):
    if stat == "ATTACK":
        attackdecrease(player,decrease)
    elif stat == "DEFENSE":
        defensedecrease(player,decrease)
    elif stat == "SPEED":
        speeddecrease(player,decrease)
    elif stat == "INTELLIGENCE":
        intelligencedecrease(player,decrease)
    elif stat == "CHARISMA":
        charismadecrease(player,decrease)
    elif stat == "ALCOHOL TOLERANCE":
        alcoholtolerancedecrease(player,decrease)
    else:
        weedtolerancedecrease(player,decrease)  

def takedamage(player,enemy,damage):
    player.health -= damage
    deathcheck(enemy,player)

def temporarycheck(player):
    tobedeleted = []
    if player.temporarystats != {}:
        for i in player.temporarystats:
            player.temporarystats[i][1] -= 1
            if player.temporarystats[i][1] <= 0:
                tobedeleted.append(i)
        for i in tobedeleted:
            if i == "DEFENSE":
                player.defense -= player.temporarystats[i][0]
            elif i == "ATTACK":
                player.attack -= player.temporarystats[i][0]
            elif i == "SPEED":
                player.speed -= player.temporarystats[i][0]
            elif i == "INTELLIGENCE":
                player.intelligence -= player.temporarystats[i][0]
            elif i == "CHARISMA":
                player.charisma -= player.temporarystats[i][0]
            elif i == "ALCOHOL TOLERANCE":
                player.alcoholtolerance -= player.temporarystats[i][0]
            elif i == "WEED TOLERANCE":
                player.weedtolerance -= player.temporarystats[i][0]
            elif i == "CRITICAL":
                player.critical -= player.temporarystats[i][0]
            elif i == "ALLISON GREEN":
                player.allisongreen = False
            else:
                player.guardbreak -= player.temporarystats[i][0]
            del player.temporarystats[i]

