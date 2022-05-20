import random

print("Welcom to Number Guessing Game")

number=random.randint(1,9)
chances=0
print("Guess a number between 1/9: ")

while chances<5:
    guess=int(input("Enter your number: "))
    if guess== number:
        print("Congrats! You won")
        break
    elif guess<number:
        print("So Close GO Higher than ",guess)
        break
    else: 
        print("your Guess was to lower than",guess)
        break
    chances+=1

if not chances<5:
    print("you lose! the number was: ",number)
        
