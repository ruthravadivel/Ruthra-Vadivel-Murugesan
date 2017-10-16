print ("Welcome to the ROCK PAPER SCISSORS game!!!")
print ("------------------------------------------")
print
user_name1 = input(" Player 1, what is your name? ")
user_name2 = input(" Player 2, what is your name? ")
print
lister = [0, 0,0]
for i in range(0,5):
    print ("Round" , i+1)
    print ("-------")
    
    def get_player1_choice(user_name1):
        user_input1 = input(" %s, what is your choice R, P or S? " % user_name1)
        if user_input1 == "r" or user_input1 == "R"  :
            print (" You chose ROCK.")
            return user_input1
        elif user_input1 == "p" or user_input1 == "P" :
            print (" You chose PAPER.")
            return user_input1
        elif user_input1 == "s" or user_input1 == "S" :
            print (" You chose SCISSORS.")
            return user_input1
        else:
            print ("  *** Error Invalid Input.")
            return "Error"

    def get_player2_choice(user_name2):
        user_input2 = input(" %s, what is your choice R, P or S? " % user_name2)
        if user_input2 == "r" or user_input2 == "R":
            print (" You chose ROCK.")
            return user_input2
        elif user_input2 == "p" or user_input2 == "P" :
                print (" You chose PAPER.")
                return user_input2
        elif user_input2 == "s" or user_input2 == "S" :
            print (" You chose SCISSORS.")
            return user_input2
        else:
            print ("  *** Error Invalid Input.")
            return "Error"

    def get_winner(player1_choice, player2_choice, user_name1, user_name2):
        player1_choices = player1_choice.lower()
        player2_choices = player2_choice.lower()
        if player1_choices == "r" and player2_choices == "s":
            print (" The winner is of Round",i+1,"is",user_name1,".")
            print
            return "Player1"
        elif player1_choices == "r" and player2_choices == "p":
                print (" The winner is of Round",i+1,"is",user_name2,".")
                print
                return "Player2"
        elif player1_choices == "s" and player2_choices == "p":
            print (" The winner is of Round",i+1,"is",user_name1,".")
            print
            return "Player1"
        elif player1_choices == "s" and player2_choices == "r":
                print (" The winner is of Round",i+1,"is",user_name2,".")
                print
                return "Player2"
        elif player1_choices == "p" and player2_choices == "r":
            print (" The winner is of Round",i+1,"is",user_name1,".")
            print
            return "Player1"
        elif player1_choices == "p" and player2_choices == "s":
                print (" The winner is of Round",i+1,"is",user_name2,".")
                print
                return "Player2"
        elif player1_choices == "error":
            print (" The winner is", user_name2,".")
            return "Player2"
        elif player2_choices == "error":
                print (" The winner is", user_name1,".")
                return "Player1"
        else:
            print (" Round",i+1,"is a tie.")
            print
            return "Tie"
        
    def record_win(record, lister):
            if record == "Player1":
                lister[0] +=1
                return lister[0]
            elif record == "Player2":
                lister[1] +=1
                return lister[1]
            else:
                lister[2] += 1
                return lister[2]
    
    player1_choice = get_player1_choice(user_name1)
    player2_choice = get_player2_choice(user_name2)
    winner = get_winner(player1_choice, player2_choice,user_name1,user_name2)
    record_win(winner, lister)

print
print ("Summary")
print ("---------")
if lister[0] > lister[1] and lister[0] > lister[2]:
    print ("The final winner is", user_name1,",who won",lister[0], "rounds and defeated", user_name2,",who won",lister[1],"rounds.")
    print ("Congrats", user_name1,"!")
elif lister[1] > lister[0] and lister[1] > lister[2]:
    print ("The final winner is", user_name2,",who won",lister[1], "rounds and defeated", user_name1,",who won",lister[0],"rounds.")
    print ("Congrats", user_name2,"!")
else:
    print ("The game is a tie between",user_name1,"and",user_name2,".")
    print ("Congrats", user_name1,"and",user_name2,"!")

