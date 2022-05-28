import random

paper = ''' _ __   __ _ _ __   ___ _ __
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |
| .__/ \__,_| .__/ \___|_|
| |         | |
|_|         |_|
'''
print(paper)



rock = '''
           _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
'''
print(rock)

sicssors = '''
                                                                                  
,adPPYba, 88  ,adPPYba, ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" 88 a8"     "" I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  88 8b          `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I 88 "8a,   ,aa aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"' 88  `"Ybbd8"' `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
                                                                              
'''
print(sicssors)
game_images = [rock, paper, sicssors]

user_choice = int(input("what do you choose? type 0 for rock, 1 for paper or 2 for sicssors \n"))
print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print(f"computer chose {computer_choice}")
if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number, you lost")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you loose")
elif computer_choice > user_choice:
    print("you loose")
elif user_choice < computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("it is a draw")
else:
    print("you typed an invalid number, you lost")
