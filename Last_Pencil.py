print('How many pencils would you like to use:')
pencils = int()
while True:
    try:
        pencils = int(input())
        if pencils <= 0:
            print('The number of pencils should be positive')
        else:
            break
    except ValueError:
        print('The number of pencils should be numeric')

first = ''
while True:
    print('Who will be the first (John, Jack):')
    first = input()
    if(first != 'John' and first != 'Jack'):
        print("Choose between 'John' and 'Jack'")
        continue
    break

print('|' * pencils)

print(f"{first}'s turn")
next = ''
if(first == 'John'):
    next = "Jack"
else:
    next = 'John'
while pencils > 0:
    remove = int()
    while True:
        try:
            if first == 'Jack':
                if pencils % 4 == 0:
                    print('3')
                    remove = 3
                elif pencils % 4 == 3:
                    print('2')
                    remove = 2
                elif pencils % 4 == 2:
                    print('1')
                    remove = 1
                elif pencils % 4 == 1:
                    print('1')
                    remove = 1
                elif pencilss == 1:
                    print('1')
                    remove = 1
            else:
                remove = int(input())
            if remove > 3 or remove <= 0:
                print("Possible values: '1', '2' or '3'")
            elif remove > pencils:
                print('Too many pencils were taken')
            else:
                break
        except ValueError:
            print("Possible values: '1', '2' or '3'")
    if remove >= pencils:
        print(f"{next} won")
        break
    pencils = pencils - remove
    if(first == 'John'):
        first = 'Jack'
        next = "John"
    else:
        first = 'John'
        next = "Jack"
    print(f"{first}'s turn")
    print('|' * pencils)
