from random import randint


print "Lets play Rock, Paper, Sissors"

player1 = raw_input("Enter you selection here: ")
player2 = raw_input("Enter you selection here: ")

def compare(player1, player2):
    
    if (player1 == "rock") and (player2 == "sissors"):
        return("Player 1 WINS!!")
        
    elif (player1 == "sissors") and (player2 == "paper"):
        return ("Palyer 1 WINS!!") 
        
    elif (player1 == "paper") and (player2 == "rock"):
        return ("Player 1 WINS!!")
        
    else:
         ("Player 2 WINS!!")  
        

print(compare(player1, player2))
        
    
    
  

    