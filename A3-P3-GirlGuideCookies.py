#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     W0239497
#Student Name:  Chauntel Smith
# YOUR CODE STARTS HERE, each line must be indented (one tab)
#Lists
# nameList = []
# soldBoxes = []
# gGuideStats = int(input("Enter number of Guides that participated in event: "))

#Calculate and output a list of all guide names.

def giudeInfo(nameList, soldBoxes, gGuideStats):
    for i in range(gGuideStats):
        GgName = input(f"Enter the name of guide #{i + 1}: ")
        nameList.append(GgName)
        box = input(int(f"Enter the amount of boxes sold by {GgName}: "))
        soldBoxes.append(box)
    return nameList,soldBoxes

#Total calculations
def totalBox(soldBoxes,nameList):
    totalSoldBox = sum(soldBoxes)
    average = totalSoldBox / len(soldBoxes)
    maxWinner = max(soldBoxes)
    indexOfMax = soldBoxes.index(len(nameList))
    return totalSoldBox,indexOfMax,maxWinner,average

#average calculations

# #Prizes calculations
def prizeCalculations(soldBoxes,nameList,average,indexOfMax):
    winnerList = []
    for i in range(len(nameList)):
        if i == indexOfMax:
            winnerList.append(f"{nameList [i]}          -A trip to the Girl Guide Jamboree")
        elif soldBoxes[i] > average:
            winnerList.append(f"{nameList [i]}          -Super Seller Badge")
        elif soldBoxes[i] > 0:
            winnerList.append(f"{nameList [i]}          -Left over cookies!")
        else:
            winnerList.append(f"{nameList [i]}          -")
    return winnerList

def main():
    nameList = []
    soldBoxes = []
    #Loop to restart if the user imputs the wrong values
    while True: 
        gGuideStats = int(input("Enter number of Guides that participated in event: "))
        nameList,soldBoxes, gGuideStats = giudeInfo(nameList, soldBoxes, gGuideStats)
        print(giudeInfo(nameList, soldBoxes, gGuideStats))
        indexOfMax,average = totalBox(soldBoxes,nameList)
        winnerList = prizeCalculations(soldBoxes,nameList,average,indexOfMax)
        correct = input("were the your inputs entered correctly? (Y/N): ")
        if correct.upper() == "Y":
            print(winnerList)   #Come back soon message
            break
        else:
            print("Sorry about that, lets try again!") 
main()

#Determine and display the prize each guide won based on their sales.
    # YOUR CODE ENDS HERE
