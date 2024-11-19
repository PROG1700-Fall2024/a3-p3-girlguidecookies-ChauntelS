#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     
#Student Name:  
# YOUR CODE STARTS HERE, each line must be indented (one tab)
#Ask the user how many guides sold cookies.
# def GGuideStats():

#Ask the user how many guides sold cookies.
# def GGuideStats():
nameList = []
soldBoxes = []
gGuideStats = int(input("Enter number of Guides that participated in event: "))

#Calculate and output a list of all guide names.
def giudeInfo(nameList, soldBoxes, gGuideStats):
    for i in range(gGuideStats):
        GgName = input(f"Enter the name of guide #{i + 1}: ")
        nameList.append(GgName)
        box = input(int(f"Enter the amount of boxes sold by {GgName}: "))
        soldBoxes.append(box)
    return nameList,soldBoxes

def totalBox(soldBoxes):
    totalSoldBox = sum(soldBoxes)
    return totalSoldBox


def averageBoX(soldBoxes, totalSoldBox):
    averageSold = totalSoldBox / soldBoxes
    return averageSold

#Prizes 
firstPrize = print("A tirp to the Girl Guide Jamboree!")
aAPrize = print("Above Average Badge!")
effortP = print("left over cookies!")
tryHarder = print("nothing")
maxWinner = soldBoxes.index(len(nameList))

#Winner calculations 
guideName, boxNum = giudeInfo
totalAmount = totalBox
averageAmount = averageBoX

for i in range(gGuideStats):
    if soldBoxes == maxWinner:
        print(firstPrize)
    elif soldBoxes > averageAmount:
        print(aAPrize)





#Winner calculations 



#Calculate the average sales.

#Determine and display the prize each guide won based on their sales.
    # YOUR CODE ENDS HERE
