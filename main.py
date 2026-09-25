import random 

def main():
    print("Welcome to MiniPy!")
    print("a - Higher/Lower")
    print("b - Rock Paper Scissors")
    x = input("Please enter one of the letters above to select! ")
    x = x.lower()
    if x == "a": 
        hl()
    if x == "b":
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


def rps():
    print("Welcome to Rock-Paper-Scissors.")
    compnum = random.randint(1,3)
    if compnum == 1:
        mv = "r"
    elif compnum == 2:
        mv = "p"
    else:
        mv = "scissors"
    play = (input("The computer has chosen! Please enter r, p, or s to play rock, paper, or scissors respectively: ")).lower()
    if mv == play:
        print("Tie! The computer also played", play)
    elif ((mv == "r") and (play == "p")) or ((mv == "p") and (play == "s")) or ((mv == "s") and (play == "r")):
        print("Player win! The computer played", mv)
    elif ((play == "r") and (mv == "p")) or ((play == "p") and (mv == "s")) or ((play == "s") and (mv == "r")):
        print("Computer win! The computer played", mv)



main()