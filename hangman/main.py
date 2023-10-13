import random

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)

end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()

    for idx in range(len(chosen_word)):
        if chosen_word[idx] == guess:
            # print('Right')
            display[idx] = guess

    print(display)
    if '_' not in display:
        end_of_game = True
