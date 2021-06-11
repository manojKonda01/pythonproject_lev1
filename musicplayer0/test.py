from playsound import playsound as play
def songByMood():
    while True:
        i=int(input('Howz your mood\n1. Sad\n2. Happy\n3. Mourning\n4. Depressed\n5. Calm\n6. Romantic\n7. Seducing\n8. Angry\n9. Lonely\nSelect (Enter number) : '))
        if i==1:
            print('Hey Dont feel SAD try some Cheerful Songs.Its Hard to Someone who loves you')
            play('sad.mp3')
        elif i==2:
            print('HoHo live your life Yooo')
            play('happy.mp3')
        elif i==3:
            print('Its Hard if we someone leaves us permananlty. But life gives u another such person')
            play('mourn.mp3')
        elif i == 4:
            print('Depressed? Na Na Listen to this song. Life is short a we live only once live it')
            play('dep.mp3')
        elif i == 5:
            print('Take some space')
            play('Calm.mp3')
        elif i == 6:
            print('Make Your be satisfy')
            play('rom.mp3')
        elif i == 7:
            print('>>>')
            play('vey.mp3')
        elif i == 8:
            print('Never take any decision when you are in anger. Please DOnt')
            play('anger.mp3')
        elif i == 9:
            print('No one likes You?? BE yourself there will be someone for you')
            play('lonely.mp3')
        l=input("Wanna listen more songs?\n1)press 'n' to stop\n Press any ")
        if l=='n':
            break


songByMood()
