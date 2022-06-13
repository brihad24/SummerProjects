from random import choice
from rich.prompt import Prompt
from rich.console import Console
from words import word_list

color_squares = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

target_word = choice(word_list)
guess_statement = "\nEnter your guess"
welcome_message = "Welcome to Wordle!" + "\n" + "You can start guessing now. You have 6 guesses" + "\n"
allowed_guesses = 6
guess_with_answer = ""

def correct_place(letter):
    return f'[black on green]{letter}[/]'

def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'

def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


def check_guess(guess):
    for turn in allowed_guesses:
        guess_letters = list(guess)
        target_letters = list(target_word)

        i = 0
        while i < 5:
            for i, letter in guess_letters:
                if letter == target_letters[i]:
                    guess_with_answer.append(color_squares['correct_place'])

                elif letter in target_letters:
                    guess_with_answer.append(color_squares['correct_letter'])

                else:
                    guess_with_answer.append(color_squares['incorrect_letter'])
        
            i = i + 1

        return guess_with_answer
                


if __name__ == '__main__':
    console = Console()
    console.print(welcome_message)
    print(target_word)
    guess = input("Enter your word: ")

    if len(guess) > 5:
        print("Please enter a 5 letter word.")
        
    check_guess(guess)
    print(check_guess)