# Welcome to the Hangman Game

import time
import random

# First, we welcome the user to play the game

print('\nWelcome to the Hangman Game!!!')
user_name = input('\nPlease enter your name: ')
time.sleep(2)
print('\nHello ' + user_name + ' Best of Luck!! '
                               '\nLets Play Hangman!!!\n')
time.sleep(2)

# Now initialising the parameters of the Game

def game_parameters():
    global word_count
    global word_display
    global guess_word
    global alphabet_previously_guessed
    global word_length
    global wish_to_play_game
    global correct_word

    emotion_word_library = ['happy', 'anxious', 'angry', 'sad', 'excited',
                            'frustrated', 'confused', 'surprised']
    action_word_library = ['playing', 'skating', 'walking', 'dancing', 'exercising',
                           'sleeping', 'fighting', 'acting']
    games_word_library = ['football', 'basketball', 'volleyball', 'cricket',
                          'badminton', 'tennis']
    country_word_library = ['india', 'italy', 'canada', 'japan', 'russia', 'england',
                            'australia', 'italy', 'france','germany', 'brazil']
    animal_word_library = ['tiger', 'lion', 'cheetah', 'zebra', 'elephant', 'dog',
                           'cat', 'cow', 'goat', 'leopard']
    bird_word_library = ['eagle', 'peacock', 'parrot', 'sparrow', 'crow',
                         'pigeon', 'vulture', 'owl', 'dove']

    guess_word = random.choice(emotion_word_library + action_word_library +
                               games_word_library + country_word_library +
                               animal_word_library + bird_word_library)

    word_length = len(guess_word)
    correct_word = guess_word
    word_count = 0
    word_display = '_' * word_length
    alphabet_previously_guessed = []
    wish_to_play_game = ""

    return correct_word, guess_word

# A loop to be executed at the end of every round

def game_repeat_loop():

    global wish_to_play_game
    game_parameters()
    wish_to_play_game = input("Do You want to play again? y = yes, n = no \n")
    while wish_to_play_game not in ["y", "n", "Y", "N"]:
        wish_to_play_game = input("Do You want to play again? y = yes, n = no \n")
    if wish_to_play_game == "y":
        print("\nYeah! Lets Play Again ")
        hangman_game()
    elif wish_to_play_game == "n":
        print("Thanks For Playing Hangman Game! Do return soon to play again!")
        exit()

# Providing Hint to user if there are 2 incorrect guesses

def hint_gangman(correct_word):

    emotion_word_library = ['happy', 'anxious', 'angry', 'sad', 'excited',
                            'frustrated', 'confused', 'surprised']
    action_word_library = ['playing', 'skating', 'walking', 'dancing', 'exercising',
                           'sleeping', 'fighting', 'acting']
    games_word_library = ['football', 'basketball', 'volleyball', 'cricket',
                          'badminton', 'tennis']
    country_word_library = ['india', 'italy', 'canada', 'japan', 'russia', 'england',
                            'australia', 'italy', 'france', 'germany', 'brazil']
    animal_word_library = ['tiger', 'lion', 'cheetah', 'zebra', 'elephant', 'dog',
                           'cat', 'cow', 'goat', 'leopard']
    bird_word_library = ['eagle', 'peacock', 'parrot', 'sparrow', 'crow',
                         'pigeon', 'vulture', 'owl', 'dove']

    if correct_word in emotion_word_library:
        print('\nHINT: The word is related to an emotion.\n')
    elif correct_word in action_word_library:
        print('\nHINT: The word is an action being performed.\n')
    elif correct_word in games_word_library:
        print('\nHINT: The word is related to a Game.\n')
    elif correct_word in country_word_library:
        print('\nHINT: The word is a name of Country.\n')
    elif correct_word in animal_word_library:
        print('\nHINT: The word is an Animal species.\n')
    else:
        print('\nHINT: The word is a Bird species.\n')

    return correct_word

# Initialising all the conditions required for the Game

def hangman_game():
    global word_count
    global word_display
    global guess_word
    global alphabet_previously_guessed
    global play_game

    guess_limit = 10

    user_guess = input("\nThe Hangman Word you need to guess: " + word_display + "\nPlease enter your guess:  ")

    user_guess = user_guess.strip()

    if len(user_guess.strip()) == 0 or len(user_guess.strip()) >= 2 or user_guess <= "9":
        print("Invalid Input, Try a New letter \n")
        hangman_game()

    elif user_guess in guess_word:
        alphabet_previously_guessed.extend([user_guess])
        index = guess_word.find(user_guess)
        guess_word = guess_word[:index] + "_" + guess_word[index + 1:]
        word_display = word_display[:index] + user_guess + word_display[index + 1:]
        # print(word_display + '\n')

    elif user_guess in alphabet_previously_guessed:
        print('You have already guessed the letter, Try a different one: \n')

    else:
        word_count += 1

        if word_count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - word_count) + " guess remaining\n")

        elif word_count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - word_count) + " guesses remaining\n")


        elif word_count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - word_count) + " guesses remaining\n")
            hint_gangman(correct_word)

        elif word_count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - word_count) + " guesses remaining\n")

        elif word_count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     | \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - word_count) + " guesses remaining\n")

        elif word_count == 6:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|  \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - word_count) + " guesses remaining\n")

        elif word_count == 7:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\  \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - word_count) + " guesses remaining\n")

        elif word_count == 8:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\  \n"
                  "  |    /    \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - word_count) + " last guess remaining\n")

        elif word_count == 9:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\  \n"
                  "  |    / \   \n"
                  "__|__\n")
            print("Wrong guess. " + str(guess_limit - word_count) + " last guess remaining\n")

        elif word_count == 10:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     0\n"
                  "  |    /|\ \n"
                  "  |    / \  \n"
                  "__|__\n")
            print("Wrong guess. The correct word is " + correct_word + ". You are now hanged!!!\n")
            game_repeat_loop()

    if guess_word == '_' * word_length:
        print("Congrats! The word is ", correct_word, " You have guessed the word correctly!\n")
        print("   _____   \n"
              "  |        \n"
              "  |        \n"
              "  |        \n"
              "  |        \n"
              "  |     0/  \n"
              "  |    /|  \n"
              "__|__  / \  \n")
        game_repeat_loop()

    elif word_count != guess_limit:
        hangman_game()

game_parameters()

hangman_game()
