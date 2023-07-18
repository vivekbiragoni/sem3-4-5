import random

def get_word():
    words = ["tiger", "lion", "rabbit", "horse", "monkey", "ant", "zebra", "bee", "hen", "elephant"]
    return random.choice(words)

def play_hangman():
    word = get_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('Good job! The letter', user_letter, 'is in the word.')
            else:
                lives = lives - 1
                print('Oops! The letter', user_letter, 'is not in the word.')
        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('Sorry, you died. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')

play_hangman()
