import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)

end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()

    for idx in range(len(chosen_word)):
        if chosen_word[idx] == guess:
            display[idx] = guess

    print(' '.join(display))
    
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print('You lose.')
        
    if '_' not in display:
        end_of_game = True
        print('You win.')
    
    print(stages[lives])