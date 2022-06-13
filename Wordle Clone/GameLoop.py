def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []

    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += correct_place(letter)
            wordle_pattern.append(color_squares['correct_place'])

        elif letter in answer:
            guessed += correct_letter(letter)
            wordle_pattern.append(color_squares['correct_letter'])

        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(color_squares['incorrect_letter'])
            
    return ''.join(guessed), ''.join(wordle_pattern)