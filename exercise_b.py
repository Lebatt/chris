#Schere Stein Papier

#Dictionary
# numconversion = {
#     0: "Rock",
#     1: "Paper",
#     2: "Scissors",
#     "q": "Quit"
#
# }
#
# choice = input("Choice: ")
#
# def tool(choice):
#     print("--- Make a choice\n --- Rock: 0\n --- Paper: 1 \n ---Scissors: 2 \n --- Quit: q")
#
#     if choice == 0:
#             print(numconversion.get(choice))
#     elif choice == 1:
#             print(numconversion.get(choice))
#     elif choice == 2:
#             print(numconversion.get(choice))
#     elif choice == "q":
#             print(numconversion.get(choice))
#     else:
#             print("Enter a valid choice")
#     return(tool(choice))

tools = (0, 1, 2, str("q"))
#1. Menu
def menu():
    print("Welcome to Rock Paper Scissors!")
    input("Player name: ")
    print(" --- MAKE A CHOICE:\n --- Rock: 0\n --- Paper: 1 \n --- Scissors: 2 \n --- Quit: q")
    #input("Choice: ")

    # if Computer > Player choice:
    #     print("SCISSORS wins against PAPER Computer scored 1 Point")
    #     print("SCORE")
    # elif Computer = Player choice
    #     print("DRAW")
    #     print("SCORE")
    # elif Computer < Player
    #     print("Player wins")
    #     print("SCORE")
    return

#2. Choice
# choice_list = ["ROCK", "PAPER", "SCISSORS", "Quit"]
# choice = input("Your Choice: ")
# choice_list.index[0] = str("ROCK")
#     choice[1] = str("PAPER")
#     choice[2] = str("SCISSORS")
def tool(choice):
    while choice not in range(0, 3):
        print("ERROR: Please enter a valid option!")
        choice = input("Choice: ")
    if choice == 0:
        print("ROCK")
    elif choice == 1:
        print("PAPER")
    elif choice == 2:
        print("SCISSORS")
    elif choice == "q":
        print("You quit the game!")
    return
#Ich bleibe in der while loop hängen!
print(menu())
choice = input("Choice: ")
print(tool(choice))
