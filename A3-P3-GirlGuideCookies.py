#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     W0239497
#Student Name:  Chauntel Smith
# YOUR CODE STARTS HERE, each line must be indented (one tab)
#Input Guide name and boxes sold and store them in 2 lists
def giudeInfo(gGuideStats):
    nameList = []
    soldBoxes = []
    for i in range(gGuideStats):
        gGName = input(f"\nEnter the name of guide #{i + 1}: ")
        nameList.append(gGName)
        boxNum = int(input(f"Enter the amount of boxes sold by {gGName}: "))
        soldBoxes.append(boxNum)
    return nameList,soldBoxes

#average calculations
def averageCalculations(soldBoxes):
    totalSoldBox = sum(soldBoxes)
    average = totalSoldBox/len(soldBoxes)
    return average

#max calculations
def maxCalculations(soldBoxes):
    maxBox = max(soldBoxes)
    indexOfMax = soldBoxes.index(maxBox)
    return maxBox,indexOfMax

# #Prizes calculations
def prizeCalculations(nameList,soldBoxes,average,indexOfMax):
    winnerList = []
    for i in range(len(nameList)):
        if i == indexOfMax:
            winnerList.append(f"{nameList [i]}              -A trip to the Girl Guide Jamboree in Aruba!")
        elif soldBoxes[i] > average:
            winnerList.append(f"{nameList [i]}              -Super Seller Badge!")
        elif soldBoxes[i] > 0:
            winnerList.append(f"{nameList [i]}              -Left over cookies!")
        else:
            winnerList.append(f"{nameList [i]}              -")
    return winnerList

    #Main Program
def main():
    print("\nGirl Guide Cookie Sell-off Calculator!\n")
    #Loop to restart if the user imputs the wrong values
    while True:
        gGuideStats = int(input("Enter number of Guides that participated in event: "))
        nameList, soldBoxes = giudeInfo(gGuideStats)
        correct = input("\nIs the information entered correct? (Y/N): ")
        if correct.upper() == "Y":
            averavge = averageCalculations(soldBoxes)
            maxBox,indexOfMax = maxCalculations(soldBoxes)
            winnerList = prizeCalculations(nameList,soldBoxes,averavge,indexOfMax)
            #Determine and display the prize each guide won based on their sales.
            print(f"\nThe average number of boxes sold by each guide was {averavge:0.1f}\n")
            print("Guide                        Prize Won:")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------")
            
            for winner in winnerList:       #<<--- I used this in program one, AI reminded me I could use a for loop with "day" replacing "i" (for day in slackDays)
                print(winner)               #and "hour" to replace "j" in "hours" to iterate over the slackDaysList 
            break                           #after the condition was applied and search the day applied and its correseponding hour to call them
        else:                               # I decided to try it in this program as well, I believe I am using it correctly
            print("Sorry about that, lets try again!") 
main()


    # YOUR CODE ENDS HERE
