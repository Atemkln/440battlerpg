import engine,titouanfile,functions,test,time

def intro(player1,player2):
    dialogue = ["...",player1.name,player2.name,"Fight hard...",
    "Fight clean...","Glory to the winner,","Humiliation for the loser.",
    "3...","2...","1...","FIGHT!"]
    for line in dialogue:
        engine.display(line)
        engine.pause()

def round(player1,player2):
    player1.combatmenu()
    player1.movechoice(player2)
    time.sleep(2)
    player2.combatmenu()
    player2.movechoice(player1) 
    time.sleep(2)   

