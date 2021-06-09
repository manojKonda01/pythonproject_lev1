import random
poss=['rock', 'paper','scissor']
com=0
play=0
while True:
    comp = random.choice(poss)
    turn = input("Rock Paper Scissor ?? : ")
    print('Computer : ',comp)
    if turn == comp:
        print('Tie!!!!!')
    elif turn == "rock":
        if comp == "paper":
            print("You lose!")
            com += 1
        elif comp=="scissor":
            print("You win!")
            play += 1
    elif turn == "paper":
        if comp == "scissor":
            print("You lose!")
            com += 1
        elif comp=="rock":
            print("You win!")
            play += 1
    elif turn == "scissor":
        if comp == "Rock":
            print("You lose..." )
            com += 1
        elif comp=="paper":
            print("You win!")
            play += 1

    i=input('Wanna play again? (y/n): ')
    if i=='n':
        print('Your score: {}\nCOmputer score: {}'.format(play,com))
        break
    elif i=='y':
        pass