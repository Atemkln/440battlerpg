import sys,time
from typing import Any

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def typeout(t, space=True):
  typing_speed = 120 #wpm
  for l in t:
      flush_input()
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(10.0/typing_speed)
  if space:
   print("")

def get_input(valid_input: list):
  count = 0
  while True:
    user_entered = input("")
    if user_entered not in valid_input and count == 0:
      print("")
      typeout("Valid inputs only.")
      count += 1
      user_entered = None
    elif user_entered not in valid_input and count == 1:     
      typeout("Bruh, valid inputs.")
      count += 1
      user_entered = None
    elif user_entered not in valid_input and count == 2:
      typeout("Dude seriously wtf.")
      user_entered = None    
    else:
      return user_entered

def display(line, get=0,amount=0):
    if get == 0:
      typeout(line)
      print("")
    elif get == 1:
        typeout(line,space=False)
        choice = get_input(["1","2"])
        print("")
        return choice
    elif get == 2:
        typeout(line,space=False)
        options = []
        for i in range(5+amount):
            options.append(f"{i+1}")
        choice = get_input(options)
        print("")
        return choice

def get_response(options: list):
  for index, option in enumerate(options):
    print(str(index) + ". " + option[0])
 
  valid_inputs = [str(num) for num in range(len(options))]

  option_index = int(get_input(valid_inputs))

  return options[option_index][1]

def pause():
    time.sleep(1)

def waitresult():
    display("...")
    time.sleep(2)