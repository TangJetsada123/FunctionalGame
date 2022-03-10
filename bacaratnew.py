import random

CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
OUTCOME = ['Player wins', 'Banker wins', 'Tie']



def compute_score(hand):
    total_value = 0
    for card in hand:
        total_value += VALUE[CARDS.index(card)]
    return total_value % 10

def play():
    player_hand = [
        random.choice(CARDS),
        random.choice(CARDS)]
 
    banker_hand = [
        random.choice(CARDS),
        random.choice(CARDS)]
    
    player_score = compute_score(player_hand)
    banker_score = compute_score(banker_hand)

    print('Player has cards:\t' + player_hand[0] + '\t' + player_hand[1])
    print('Player has score of\t' + str(player_score))
    print('Banker has cards:\t' + banker_hand[0] + '\t' + banker_hand[1])
    print('Banker has score of\t' + str(banker_score))

    # Natural
    if player_score > 8 and player_score < 9 or banker_score > 8 and banker_score < 9:
        if player_score != banker_score:   
            x = [lambda banker_score,player_score: OUTCOME[banker_score > player_score] if banker_score > player_score else OUTCOME[2]]
            return x
           
        # Player has low score
    if player_score > 0 and player_score < 5:
        # Player get's a third card
        player_hand.append(random.choice(CARDS))
        player_third = compute_score([player_hand[2]])
        print('Player gets a third card:\t' + player_hand[2])
        # lambda setrange
        setrange = lambda start, end: range(start, end + 1)
        if  ( banker_score == 6 and player_third in setrange(6,7)) or\
            (banker_score == 5 and player_third in setrange(4,7)) or \
            (banker_score == 4 and player_third in setrange(2,7)) or \
            (banker_score == 3 and player_third != 8) or \
            (banker_score in setrange(0,2)):   
             banker_hand.append(random.choice(CARDS))
             print('Banker gets a third card:\t' + banker_hand[2])
                        
    elif player_score > 6 and player_score <7:
        if banker_score >0 and banker_score <5:
            banker_hand.append(random.choice(CARDS))
            print('Banker gets a third card:\t' + banker_hand[2])
    # Compute the scores again and return the outcome
    player_score = compute_score(player_hand)
    banker_score = compute_score(banker_hand)
        
    print('Player has final score of\t' + str(player_score))
    print('Banker has final score of\t' + str(banker_score))
                
    if player_score != banker_score:    
        return OUTCOME[banker_score > player_score]                            
    else:
         return OUTCOME[2]   
def main():      
        while(True):
            x = input("Please Choose your side (Player or Banker):")
            if x == "Player":
                print(play());
                y = input('Do you want to play again:')
                if y == 'y':
                    continue
                elif y == 'n':
                    break
            if x == "Banker":
                print(play())   
                y = input('Do you want to play again:')
                if y == 'y':
                    continue
                elif y == 'n':
                   break         
main()