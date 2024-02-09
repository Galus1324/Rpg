import sys, time, pygame, os

def print_slow(args):
    for arg in args:
        for char in arg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

def multi_choice(answers, consequences):
    print_slow("Choose an option:\n")
    x = input()
    if x not in answers:
        print_slow(f"Your answer is not valid.\nValid answers are: {', '.join(answers)}\n")
        multi_choice(answers, consequences)
    else:
        index = answers.index(x)
        consequences[index]()

def soba2():
    print("soba 2")

def soba3():
    print("soba 3")

drink = True

print_slow("What is your name?\n")
player_name = input()
print_slow("You are resting in a tavern from a long adventure you just came back from recently.\n"
            "To you comes a grumpy and tired-looking dwarf bartender and asks you:\n"
            "Bartender: Do you want anything to drink?\nBartender: I have got beer and mead but don't ask for anything fancier than that cuz I don't have it!\n")

multi_choice(["beer", "mead", "nothing"],
             [lambda: print_slow("Bartender: Good choice!\n"
                                "Bartender: All our beer comes from locals just a couple minutes from here.\n"
                                "Bartender: Many strong heroes like yourself have enjoyed the beer here.\n"
                                "Bartender: Here you go and enjoy!\n"),
              lambda: print_slow("Bartender: Eh mead, was never a big fan of the drink.\n"
                                "Bartender: It is just too sweet for me.\n"
                                "Bartender: I like more erm how would I say manly drinks like beer.\n"
                                "Bartender: It is nice and bitter.\n"),
              lambda: (print_slow("Bartender: An adventurer that refuses a drink?\n"
                                  "Bartender: What kind of an adventurer even are you?\n"),
                       globals().update({'drink': False}))])

print_slow("Bartender: Anyways, have you heard that there has been a tomb found near our little village?\n"
            "Bartender: Yea, it is rumored that it was created by an ancient lich.\n"
            "Bartender: The tomb only accepts one adventurer at a time.\n"
            "Bartender: The one who can get out of it alive will gain enormous wealth if the writings on the tomb walls are to be trusted.\n"
            "Bartender: I have seen many heroes go and try to clear the tomb but none has succeeded yet.\n"
            "Bartender: Are you gonna try, young adventurer?\n")

multi_choice(["yes", "no"],
             [lambda: print_slow("Bartender: Oh, you must be brave, or are you just so desperate for money?\n"
                                 "Bartender: Who knows well anyways got to go help other customers.\n"),
              lambda: print_slow("Bartender: Well, an honest answer and the one I like as the dead customers don't spend much money.\n"
                                 "Bartender: Just promise to protect my tavern if anything crawls out of it.\n")])

if drink:
    print_slow("After drinking your drink, you leave the tavern.\n")
else:
    print_slow("After that conversation, you leave the tavern.\n")
    
print_slow("when you come outside the tavern you see the sun shining in a beautiful spring morning.\n"
           "before you could go anywhere you see a small child comes with ragged clothes who is running towards you and says:\n"
           "Eirlys: Hello I am Eirlys.\n"
           "Eirlys: And really really need your help.\n"
           "Eirlys: My father went to the tomb so that our family could finally eat every day.\n"
           "Eirlys: But he hasn't come back.\n" )
