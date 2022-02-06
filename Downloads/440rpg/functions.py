from msilib.schema import Class
import engine,random

def basicattack(player,enemy):
    attackmod = random.randint(1,5)
    attackvalue = player.attack + attackmod - player.defense
    enemy.health -= attackvalue
    engine.display(f"{player.name} hits {enemy.name} for {attackvalue} DAMAGE!")
    deathcheck(player,enemy)

def basicdefend(player):
    defendmod = random.randint(1,10)
    player.defense += defendmod
    engine.display(f"{player.name} raises his defense by {defendmod} for 1 TURN!")
    return defendmod

def chugbeer(player):
    beerchoice = random.choice(["BUDWEISER","MOLSON","MOOSEHEAD","TSING TAO","SLEEMAN","LABATT BLUE"])
    engine.display(f"{player.name} chugs a shtein of {beerchoice}!")
    engine.display("*burp*")
    engine.display("CHARISMA, ATTACK, and HEALTH all increase by 1...")
    player.charisma += 1
    player.health += 1
    player.attack += 1
    drunk = 10 - player.alcoholtolerance
    engine.display(f"But {player.name} loses some brain cells in the process :(")
    engine.display(f"{player.name}'s INTELLIGENCE is reduced by {drunk}!")
    intelligencedecrease(player,drunk)

def smokeweed(player):
    engine.display(f"{player.name} balls up in the foyer...")
    engine.pause()
    engine.display(f"{player.name} is now HIGH,")
    engine.display("DEFENSE, CHARISMA, and HEALTH all increase by 1...")
    player.defense += 1
    player.charisma += 1
    player.health += 1
    high = 10 - player.weedtolerance
    engine.display(f"But {player.name} slows the fuck down in the process :(")
    engine.display(f"{player.name}'s SPEED is reduced by {high}!")
    speeddecrease(player,high)

def study(player):
    subjectchoice = random.choice(["PHYSICS","GEOGRAPHY","MATH","KINESIOLOGY","BIOLOGY"])
    engine.display(f"{player.name} heads to Stauff for a study sesh...")
    studymod = random.randint(1,3) + player.intelligence
    studymod //= 3
    engine.pause()
    if subjectchoice == "PHYSICS":
        engine.display(f"{player.name} gets down with some {subjectchoice}!")
        engine.display(f"ATTACK increases by {studymod}")
        player.attack += studymod
    elif subjectchoice == "GEOGRAPHY":
        engine.display(f"{player.name} brushes up on some {subjectchoice}!")
        engine.display(f"SPEED increases by {studymod}")
        player.speed += studymod
    elif subjectchoice == "MATH":
        engine.display(f"{player.name} grinds out 3 hours of {subjectchoice}!")
        engine.display(f"INTELLIGENCE increases by {studymod}")
        player.intelligence += studymod  
    elif subjectchoice == "KINESIOlOGY":
        engine.display(f"{player.name} gets up to date on their {subjectchoice}!")
        engine.display(f"DEFENSE increases by {studymod}")
        player.defense += studymod  
    else:
        engine.display(f"{player.name} delves into some {subjectchoice}!")
        engine.display(f"HEALTH increases by {studymod}")
        player.defense += studymod          

def deathcheck(winner,loser):
    if loser.health <= 0:
        engine.display(f"{loser.name} has been DEFEATED!")
        engine.display(f"{winner.name} is now smoking that {loser.name} pack")
        engine.pause()
        engine.display("#PACKWATCH")
        engine.pause()
        engine.display("#RIPBOZO")

def healthincreasecheck(player,maxhealth,healthincrease):
    player.health += healthincrease
    check = player.health - maxhealth
    if check > 0:
        player.health = maxhealth

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