
player1_score=0
player2_score=0

for play in range(3):
    player1=input("Enter your Play [Rock,Paper or Scissors] ").upper()

    from random import choice
    player2=choice(["ROCK","PAPER","SCISSORS"])

    if (player1==player2):
        player1_score=player1_score+0
        player2_score=player1_score+0

    elif (player1 =="ROCK" and player2=="PAPER"):
        player1_score=player1_score+0
        player2_score=player2_score+1
    elif (player1 =="ROCK" and player2=="SCISSORS"):
        player1_score=player1_score+1
        player2_score=player2_score+0

    elif (player1 =="PAPER" and player2=="ROCK"):
        player1_score=player1_score+1
        player2_score=player2_score+0
    elif (player1 =="PAPER" and player2=="SCISSORS"):
        player1_score=player1_score+0
        player2_score=player2_score+1

    elif (player1 =="SCISSORS" and player2=="ROCK"):
        player1_score=player1_score+0
        player2_score=player2_score+1
    elif (player1 =="SCISSORS" and player2=="PAPER"):
        player1_score=player1_score+1
        player2_score=player2_score+0
    else:
        print("Invalid input")
if (player1_score>player2_score):
    print( f"player1_score is {player1_score},player2_score is {player2_score} = player1 is the  winner")
elif (player1_score<player2_score):
    print(f"player1_score is {player1_score},player2_score is {player2_score} =player2 is the winner")
else:
    print(f"player1_score is {player1_score},player2_score is {player2_score} =No winner")






  



