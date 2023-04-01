import random
import time


print('--------------')
print("Bot: Welcome Buddy!")
print('--------------')

print("Bot: What's your name bravo ?")
name = input(' ')

while True:
    print("Bot: Choose Head or Tail")
    choose1 = input(f'{name}: ').lower()
    if choose1 == 'head':
        time.sleep(1)
        print('Bot: Ok I will take Tail this time.')
    elif choose1 == 'tail':
        time.sleep(1)
        print('Bot: Ok I will take Head. Boom to your face.')
        time.sleep(1)
        print('Bot: hahaha')

        print("----x-----x------x------x---x-----x------x------x-----x-----x------x------x------x-----x--")
    time.sleep(1)
    print('Bot: Now we have to pull out our fingers or throw numbers lets see who gon take a shot! :)')
    time.sleep(2)
    print('Bot: You go first!')
    print('_______________________________________________________________________________________________')
    choice_mine = int(input(f'{name}: '))
    choice_Bot = random.randint(1, 5)
    print('Bot:', choice_Bot)
    if choose1 == 'head':
        if choice_mine == 1 and choice_Bot == 1:
            print("Bot: Hahaha I won!!")
        elif choice_mine == 1 and choice_Bot == 2:
            print('Bot: Damn you won :( ')
        elif choice_mine == 1 and choice_Bot == 3:
            print('Bot: I won I wonnnnn Tails haha')
        elif choice_mine == 1 and choice_Bot == 4:
            print('Bot: Congrats Bravo You Won :(')
        elif choice_mine == 1 and choice_Bot == 5:
            print('Bot: Ulllllll Tail Wonnn!!')

        elif choice_mine == 2 and choice_Bot == 1:
            print("Bot: Damn Bro You won :(")
        elif choice_mine == 2 and choice_Bot == 2:
            print('Bot: I won haha!! ')
        elif choice_mine == 2 and choice_Bot == 3:
            print('Bot: Congrats Bravo You Won :(')
        elif choice_mine == 2 and choice_Bot == 4:
            print('Bot: I won I wonnnnn Tails haha')
        elif choice_mine == 2 and choice_Bot == 5:
            print('Bot: You Won :( ')

        elif choice_mine == 3 and choice_Bot == 1:
            print('Bot: I won haha!! ')
        elif choice_mine == 3 and choice_Bot == 2:
            print("Bot: Damn Bro You won :(")
        elif choice_mine == 3 and choice_Bot == 3:
            print('Bot: I won I wonnnnn Tails haha')
        elif choice_mine == 3 and choice_Bot == 4:
            print('Bot: Congrats Bravo You Won :(')
        elif choice_mine == 3 and choice_Bot == 5:
            print('Bot: I wonnnnnnnnn!!! ')

        elif choice_mine == 4 and choice_Bot == 1:
            print("Bot: Damn Bro You won :(")
        elif choice_mine == 4 and choice_Bot == 2:
            print('Bot: I won haha!! ')
        elif choice_mine == 4 and choice_Bot == 3:
            print('Bot: Congrats Bravo You Won :(')
        elif choice_mine == 4 and choice_Bot == 4:
            print('Bot: I won I wonnnnn Tails haha')
        elif choice_mine == 4 and choice_Bot == 5:
            print('Bot: You Won :( ')

        elif choice_mine == 5 and choice_Bot == 1:
            print('Bot: I won haha!! ')
        elif choice_mine == 5 and choice_Bot == 2:
            print("Bot: Damn Bro You won :(")
        elif choice_mine == 5 and choice_Bot == 3:
            print('Bot: I won I wonnnnn HEADSSS haha')
        elif choice_mine == 5 and choice_Bot == 4:
            print('Bot: Congrats Bravo You Won :(')
        elif choice_mine == 5 and choice_Bot == 5:
            print('Bot: I wonnnnnnnnn!!! ')

    elif choose1 == 'tail':
        if choice_mine == 1 and choice_Bot == 1:
            print('Bot: Damn you won :( ')
        elif choice_mine == 1 and choice_Bot == 2:
            print("Bot: Hahaha I won!!")
        elif choice_mine == 1 and choice_Bot == 3:
            print('Bot: Congrats Bravo You Won :(')
        elif choice_mine == 1 and choice_Bot == 4:
            print('Bot: I won I wonnnnn Head haha')
        elif choice_mine == 1 and choice_Bot == 5:
            print('Bot: yeahhh yeah i know you won :(')

        elif choice_mine == 2 and choice_Bot == 1:
            print('Bot: I won haha!! ')
        elif choice_mine == 2 and choice_Bot == 2:
            print("Bot: Damn Bro You won :(")
        elif choice_mine == 2 and choice_Bot == 3:
            print('Bot: I won I wonnnnn Heads haha')
        elif choice_mine == 2 and choice_Bot == 4:
            print('Bot: Congrats Bravo You Won :(')
        elif choice_mine == 2 and choice_Bot == 5:
            print('Bot: I won haha! :) ')

        elif choice_mine == 3 and choice_Bot == 1:
            print("Bot: Damn Bro You won :(")
        elif choice_mine == 3 and choice_Bot == 2:
            print('Bot: I won haha!! ')
        elif choice_mine == 3 and choice_Bot == 3:
            print('Bot: Congrats Bravo You Won :(')
        elif choice_mine == 3 and choice_Bot == 4:
            print('Bot: I won I wonnnnn Heads haha')
        elif choice_mine == 3 and choice_Bot == 5:
            print('Bot: You won :( ')

        elif choice_mine == 4 and choice_Bot == 1:
            print('Bot: I won haha!! ')
        elif choice_mine == 4 and choice_Bot == 2:
            print("Bot: Damn Bro You won :(")
        elif choice_mine == 4 and choice_Bot == 3:
            print('Bot: I won I wonnnnn Heads haha')
        elif choice_mine == 4 and choice_Bot == 4:
            print('Bot: Congrats Bravo You Won :(')
        elif choice_mine == 4 and choice_Bot == 5:
            print('Bot: I Won! ')

        elif choice_mine == 5 and choice_Bot == 1:
            print("Bot: Damn Bro You won :(")
        elif choice_mine == 5 and choice_Bot == 2:
            print('Bot: I won haha!! ')
        elif choice_mine == 5 and choice_Bot == 3:
            print('Bot: Congrats Bravo You Won :(')
        elif choice_mine == 5 and choice_Bot == 4:
            print('Bot: I won I wonnnnn Heads haha')
        elif choice_mine == 5 and choice_Bot == 5:
            print('Bot: You Won :(')
    else:
        print('invalid command :(')
        
    time.sleep(1)
    print('Wanna try Again ? yes/no')
    ask1 = input(f'{name}: ').lower()
    if ask1 == 'yes':
        continue
    else:
        break
    
print(f'Ok {name} see ya next time :)')

