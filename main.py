import random
n=random.randint(1,100)
guesses=0
a=-1
while(a!=n):
    guesses+=1
    a=int(input("Enter the number:"))
    if (a>n):
        print("Oops! Hint is enter lower number.")
    elif (a<n):
        print("Oops! Hint is enter Higher number.")
    elif(a<=0):
        print("Invalid enter between 0 to 100")

print(f"Hurray! you guessed {n} right at {guesses} guesses.")        