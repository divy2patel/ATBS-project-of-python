def numguess(num, N):
    if num > N:
        print("Lower")
        return False
    elif num < N:
        print("Higher")
        return False
    else:
        print("Guessed the Number. 👍")
        return True

N = int(input("What number do you want someone to guess: "))
num = int(input("Enter the number: "))
guess=0
while numguess(num, N) == False:
    num = int(input("Enter the number: "))
    guess+=1
print(f"Number of guess={guess+1}")