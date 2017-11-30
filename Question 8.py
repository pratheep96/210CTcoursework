#Sets upper bound and lower bound of the search
highNumber = 2000
lowNumber = 1
feedback = "No"
#This while loop repeats until the user confirms the computer guess is correct
while feedback == "No":
    computerGuess = int(round(highNumber + lowNumber)/2)
    print("Computer guesses " + str(computerGuess))
    feedback = str(input("Is this correct(Yes/No)? "))
    if feedback == "Yes":
        print("Computer has guessed your number correctly")
    elif feedback == "No":
        highOrLow = str(input("Higher or Lower(Higher/Lower)? "))
        if highOrLow == "Higher":
            lowNumber = computerGuess
        elif highOrLow == "Lower":
            highNumber = computerGuess

