import csv, os, sys
from decimal import *

tripPath=sys.argv[1] if len(sys.argv) > 1 else './trips/'
tabulation="\n    "


def parseCSV(file):
    csvFile = open(file, "r")
    csvData = list(csv.reader(csvFile, delimiter=","))
    csvFile.close()
    return csvData


def calcTotals(tripItems):
    base=0
    worn=0
    food=0

    for item in tripItems:
        isWorn = item[8]
        isFood = item[9]
        if isWorn.lower() != "":
            worn += 1
        elif isFood.lower() != "":
            food += 1
        else:
            base += 1

    return( \
        tabulation + "Total:   " + str(len(tripItems)) + \
        tabulation + "Base:    " + str(base) + \
        tabulation + "Worn:    " + str(worn) + \
        tabulation + "Food:    " + str(food))


def calcWeight(tripItems):
    total=0
    base=0
    worn=0
    food=0
    nullValues=0

    for item in tripItems:
        quantity = item[3]
        value = item[4]
        isWorn = item[8]
        isFood = item[9]

        if all(val != "" for val in [quantity, value]):
            if isWorn.lower() != "":
                worn += int(quantity) * float(value)
            elif isFood.lower() != "":
                food += int(quantity) * float(value)
            else:
                base += int(quantity) * float(value)
        else:
            nullValues += 1

        total = (base + worn + food)

    return ( \
        tabulation + "Total:   " + gramsToLBS(total) + "lbs" + \
        tabulation + "Base:    " + gramsToLBS(base) + "lbs" +  \
        tabulation + "Worn:    " + gramsToLBS(worn) + "lbs" +  \
        tabulation + "Food:    " + gramsToLBS(food) + "lbs" +  \
        nullValueFormat(nullValues))


def calcCost(tripItems):
    total=0
    base=0
    worn=0
    food=0
    nullValues=0

    for item in tripItems:
        quantity = item[3]
        value = item[7]
        isWorn = item[8]
        isFood = item[9]

        if all(val != "" for val in [quantity, value]):
            if isWorn.lower() != "":
                worn += int(quantity) * Decimal(value)
            elif isFood.lower() != "":
                food += int(quantity) * Decimal(value)
            else:
                base += int(quantity) * Decimal(value)
        else:
            nullValues += 1

        total = (base + worn + food)

    return ( \
        tabulation + "Total:   " + "${:,.2f}".format(total) + \
        tabulation + "Base:    " + "${:,.2f}".format(base) + \
        tabulation + "Worn:    " + "${:,.2f}".format(worn) + \
        tabulation + "Food:    " + "${:,.2f}".format(food) + \
        nullValueFormat(nullValues))


def calcCategories(tripItems):
    tmpList = {}
    nullValues = 0

    for item in tripItems:
        category = item[1]
        if category not in tmpList:
            tmpList[category] = 1
        else:
            tmpList[category] += 1

    categoryList = [[category, count] for category, count in tmpList.items()]

    resultList = ""
    for result in categoryList:
        resultList += tabulation + result[0] + ": " + str(result[1])
        
        categoryWeight = 0
        categoryValue = 0
        for item in tripItems:
            if result[0] == item[1]:
                if item[4] != "":
                    categoryWeight += float(item[4])
                if item[7] != "":
                    categoryValue += Decimal(item[7])

        resultList += "\n        Weight:   " + gramsToLBS(categoryWeight) + "lbs"
        resultList += "\n        Value:    " + "${:,.2f}".format(round(categoryValue,2))

    return resultList


def gramsToLBS(grams):
    return str(round((float(grams) / 453.59237),2))


def nullValueFormat(value):
    if value is not None and value > 0:
        return tabulation + "\033[91mNo Data: " + str(value) + "\033[0m"
    else:
        return ""


def main():
    listOfTrips = []

    if os.path.isdir(tripPath):
        for file in os.listdir(tripPath):
            listOfTrips.append((file,parseCSV(tripPath + file)))
    elif os.path.isfile(tripPath):
        listOfTrips.append((tripPath,parseCSV(tripPath)))

    for trip in listOfTrips:
        tripName = trip[0]
        tripItems = trip[1]
        print("Trip: " + tripName)
        print("\nTotal Items: " + calcTotals(tripItems))
        print("\nTotal Weight: " + calcWeight(tripItems))
        print("\nTotal Cost: " + calcCost(tripItems))
        print("\nTotal Categories: " + calcCategories(tripItems))
        print("-----------------------------------\n")

if __name__ == "__main__":
    main()
