# QUESTION :
# Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
# and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.


def dataFinder_fromMiddle(card_list,askedNumber):
    steps=1
    if len(card_list)!=0:
        card_list=sorted(card_list,reverse=True)
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
            print(" Step : "+steps.__str__()+" Number : "+chosen_card.__str__())
            if chosen_card==askedNumber:
                print("You have found the card in only "+ steps.__str__() +" STEPS!")
                print("It is : "+ askedNumber.__str__())
                return 0
            elif chosen_card<askedNumber:
                half_of_list-=1
            else:
                half_of_list+=1
            steps+=1
        print("The card you are looking for is not in the deck :(")
    else:
        print("There are no cards in the deck")
def checkRepetition(checked_cards):
    for i in range(len(checked_cards)-2):
        temp = checked_cards[i]
        if checked_cards[i + 2] is not None and temp == checked_cards[i + 2]:
            return True
    return False
def dataFinder_fromClosestEnd(card_list,askedNumber):
    steps = 1
    if len(card_list)!=0:
        card_list = sorted(card_list, reverse=True)
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
            print("Step : "+steps.__str__()+" Number : "+card_list[index].__str__())
            if card_list[index]==askedNumber:
                print("You have found the card in only "+steps.__str__()+" STEPS!")
                print("It is : " + askedNumber.__str__())
                return 0
            elif start_end==True:
                index+=1
            elif start_end==False:
                index-=1

            steps+=1
        print("The card you are looking for is not in the deck :(")

    else:
        print("There are no cards in the deck")
def checkIfPassed(card_list,index,askedNum):
    if card_list[index-1]>askedNum and card_list[index]<askedNum:
        return True
    return False
"""def linearCheck(card_list,askedNum):
    if len(card_list)>0:
        for index in range(len(card_list)):
            print(index)
            print(card_list[index])
            if card_list[index]==askedNum:
                print("YOU FOUND THE CARD AT INDEX : "+ index.__str__())
                return 0

        print("THE CARD DOESN'T EXIST")
    elif len(card_list)==0:
        print("THERE IS NO CARDS IN THIS DECK")
"""
# LIST OF CARDS YOU WANT TO CHECK ( WILL BE SORTED DECREASINGLY )
new_card_list={1,2,3,4,6,7,8,9,10,11,12,13,14,15,17}

# FUNCTION WHICH STARTS TO CHECK FROM MIDDLE
print("MIDDLE")
dataFinder_fromMiddle(new_card_list,17)

# FUNCTION WHICH STARTS TO CHECK FROM THE CLOSEST END OF THE CARD LIST
print("CLOSEST END")
dataFinder_fromClosestEnd(new_card_list,17)

"""
# LINEAR CHECK. (JUST TO PUT IT)
print("LINEAR CHECK")
linearCheck(new_card_list,17)
"""