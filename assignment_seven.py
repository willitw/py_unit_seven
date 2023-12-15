# assignment_seven
# Liam Toebbe & Twig Williams
# 12/15/23
# This program plays a text adventure game, that based in a cave where you must make correct choices to find the exit


def you_die():
    '''
    This function prints a message indicating that the player has died and prompts them to play again.
    :return: None
    '''
    print("You died, better luck next time!")
    while True:                                                             # Infinite loop to keep prompting the player until valid input is received.
        play_again = input("Would you like to play again? Input y or n:")   # Prompting the player to choose whether to play again.
        if play_again == "y":                                               # If the player chooses to play again,
            start_game()                                                    # Restart the game by calling the start_game function.
            exit()                                                          # Exit the current function when start_game() is called.
        if play_again == "n":                                               # If the player chooses not to play again,
            print("We'll be here waiting when you change your mind.")       # Display a message indicating the game is ready when the player decides to play again.
            exit()                                                          # Exit the current function when n in inputted after the goodbye message is printed.
        print("Invalid input")                                              # If the player enters an invalid option, print an error message.

def you_win():
    print("Congratulations you found the exit, you win!")
    while True:
        play_again = input("Would you like to play again? Input y or n:")
        if play_again == "y":
            start_game()
            exit()
        if play_again == "n":
            print("We'll be here waiting when you change your mind.")
            exit()
        print("Invalid input")

def prob_wakeup_A1_B1():
    print("You wake up dazed and confused in a cave, the entrance has collapsed you must find the exit")
    print("1: Feel along the wall of the cave")
    print("2: Follow the smell of food")
    while True:
        selectA1B1 = input("Input 1 or 2:")
        if selectA1B1 == '1':
            prob_findstuff_A2_C1()
            break
        if selectA1B1 == '2':
            prob_spiderright_K1_L1_M1_B2()
            break
        print("Invalid input")


def prob_findstuff_A2_C1():
    print("You find a stick, a sharp rock, a rag, and a lighter")
    print("1: Make a spear")
    print("2: Make a torch")
    while True:
        selectA2C1 = input("Input 1 or 2:")
        if selectA2C1 == '1':
            prob_stillhungry_A3_E1()
            break
        if selectA2C1 =='2':
            prob_cavebugs_C2_D1()
            break
        print("Invalid input")

def prob_stillhungry_A3_E1():
    print("You can still smell food")
    print("1: Follow it")
    print("2: Ignore hunger")
    while True:
        selectA3E1 = input("Input 1 or 2:")
        if selectA3E1 == '1':
            prob_spiderleft_A4_F1_G1()
            break
        if selectA3E1 == '2':
            print("You turn away from the smell and your stomach growls loudly.")
            print("The sound echoes through the cave, and suddenly you don't feel as alone in the space.")
            print("Something attacks you from behind, killing you.")
            print("You never saw it coming.")
            you_die()
            break
        print("Invalid input")

def prob_spiderleft_A4_F1_G1():
    print("You encounter a giant cave spider busy wrapping what looks like a boar carcass in webs, its eyes are cloudy with disuse (it is blind)")
    print("1: Try to fight it")
    print("2: Try to sneak past it")
    print("3: Try to get food from the piles of other carcasses")
    while True:
        selectA4F1G1 = input("Input 1, 2, or 3:")
        if selectA4F1G1 == '1':
            prob_boarbits_A5_H1()
            break
        if selectA4F1G1 == '2':
            print("You attempt to sneak past it.")
            print("As you move, your spear scrapes against the stone floor.")
            print("The sound is faint, but not faint enough.")
            print("A few minutes later, you lie still next to the other carcasses.")
            you_die()
            break
        if selectA4F1G1 == '3':
            print("You attempt to sneak past it.")
            print("As you move, your spear scrapes against the stone floor.")
            print("The sound is faint, but not faint enough.")
            print("A few minutes later, you lie still next to the other carcasses.")
            you_die()
            break
        print("Invalid input")
        
def prob_boarbits_A5_H1():
    print("You successfully kill the spider with your spear but you are injured you take off a piece of the boar")
    print("1: Eat it raw")
    print("2: Store the meat for later")
    while True:
        selectA5H1 = input("Input 1 or 2:")
        if selectA5H1 == '1':
            print("you get a rush of energy and find the light at the end of the tunel") #MAKE THIS SOUND BETTE RLAIM PLEASEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
            you_win()
            break
        if selectA5H1 == '2':
            prob_storebits_H2_I1()
            break
        print("Invalid input")
        
def prob_storebits_H2_I1():
    print("Store the meet for later")
    print("1: Go back")
    print("2: Continue past spider's den")
    while True:
        selectH2I2 = input("Input 1 or 2:")
        if selectH2I2 == '1':
            prob_blindattack_H3_J1()
            break
        if selectH2I2 == '2':
            print("You keep walking forward but get hungry you try to eat your raw meat you saved but die from food poisoning")
            you_die()
            break
        print("Invalid input")
        
def prob_blindattack_H3_J1():
    print("You smell like food and something you can't see attacks, you are severely injured but alive")
    print("1: Run")
    print("2: Swing wildly with your spear")
    while True:
        selectH3J1 = input("Input 1 or 2:")
        if selectH3J1 == '1':
            print("It eats you and your boar drumstick")
            you_die()
            break
        if selectH3J1 == '2':
            print("It eats you and your boar drumstick")
            you_die()
            break
        print("Invalid input")

def prob_cavebugs_C2_D1():
    print("The light from the torch attracts a bunch of cave bugs. they start to climb you to try to get to the light")
    print("1: Stay still")
    print("2: Brush them off and run")
    while True:
        selectC2D1 = input("Input 1 or 2:")
        if selectC2D1 == '1':
            prob_ladyliberty_C3_D2()
            break
        if selectC2D1 == '2':
            print("They bite you when you brush them off, they are venomous and you are poisoned")
            you_die()
            break
        print("Invalid input")

def prob_ladyliberty_C3_D2():
    print("They climb up you and jump into the fire, making it bigger you are burnt and hurt, but your torch is now extra bright. it allows you to see a patch of shimmery looking moss")
    print("1: Eat moss")
    print("2: Don't eat moss")
    while True:
        selectC3D2 = input("Input 1 or 2:")
        if selectC3D2 == '1':
            print("You get high and doze off to sleep")
            start_game()
            break
        if selectC3D2 == '2':
            print("Don't eat moss and remain hungry, you eventually starve")
            you_die()
            break
        print("Invalid input")

def prob_spiderright_K1_L1_M1_B2():
    print("You encounter a giant cave spider busy wrapping what looks like a boar carcass in webs. its eyes are cloudy with disuse (it is blind)")
    print("1: Try to fight it")
    print("2: Sneak to the left")
    print("3: Sneak to the right")
    print("4: Try to get food from the piles of other carcasses")
    while True:
        selectK1L1M1B2 = input("Input 1, 2, 3, or 4:")
        if selectK1L1M1B2 == '1':
            print("You are unarmed and not strong enough to kill it")
            you_die()
            break
        if selectK1L1M1B2 == '2':
            prob_behindyou_L2_N1()
            break
        if selectK1L1M1B2 == '3':
            print("You step on an old scapula bone, it hears you")
            you_die()
            break
        if selectK1L1M1B2 == '4':
            print("It hears you and deems you delicious")
            you_die()
            break
        print("Invalid input")

def prob_behindyou_L2_N1():
    print("You successfully sneak past the spider but you hear something behind you")
    print("1: Run away")
    print("2: Stay and see what it is")
    while True:
        selectL2N1 = input("Input 1 or 2:")
        if selectL2N1 == '1':
            prob_3paths_L3_O1_P1()
            break
        if selectL2N1 == '2':
            print("It smells you and deems you delicious")
            you_die()
            break
        print("Invalid input")

def prob_3paths_L3_O1_P1():
    print("It hears you running and starts chasing you, you see three pathways you must choose one to go down")
    print("1: Take a left")
    print("2: Go straight")
    print("3: Turn right")
    while True:
        selectL3O1P1 = input("Input 1, 2, or 3:")
        if selectL3O1P1 == '1':
            print("Dead end, there is nowhere to go")
            you_die()
            break
        if selectL3O1P1 == '2':
            print("You see a bright light at the end of the tunnel")
            you_win()
            break
        if selectL3O1P1 == '3':
            prob_3morepaths_P2_Q1_R1()
            break
        print("Invalid input")

def prob_3morepaths_P2_Q1_R1():
    print("You trip and are severely injured but you find 3 more pathways")
    print("1: Steer left")
    print("2: Continue straight")
    print("3: Take a sharp right")
    while True:
        selectP2Q1R1 = input("Input 1, 2, or 3:")
        if selectP2Q1R1 == '1':
            print("You see a bright light at the end of the tunnel")
            you_win()
            break
        if selectP2Q1R1 == '2':
            print("Dead end, there is nowhere to go")
            you_die()
            break
        if selectP2Q1R1 == '3':
            print("You trip and it finds you")
            you_die()
            break
        print("Invalid input")

def main():
    prob_wakeup_A1_B1()         # Starts the game by calling the first problem function.

main()