import engine,titouanfile,johnfile,functions,random

def intro(player1,player2):
    dialogue = ["...",player1.name,player2.name,"Fight hard...",
    "Fight clean...","Glory to the winner,","Humiliation for the loser.",
    "3...","2...","1...","FIGHT!"]
    for line in dialogue:
        engine.display(line)
        engine.pause()

def round(player1,player2):
    if player1.speed > player2.speed:
        functions.singleturn(player1,player2)
        functions.singleturn(player2,player1)
    elif player1.speed == player2.speed:
        choice = random.randint(1,2) 
        if choice == 1:  
            functions.singleturn(player1,player2)
            functions.singleturn(player2,player1)
        else:
            functions.singleturn(player2,player1)
            functions.singleturn(player1,player2)
    else:
        functions.singleturn(player2,player1)
        functions.singleturn(player1,player2)

titouan = titouanfile.titouan
allisongreen = johnfile.allisongreen
john = johnfile.john
intro(titouan,john)
john.money = 150
while True:
    round(titouan,john)