import os
import random
choices = [
    ("rock", "\033[0;31m", "\033[0;31m"),    # Red color for rock symbol
    ("paper", "\033[1;37m", "\033[1;37m"),   # Dark white color for paper symbol
    ("scissors", "\033[1;33m", "\033[1;33m")  # Yellow color for scissors symbol
]
def determine_winner(player, opp):
    # Check if it's a tie
    if player == opp:
        return "It's a tie game!"
    # Check if the player won
    elif ((player == "rock" and opp == "scissors") or
          (player == "paper" and opp == "rock") or
          (player == "scissors" and opp == "paper")):
        return "Congratulations! You Won!"
    # If they didn't win, then we know the computer won
    else:
        return "AI Won,Please Try Again!"
def print_choices():
    # Rock
    rock_color = choices[0][1]
    rock_symbol_color = choices[0][2]
    print(rock_color + "Rock" + "\033[0m")
    print(rock_symbol_color + """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """ + "\033[0m")
    # Paper
    paper_color = choices[1][1]
    paper_symbol_color = choices[1][2]
    print(paper_color + "Paper" + "\033[0m")
    print(paper_symbol_color + """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """ + "\033[0m")
    # Scissors
    scissors_color = choices[2][1]
    scissors_symbol_color = choices[2][2]
    print(scissors_color + "Scissors" + "\033[0m")
    print(scissors_symbol_color + """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """ + "\033[0m")
def play_rock_paper_scissors():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[0;32mWelcome to Rock Paper Scissors!\033[0m")  # Green color for the welcome message
    playing = True
    while playing:
        print_choices()
        print("\033[1;37mChoose\033[0m \033[0;31mrock\033[0m\033[1;37m, \033[0mpaper\033[1;37m, \033[0mor\033[1;37m, \033[1;33mscissors\033[0m")
        print("Or enter \033[0;31mq\033[0m to quit")
        player_choice = input().lower()
        if player_choice == "q":
            playing = False
        elif player_choice in [choice[0] for choice in choices]:
            opp_choice = get_opponent_choice(player_choice)
            player_choice_name = choices[[i[0] for i in choices].index(player_choice)][1] + player_choice.capitalize() + "\033[0m"
            player_choice_symbol_color = choices[[i[0] for i in choices].index(player_choice)][2]
            opp_choice_name = choices[[i[0] for i in choices].index(opp_choice[0])][1] + opp_choice[0].capitalize() + "\033[0m"
            print("You Chosen:", player_choice_name)
            print("AI Chosen:", opp_choice_name)
            print(determine_winner(player_choice, opp_choice[0]))
        else:
            print("\033[91mInvalid input, please type rock, paper, or scissors\033[0m")
        if playing:
            replay = input("Wanna play again? Type \033[1;32myes\033[0m to replay or \033[0;31mno\033[0m to end the game\n").lower()
            print()
            playing = replay == "yes"
            os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[0;31mThanks for Playing!\033[0m")
def get_opponent_choice(player_choice):
    remaining_choices = [choice for choice in choices if choice[0] != player_choice]
    return random.choice(remaining_choices)
play_rock_paper_scissors()


