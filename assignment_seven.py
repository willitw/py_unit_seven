def start_game():
    prob_wakeup_A1_B1()


def you_die():
    print("You died, better luck next time")
    while True:
        play_again = input("Would you like to play again? Input y or n:")
        if play_again == "y":
            start_game()
            exit()
        if play_again == "n":
            print("We'll be here waiting when you change your mind")
            exit()
        print("Invalid input")

def you_win():
    print("Congratulations you found the exit, you win!")
    while True:
        play_again = input("Would you like to play again? Input y or n:")
        if play_again == "y":
            start_game()
            exit()
        if play_again == "n":
            print("We'll be here waiting when you change your mind")
            exit()
        print("Invalid input")

def prob_wakeup_A1_B1():
    print("You wake up dazed and confused in a cave, the entrance has collapsed you must find the exit")
    print("1: Feel along the wall of the cave")
    print("2: Follow the smell of food")
    while True:
        selectA1B1 = input("Input 1 or 2:")
        if selectA1B1 == '1':
            choiceA1()
            break
        if selectA1B1 == '2':
            choiceB1()
            break
        print("Invalid input")


def prob_findstuff_A2_C1():
    print("You find a stick, a sharp rock, a rag, and a lighter")
    print("1: Make a spear")
    print("2: Make a torch")
    while True:
        selectA2C1 = input("Input 1 or 2:")
        if selectA2C1 == '1':
            choiceA2()
            break
        if selectA2C1 =='2':
            choiceC1()
            break
        print("Invalid input")

def prob_stillhungry_A3_E1():
    print("You can still smell food")
    print("1: Follow it")
    print("2: Ignore hunger")
    while True:
        selectA3E1 = input("Input 1 or 2:")
        if selectA3E1 == '1':
            choiceA3()
            break
        if selectA3E1 == '2':
            choiceE1()
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
            choiceA4()
            break
        if selectA4F1G1 == '2':
            choiceF1()
            break
        if selectA4F1G1 == '3':
            choiceG1()
            break
        print("Invalid input")
        
def prob_boarbits_A5_H1():
    print("You successfully kill the spider with your spear but you are injured you take off a piece of the boar")
    print("1: Eat it raw")
    print("2: Store the meat for later")
    while True:
        selectA5H1 = input("Input 1 or 2:")
        if selectA5H1 == '1':
            choiceA5()
            break
        if selectA5H1 == '2':
            choiceH1()
            break
        print("Invalid input")
        
def prob_storebits_H2_I1():
    print("Store the meet for later")
    print("1: Go back")
    print("2: Continue past spider's den")
    while True:
        selectH2I2 = input("Input 1 or 2:")
        if selectH2I2 == '1':
            choiceH2()
            break
        if selectH2I2 == '2':
            choiceI1()
            break
        print("Invalid input")
        
def prob_blindattack_H3_J1():
    print("You smell like food and something you can't see attacks, you are severely injured but alive")
    print("1: Run")
    print("2: Swing wildly with your spear")
    while True:
        selectH3J1 = input("Input 1 or 2:")
        if selectH3J1 == '1':
            choiceH3()
            break
        if selectH3J1 == '2':
            choiceJ1()
            break
        print("Invalid input")

def prob_cavebugs_C2_D1():
    print("The light from the torch attracts a bunch of cave bugs. they start to climb you to try to get to the light")
    print("1: Stay still")
    print("2: Brush them off and run")
    while True:
        selectC2D1 = input("Input 1 or 2:")
        if selectC2D1 == '1':
            choiceC2()
            break
        if selectC2D1 == '2':
            choiceD1()
            break
        print("Invalid input")

def prob_ladyliberty_C3_D2():
    print("They climb up you and jump into the fire, making it bigger you are burnt and hurt, but your torch is now extra bright. it allows you to see a patch of shimmery looking moss")
    print("1: Eat moss")
    print("2: Don't eat moss")
    while True:
        selectC3D2 = input("Input 1 or 2:")
        if selectC3D2 == '1':
            choiceC3()
            break
        if selectC3D2 == '2':
            choiceD2()
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
            choiceK1()
            break
        if selectK1L1M1B2 == '2':
            choiceL1()
            break
        if selectK1L1M1B2 == '3':
            choiceM1()
            break
        if selectK1L1M1B2 == '4':
            choiceB2()
            break
        print("Invalid input")

def prob_behindyou_L2_N1():
    print("You successfully sneak past the spider but you hear something behind you")
    print("1: Run away")
    print("2: Stay and see what it is")
    while True:
        selectL2N1 = input("Input 1 or 2:")
        if selectL2N1 == '1':
            choiceL2()
            break
        if selectL2N1 == '2':
            choiceN1()
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
            choiceL3()
            break
        if selectL3O1P1 == '2':
            choiceO1()
            break
        if selectL3O1P1 == '3':
            choiceP1()
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
            choiceP2()
            break
        if selectP2Q1R1 == '2':
            choiceQ1()
            break
        if selectP2Q1R1 == '3':
            choiceR1()
            break
        print("Invalid input")

# ADD DEF CHOICES INTO DEF PROBS
# EDIT RESPODES
# DOCUMENT CODE
# ADD THE SHIT TOP THE TOP
# ADD PUNCUATION

def choiceA1():
    prob_findstuff_A2_C1()
def choiceA2():
    prob_stillhungry_A3_E1()
def choiceA3():
    prob_spiderleft_A4_F1_G1()
def choiceA4():
    prob_boarbits_A5_H1()
def choiceA5():
    print("You are no longer hungry and have a rush of energy, you keep venturing on and see a bright light at the end of the tunnel")
    you_win()
def choiceB1():
    prob_spiderright_K1_L1_M1_B2()
def choiceB2():
    print("It hears you and deems you delicious")
    you_die()

def choiceC1():
    prob_cavebugs_C2_D1()

def choiceC2():
    prob_ladyliberty_C3_D2()

def choiceC3():
    print("You get high and doze off to sleep")
    start_game()
def choiceD1():
    print("They bite you when you brush them off, they are venomous and you are poisoned")
    you_die()
def choiceD2():
    print("Don't eat moss and remain hungry, you eventually starve")
    you_die()
def choiceE1():
    print("Your hungry stomach makes a load noise that attracts something you cant see")
    you_die()

def choiceF1():
    print("Your spear makes a noise as you move, it hears you")
    you_die()

def choiceG1():
    print("Your spear makes a noise as you move, it hears you")
    you_die()

def choiceH1():
    prob_storebits_H2_I1()

def choiceH2():
    prob_blindattack_H3_J1()

def choiceH3():
    print("It eats you and your boar drumstick")
    you_die()

def choiceI1():
    print("You keep walking forward but get hungry you try to eat your raw meat you saved but die from food poisoning")
    you_die()

def choiceJ1():
    print("It eats you and your boar drumstick")
    you_die()

def choiceK1():
    print("You are unarmed and not strong enough to kill it")
    you_die()

def choiceL1():
    prob_behindyou_L2_N1()

def choiceL2():
    prob_3paths_L3_O1_P1()

def choiceL3():
    print("Dead end, there is nowhere to go")
    you_die()

def choiceM1():
    print("You step on an old scapula bone, it hears you")
    you_die()

def choiceN1():
    print("It smells you and deems you delicious")
    you_die()

def choiceO1():
    print("You see a bright light at the end of the tunnel")
    you_win()
def choiceP1():
    prob_3morepaths_P2_Q1_R1()

def choiceP2():
    print("You see a bright light at the end of the tunnel")
    you_win()
def choiceQ1():
    print("Dead end, there is nowhere to go")
    you_die()

def choiceR1():
    print("You trip and it finds you")
    you_die()

def main():
    start_game()

main()