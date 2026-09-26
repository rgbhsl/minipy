import random 

def main():
    print("Welcome to MiniPy!")
    print("a - Higher/Lower (Computer)")
    print("b - Higher/Lower (2 Players)")
    print("c - Rock Paper Scissors")
    
    game = input("Please enter one of the letters above to select! ")
    game = game.lower()
    if game == "a": 
        hl()
    if game == "b":
        hl2p()
    if game == "c":
        rps()


def hl():
    print("HIGHER/LOWER : The number will be a positive integer 1 to 50. You get 6 guesses.")
    compnum = random.randint(1, 50)
    guesses = 6
    while guesses != 0:
        x = int(input("Enter your guess. "))
        if x<1 or x>50 :
            print("Your guess is out of range. ")
        else:
            guesses = guesses - 1
            if x == compnum:
                print("Well done! You win with", guesses, "guess(es) remaining")
            elif x> compnum:
                print("Too high!", guesses, "guesses left.")
            elif x< compnum:
                print("Too low!", guesses, "guesses left.")
    if guesses == 0 :
        print("The number was", compnum)
    p = input("To select another game, enter 1. To play this game again, enter anything else. ")
    if p != "1":
        hl()
    else:
        main()

def hl2p():
    print("HIGHER/LOWER : Player 1 may enter an integer 1-100, and Player 2 will get 8 guesses.")
    p1num = int(input("Player 1, please enter an integer 1 to 100. "))
    while (p1num>100) or (p1num<1):
        p1num = int(input("Player 1, your value is invalid. Please enter an integer 1 to 100."))
    spacer = 0
    while spacer != 40:
        print("...")
        spacer = spacer + 1
    guesses = 8
    while guesses != 0:
        x = int(input("Enter your guess. "))
        if x<1 or x>100 :
            print("Your guess is out of range. ")
        else:
            guesses = guesses - 1
            if x == p1num:
                print("Well done! Player 2 wins with", guesses, "guess(es) remaining")
            elif x> p1num:
                print("Too high!", guesses, "guesses left.")
            elif x< p1num:
                print("Too low!", guesses, "guesses left.")
    if guesses == 0 :
        print("Player 1 win! The number chosen by Player 1 was", p1num)
    p = input("To select another game, enter 1. To play this game again, enter anything else. ")
    if p != "1":
        hl2p()
    else:
        main()


def rps():
    print("Welcome to Rock-Paper-Scissors.")
    compnum = random.randint(1,3)
    if compnum == 1:
        mv = "r"
    elif compnum == 2:
        mv = "p"
    else:
        mv = "s"
    play = (input("The computer has chosen! Please enter r, p, or s to play rock, paper, or scissors respectively: ")).lower()
    if mv == play:
        print("Tie! The computer also played", play)
    elif ((mv == "r") and (play == "p")) or ((mv == "p") and (play == "s")) or ((mv == "s") and (play == "r")):
        print("Player win! The computer played", mv)
    elif ((play == "r") and (mv == "p")) or ((play == "p") and (mv == "s")) or ((play == "s") and (mv == "r")):
        print("Computer win! The computer played", mv)
    p = input("To select another game, enter 1. To play this game again, enter anything else. ")
    if p != "1":
        rps()
    else:
        main()


main()