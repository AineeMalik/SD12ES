#Example 1

LIST = [23,45,87,34]




def TestFunction():

    Cost = 200.00
    Amort = 5.45
    Code = "ER-453"

    return Cost, Amort, Code

def CalcBonus(TotalSales):

    Bonus = TotalSales * .01

    if TotalSales < 5000.00:
        Deduct = (5000.00 - TotalSales) * .17
        Bonus -= Deduct
        Status = "Under"
    elif TotalSales >= 5000.00 and TotalSales <= 100000.00:
        Status = "Normal"
    elif TotalSales > 100000.00:
        Bonus += 500.00
        Status = "Extraordinary"
    
    return Bonus, Status


while True:

    Test = TestFunction()
    print(Test)

    print(LIST)
    LIST[1] = 54
    print(LIST)

    
    print(Test)

    print()
    #Returns a tuple with bonus amount and the status message.
    Bonus = CalcBonus(30000.00)
    print(Bonus)

    print()
    GrossPay = 1200 + Bonus[0]
    print(GrossPay)

    print()
    Continue = input("Continue (Y/N): ").upper()
    if Continue == "N":
        break

#Example 3

import datetime

while True:

    ListingNum = input("Enter the listing number: ")
    StAdd = "123 Water Street"
    NumBed = 3
    NukmBath = 2
    SqFoot = 2475

    PriceLst = []
    DateLst = []

    while True:
        while True:
            try:
                ListingPrice = input("Enter the listing price (-1 to end): ")
                ListingPrice = float(ListingPrice)
                if ListingPrice == -1:
                    break #Just breaks out of the validation loop. 
            except:
                print("Error - invalid value for listing price.")
            else:
                break
        
        if ListingPrice == -1:
            break
        
        while True:
            try:
                ListingDate = input("Enter the listing date (YYY-MM-DD): ")
                ListingDate = datetime.datetime.strptime(ListingDate, "%Y-%m-%d")
            except:
                print("Error - invalid value for the purchase date")
            else:
                break

        PriceLst.append(ListingPrice)
        DateLst.append(ListingDate)

    Status = input("Enter the status (Open, Offer Pending, Sold): ")


    print(ListingNum)
    print(PriceLst)
    print(DateLst)
    print(Status)