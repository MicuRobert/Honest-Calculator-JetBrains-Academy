import random
print('H A N G M A N \n')

type = ''
results = [0, 0]
while True:
    type = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if type == "play":
        words = ['python', 'java', 'swift', 'javascript']
        word = random.choice(words)
        word_to_show = "-" * len(word)
        used_letters = []
        
        attempts = 8
        used = ''
        
        while attempts > 0:
            print(word_to_show)
            if word_to_show.find("-") == -1:
                print(f'You guessed the word {word}!')
                print('You survived!')
                results[0] += 1
                break
            letter = input('Input a letter: \n')
            if len(letter) > 1 or len(letter) == 0:
                print('Please, input a single letter.')
            elif not letter.isalpha() or letter.isupper():
                print('Please, enter a lowercase letter from the English alphabet.')
            elif used.find(letter) != -1:
                print("You've already guessed this letter.")
            else:
                used = used + letter
                if word.find(letter) == -1:
                    print(f"That letter doesn't appear in the word. # {attempts} \n")
                    attempts -= 1
                elif word_to_show.find(letter) >= 0:
                    print(f'No improvements. #{attempts}')
                    attempts -= 1
                else:
                    indices = [index for index, element in enumerate(list(word)) if element == letter]
                    word_to_show = list(word_to_show)
                    for x in indices:
                        word_to_show[x] = letter
                    word_to_show = "".join(word_to_show)
        if attempts == 0:
            results[1] += 1
            print('You lost!')
    elif type == "results":
        print(f'You won: {results[0]} times')
        print(f'You lost: {results[1]} times')
    elif type == 'exit':
        break
