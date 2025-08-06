mystery_word = "DINOSAUR"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guess = False

while guess != mystery_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("Guess a word: ")
        guess_count += 1

    else:
        out_of_guess = True


if out_of_guess:
     print("You LOSE")

else:
     print("You guessed my word!")
