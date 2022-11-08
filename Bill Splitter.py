import random

number_of_friends = int(input('Enter the number of friends joining (including you):\n'))
if number_of_friends <= 0:
    print('\nNo one is joining for the party')
    exit()

print('\nEnter the name of every friend (including you), each on a new line:')
names = [input() for x in range(0, number_of_friends)]

dict_friends = dict.fromkeys(names, 0)

bill_value = int(input('\nEnter the total bill value:\n'))

lucky = input('\n Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
if lucky == 'Yes':
    lucky_name = random.choice(list(dict_friends.keys()))
    print(f'\n{lucky_name} is the lucky one!\n')

    split_value = round(bill_value / (number_of_friends - 1), 2)

    for name in dict_friends.keys():
        if name != lucky_name:
            dict_friends[name] = split_value

    print(dict_friends)
else:
    print('\nNo one is going to be lucky\n')

    split_value = round(bill_value / (number_of_friends ), 2)

    for name in dict_friends.keys():
        dict_friends[name] = split_value

    print(dict_friends)
