import engine,titouanfile,johnfile,time,functions,random

def intro(player1,player2):
    dialogue = ["...",player1.name,player2.name,"Fight hard...",
    "Fight clean...","Glory to the winner,","Humiliation for the loser.",
    "3...","2...","1...","FIGHT!"]
    for line in dialogue:
        engine.display(line)
        engine.pause()

def turnround(player1,player2):
    functions.temporarycheck(player1)
    player1.combatmenu()
    player1.movechoice(player2)
    time.sleep(2)
    functions.temporarycheck(player2)
    player2.combatmenu()
    player2.movechoice(player1) 
    time.sleep(2)

def round(player1,player2):
    if player1.speed > player2.speed:
        turnround(player1,player2)
    elif player1.speed == player2.speed:
        choice = random.randint(1,2) 
        if choice == 1:  
            turnround(player1,player2)
        else:
            turnround(player2,player1)
    else:
        turnround(player2,player1)

john = johnfile.john
titouan = titouanfile.titouan
john.greygoose(titouan)

print(john.health)
print(john.attack)
print(john.defense)
print(john.maxhealth)
print(titouan.health)