import random


#             0         1       2          3
word_bank = ["tiger", "fishes", "houses", "watch"]

word = random.choice(word_bank)

word_chars = list(word)

#the below is an integer because it is a whole number
num_chars = len(word_chars)
#the print statement only accepts strings so we need to convert num_chars
user_guess = ""

lives = 3
victory = False

for char in word_chars:
    user_guess += '_' #user_guess = user_guess + '_'

print("Welcome to Hangman! your word contains " + str(num_chars) + " letters")
print("Your current guess is: " + user_guess)
print("You have " + str(lives) + " guesses left")

while(lives >= 1 and victory == False):
    current_guess = user_guess
    guess = input("What is your guess?")

    for index, char in enumerate(word_chars):
        #our test word is 'houses'
        #user guesses 's'
        if char == guess:
            #converting the user_guess aka underscores to include correct letters
            #current user_guess is '-----'
            temp_user_guess = list(user_guess)
            #set temp_user_guess to [-, -, -, -, -]
            temp_user_guess[index] = guess
            #from the code above we have the index '1' which is the second letter in house
            #setting temp_user_guess[1] = 'o' gives us the array [-, o, -, -, -]
            user_guess = ""
            #turn [-, o, -, -, -] into "---s-s"
            for x in temp_user_guess:
                user_guess += x
            

            if user_guess == word:
                victory = True
    #this means incorrect
    if current_guess == user_guess:
        lives -= 1
        print("You guessed incorrectly! Try again! You have " + str(lives) + " guesses left!")
    else:
        print("You guessed correct! Your current guess is " + user_guess)
                
if victory:
    print("you win!")
else:
    print("you lose!")



        
            



