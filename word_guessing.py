# Word Guessing Main Script

import os
import random

print("Welcome to the Word Guessing Game!")

def choose_word():
    words = ["pants","sweater","shirt"]
    return random.choice(words)

def mask_word(word, guesses):
    return ''.join([letter if letter in guesses else'_' for letter in word])

def game():
    secret_word = choose_word()
    attempts = 0
    word_guesses = 0
    letter_guesses = set()

    print("Guess the word! You get three chances to guess the word.")

    while word_guesses < 3:
        print("Word so far:", mask_word(secret_word, letter_guesses))
        guess = input("Guess a letter or entire word:").lower()

        if len(guess) == len(secret_word) and guess.isalpha():
            if guess == secret_word:
                print("Congrats! You have guessed the word correctly.")
                break
            else:
                word_guesses += 1
                print("Wrong guess. You have", 3 - word_guesses, "word guesses left.")
                if word_guesses == 3:
                    print("Game is up. The word was:", secret_word)
        elif len(guess) == 1 and guess.isalpha():
            if guess in secret_word:
                print("The letter", guess, "is in the word")
                letter_guesses.add(guess)
            else:
                print("The letter", guess, "it's not in the word.")
            attempts += 1
        else:
            print("Input is invalid. Only guess the whole word or a single letter.")

            if '_' not in mask_word(secret_word, letter_guesses):
                print("Congrats! You discovered the word", secret_word, "with", attempts, "guesses")
                break

    if __name__ == "main":
        game()