import random

name = input('Enter your name:')
print(f'Hello, {name}')

name_rating = open('rating.txt', 'r').readlines()
score = 0;
for line in name_rating:
    if name in line:
        score = int(line.split(' ')[1])
        
options = input()
if options == '':
    options = ["rock", "paper", "scissors"]
else:
    options = options.split(',')
    
print("Okay, let's start")

while True:
    user_option = input()
    if user_option == '!exit':
        print('Bye!')
        break
    elif user_option == "!rating":
        print(f'Your rating: {score}')
        continue
    elif user_option not in options:
        print('Invalid input')
        continue
    
    comp_option = random.choice(options)

    if user_option == comp_option:
        print(f'The is a draw ({user_option})')
        score += 50
        continue
        
    new_set_of_options = [*options[options.index(user_option)+1:],*options[:options.index(user_option)]]
    stronger_options = new_set_of_options[:int(len(new_set_of_options)/2)]
    weaker_options = new_set_of_options[int(len(new_set_of_options)/2):]
    
    if comp_option in stronger_options:
        print(f"Sorry, but the computer chose {comp_option}")
        continue
    elif comp_option in weaker_options:
        print(f'Well done. The computer chose {comp_option} and failed')
        score += 100
        continue
    
    
