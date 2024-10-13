# QUESTION :
# Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
# and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

# ALL THE FUNCTIONS WORK FOR BOTH
# DECREASING LIST AND INCREASING LIST


# FUNCTION WHICH STARTS TO CHECK FROM MIDDLE
def dataFinder_fromMiddle(card_list,askedNumber):
    steps=1
    if len(card_list)!=0:
        if len(card_list)>1:
            if card_list[0]>card_list[1]:
                minus_or_plus_one=-1
            else:
                minus_or_plus_one=1
        half_of_list=len(card_list)
        if half_of_list%2==1:
            half_of_list-=1
            half_of_list//=2
        elif half_of_list%2==0:
            half_of_list//=2

        checked_cards = []
        for i in range(len(card_list)):
            checked_cards.append(i)

            chosen_card=card_list[half_of_list-1]
            checked_cards[i]=chosen_card
            if checkRepetition(checked_cards):
                break

            if half_of_list==len(card_list) and chosen_card!=askedNumber:
                break
            elif half_of_list==1 and chosen_card!=askedNumber:
                break
            if chosen_card==askedNumber:
                print("You have found the card in only "+ steps.__str__() +" STEPS!")
                return steps
            elif chosen_card<askedNumber:
                half_of_list+=minus_or_plus_one
            else:
                half_of_list-=minus_or_plus_one
            steps+=1
        print("The card you are looking for is not in the deck :(")
        return 100
    else:
        print("There are no cards in the deck")
        return 100
        # checkRepetition is inside dataFinder_fromMiddle
def checkRepetition(checked_cards):
    for i in range(len(checked_cards)-2):
        temp = checked_cards[i]
        if checked_cards[i + 2] is not None and temp == checked_cards[i + 2]:
            return True
    return False

# FUNCTION WHICH STARTS TO CHECK FROM THE CLOSEST END OF THE CARD LIST
def dataFinder_fromClosestEnd(card_list,askedNumber):
    steps = 1
    if len(card_list)!=0:
        if len(card_list)>1:
            if card_list[0]>card_list[1]:
                minus_or_plus_one=-1
            else:
                minus_or_plus_one=1
        start = 0
        end = len(card_list)-1
        index=-1
        if card_list[end]>askedNumber:
            index=end
            start_end=False
        elif card_list[start] < askedNumber:
            index=start
            start_end=True
        elif abs(card_list[start]-askedNumber)>abs(card_list[end]-askedNumber):
            index=end
            start_end=False
        else:
            index=start
            start_end=True
        if len(card_list)!=1:
            for_range = len(card_list)
        else:
            for_range=1
        for i in range(for_range):
            if checkIfPassed(card_list,index,askedNumber):
                break
            if not start_end and index-1 >=0 and askedNumber < card_list[index]<card_list[index-1]:
                break
            if  start_end and index+1<=len(card_list) and askedNumber>card_list[index]>card_list[index+1]:
                break
            if card_list[index]==askedNumber:
                print("You have found the card in only "+steps.__str__()+" STEPS!")
                return steps
            elif start_end==True:
                index-=minus_or_plus_one
            elif start_end==False:
                index+=minus_or_plus_one

            steps+=1
        print("The card you are looking for is not in the deck :(")
        return 100

    else:
        print("There are no cards in the deck")
        return 100
        #checkIfPassed is inside dataFinder_fromClosestEnd
def checkIfPassed(card_list,index,askedNum):
    if card_list[index-1]>askedNum and card_list[index]<askedNum:
        return True
    return False


# LINEAR CHECK. (JUST TO PUT IT)
def linearCheck(card_list,askedNum):
    if len(card_list)>0:
        for index in range(len(card_list)):
            if card_list[index]==askedNum:
                print("You have found the card in only "+ index.__str__()+" STEPS!")
                return index

        print("The card you are looking for is not in the deck :(")
        return 100
    elif len(card_list)==0:
        print("THERE IS NO CARDS IN THIS DECK")
        return 100

# BINARY SEARCH with my method
def binarySearch(card_list,askedNum):
    if len(card_list)>0:
        if len(card_list)>1:
            if card_list[0]>card_list[1]:
                minus_or_plus_one=-1
            else:
                minus_or_plus_one=1
        steps=1
        power=2
        current_index = len(card_list)//2
        for index in range(len(card_list)):
            if current_index<0 or current_index>len(card_list)-1:
                break
            change = len(card_list)//pow(2,power)
            if change==0:
                change=1
            if card_list[current_index]==askedNum:
                print("You have found the card in only "+steps.__str__()+" STEPS!")
                return steps
            elif card_list[current_index]<askedNum:
                current_index+=change*minus_or_plus_one
            elif card_list[current_index]>askedNum:
                current_index-=change*minus_or_plus_one
            power+=1
            steps+=1
        print("The card you are looking for is not in the deck :(")
        return 100
    else:
        print("THERE IS NO CARD IN THE DECK")
        return 100

# RUNS THEM ALL!
def run_Them_All(card_list,askedNum,winner_count):
    print("MIDDLE")
    middle=dataFinder_fromMiddle(card_list,askedNum)
    print("CLOSEST END")
    closest_end=dataFinder_fromClosestEnd(card_list,askedNum)
    print("LINEAR CHECK")
    linear_check=linearCheck(card_list,askedNum)
    print("BINARY SEARCH")
    binary_search=binarySearch(card_list,askedNum)
    winner = min(middle,closest_end,linear_check,binary_search)
    if winner == middle:
        winner_count[0]+=1
    if winner == closest_end:
        winner_count[1]+=1
    if winner == linear_check:
        winner_count[2]+=1
    if winner == binary_search:
        winner_count[3]+=1
def main():
    # LIST OF CARDS YOU WANT TO CHECK ( WILL BE SORTED DECREASINGLY )
    new_card_list=[1,2,3,4,5,6,7,8,9,10]
    new_card_list = sorted(new_card_list, reverse=True)
    winner_list=["MIDDLE","CLOSEST END","LINEAR CHECK","BINARY SEARCH"]
    winner_count=[0,0,0,0]
    for index in range(-1,len(new_card_list)):
        print(index.__str__())
        run_Them_All(new_card_list,index,winner_count)
        print(" ")

        winner_num=max(winner_count[0],winner_count[1],winner_count[2],winner_count[3])

    if winner_num==winner_count[0]:
        print(winner_list[0]+" WON with "+winner_count[0].__str__()+" WINS")
    if winner_num == winner_count[1]:
        print(winner_list[1] + " WON with "+winner_count[1].__str__()+" WINS")
    if winner_num==winner_count[2]:
        print(winner_list[2]+" WON with "+winner_count[2].__str__()+" WINS")
    if winner_num==winner_count[3]:
        print(winner_list[3]+" WON with "+winner_count[3].__str__()+" WINS")



main()