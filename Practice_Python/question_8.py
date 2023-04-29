# QUESTION - 8 

# Make a two-player Rock-Scissors game. 
# Rules;
# Rock beats scissors
# Scissors beats paper
# Paper beats rock 

player_1 = input("Choose from rock, paper or scissors ") 
player_2 = input("Choose from rock, paper and scissors ")

def game(p1, p2):
    if (p1 == p2):
        return "It's a tie"
    elif (p1 == "rock"):
        if (p2 == "scissors"):
            return ("Rock wins!")
        else:
            return ("Paper wins!")

    elif (p1 == "scissors"):
        if (p2 == "paper"):
            return ("Scissors wins!")
        else:
            return("Rock wins!")
    elif (p1 == "paper"):
        if (p2 == "rock"):
            return ("Paper wins!")
        else:
            return("Scissors wins")
    else:
        return ("Invalid input, try again!")
    
print(game(player_1,player_2))


