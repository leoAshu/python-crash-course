import os
import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)
lives = 6

chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    os.system('cls')

    if guess in display:
        print(f'You\'ve already guessed {guess}.')

    for idx in range(len(chosen_word)):
        if chosen_word[idx] == guess:
            display[idx] = guess

    print(' '.join(display))
    
    if guess not in chosen_word:
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
        lives -=1
        if lives == 0:
            end_of_game = True
            print('You lose.')
        
    if '_' not in display:
        end_of_game = True
        print('You win.')
    
    print(stages[lives])
