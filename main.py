import random
import art
import game_data

#returns random account
def random_account():
    account=random.choice(game_data.data)
    return account

#compares account_a with account_b
def compare_accounts(account_a, account_b):
    a=int(account_a["follower_count"])
    b=int(account_b["follower_count"])
    if a>b:
        return "a"
    else:
        return "b"

#display game art and informations
def display_game(account_a, account_b):
    a_name=account_a["name"]
    b_name=account_b["name"]
    a_description=account_a["description"]
    b_description=account_b["description"]
    a_country=account_a["country"]
    b_country=account_b["country"]

    print(art.logo)
    print(f"\nCompare A: {a_name}, a {a_description}, from {a_country}.\n")
    print(art.vs)
    print(f"\nAgainst B: {b_name}, a {b_description}, from {b_country}.\n")

play_game=""

while play_game!="n":
    play_game=input("Do you want to play around? Hit 'n' for no or any other key for yes: ")
    
    #reset game values for another round
    game_end=False
    account_a=account_b=score=0

    if play_game!="n":
        while game_end!=True:
            #assigns in the first round values
            if account_a==0:
                account_a=random_account()
                account_b=random_account()

            #makes sure values are not the same
            while account_a==account_b:
                account_b=random_account()

            #call of compare function
            correct_answer=compare_accounts(account_a, account_b)
            display_game(account_a, account_b)
            answer=input("Who has more followers? Type 'A' or 'B':")
            if answer!=correct_answer:
                print(f"\nSorry! This was not right, you lost!\nYou achieved a score of: {score}\n")
                game_end=True
            else:
                score+=1
                print(f"\nThats right! You have a score of {score}\n")

            #when game continues
            if game_end!=True:
                account_a=account_b
                account_b=random_account()