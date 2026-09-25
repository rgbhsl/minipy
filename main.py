import random 

def main():
    print("Welcome to MiniPy!")
    print("a - Higher/Lower")

    x = input("Please enter one of the letters above to select! ")
    x = x.lower()
    if x == "a": 
        hl()

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








main()