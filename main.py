import random 

def main():
    print(" ")
    print("Menu:")
    print("a - Higher/Lower (Computer)")
    print("b - Higher/Lower (2 Players)")
    print("c - Rock Paper Scissors")
    print("d - Roll a die")
    print("e - Capitle")
    game = input("Please enter one of the letters above to select! In case of confusion, please write 0 for help. ")
    game = game.lower()
    if game == "a": 
        hl()
    if game == "b":
        hl2p()
    if game == "c":
        rps()
    if game == "d":
        rolld()
    if game == "e":
        capitle()
    if game == "0":
        helpfunc()

def helpfunc():
    print(" ")
    print("MiniPy features a collection of terminal-based minigames that you can play vs the computer, or in-person vs a friend.")
    print("Each game will have rules and general prompts to help you with any input you need to enter.")
    print("Thank you for trying out my project!!! -rgbhsl")
    x = input("To return to menu, please enter m. ")
    if x == "m":
        main()

def hl():
    print(" ")
    print("HIGHER/LOWER : The number will be a positive integer 1 to 50. You get 6 guesses.")
    compnum = random.randint(1, 50)
    guesses = 6
    while guesses != 0:
        x = int(input("Enter your guess. "))
        if x<1 or x>50 :
            print("Your guess is out of range. ")
        else:
            guesses = guesses - 1
            if x> compnum:
                print("Too high!", guesses, "guesses left.")
            elif x< compnum:
                print("Too low!", guesses, "guesses left.")
            elif x == compnum:
                print("Well done! You win with", guesses, "guess(es) remaining")
                break
    if guesses == 0 :
        print("The number was", compnum)
    print(" ")
    p = input("To select another game, enter 1. To play this game again, enter anything else. ")
    if p != "1":
        hl()
    else:
        main()

def hl2p():
    print(" ")
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
        x = int(input("Player 2, enter your guess. "))
        if x<1 or x>100 :
            print("Player 2, your guess is out of range. ")
        else:
            guesses = guesses - 1
            if x> p1num:
                print("Too high!", guesses, "guesses left.")
            elif x< p1num:
                print("Too low!", guesses, "guesses left.")
            elif x == p1num:
                print("Well done! Player 2 wins with", guesses, "guess(es) remaining")
                break
    if guesses == 0 :
        print("Player 1 win! The number chosen by Player 1 was", p1num)
    print(" ")
    p = input("To select another game, enter 1. To play this game again, enter anything else. ")
    if p != "1":
        hl2p()
    else:
        main()

def rps():
    print(" ")
    print("Welcome to Rock-Paper-Scissors. Please note r = rock, p = paper, s = scissors. ")
    compnum = random.randint(1,3)
    if compnum == 1:
        mv = "r"
    elif compnum == 2:
        mv = "p"
    else:
        mv = "s"
    play = (input("The computer has chosen! Please enter r, p, or s: ")).lower()
    if mv == play:
        print("Tie! The computer also played", play)
    elif ((mv == "r") and (play == "p")) or ((mv == "p") and (play == "s")) or ((mv == "s") and (play == "r")):
        print("Player win! The computer played", mv)
    elif ((play == "r") and (mv == "p")) or ((play == "p") and (mv == "s")) or ((play == "s") and (mv == "r")):
        print("Computer win! The computer played", mv)
    print(" ")
    p = input("To select another game, enter 1. To play this game again, enter anything else. ")
    if p != "1":
        rps()
    else:
        main()

def rolld():
    print(" ")
    print("DIE ROLL: Pick an upper bound, and a random integer from 1 to your number will be generated!")
    up = int(input("Your upper bound: "))
    x = random.randint(1, up)
    print(f"On the die: {x}")
    p = input("Write 1 to go back to menu. Write anything else to change your die or roll again: ")
    if p != "1":
        rolld()
    else:
        main()

def capitle():
    capitals = ["Paris", "Berlin", "London", "Moscow", "Tashkent", "Abuja", "Algiers", "Astana", "Athens", "Baku", "Bangkok", "Beijing", "Brasilia", "Dhaka", "Djibouti", "Havana", "Ljubljana", "Rabat", "Seoul", "Tokyo", "Yerevan"]
    word = random.choice(capitals)
    word = word.lower()
    guessed = []
    wrong = 0
    maxg = 5
    print("")
    print("A game inspired by Hangman, with the theme being capitals of countries! You get 5 chances to get a letter wrong.")
    while wrong < maxg:
        display = ("")
        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "
        print("Word:", display)
        if "_" not in display:
            print("You won! The word was: ", word)
            break
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter just one letter.")
            continue
        if guess in guessed:
            print("You guessed this before.")
            continue
        guessed.append(guess)
        if guess not in word:
            wrong = wrong + 1
            print(f"{wrong} out of 5 chances used!")
    else:
        print("Game over! The capital was: ", word)

print("Welcome to MiniPy!")
main()