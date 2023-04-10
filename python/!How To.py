print ("How to... e.g. 'How to Fly, How to Eat btw caps matter")
thing = input("> ")
if thing == ("How to Move"):
    print ("Choose mode to move")
    print("Choose mode, Helicopter, Airplane, or Jet Engines")
    input("> ")
    if input == ("Helicopter"):
        print("Have helicopter?")
        input ("> ")
        if input == ("Yes"):
            print ("Good job!")
        else:
            print("Sorry :(")