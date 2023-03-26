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
        if isWorn.lower() == "worn":
            worn += 1
        elif isFood.lower() == "consumable":
            food += 1
        else:
            base += 1

    return( \
        tabulation + "Total: " + str(len(tripItems)) + \
        tabulation + "Base: " + str(base) + \
        tabulation + "Worn: " + str(worn) + \
        tabulation + "Food: " + str(food))


def calcWeight(tripItems):
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
            if isWorn.lower() == "worn":
                worn += int(quantity) * float(value)
            elif isFood.lower() == "consumable":
                food += int(quantity) * float(value)
            else:
                base += int(quantity) * float(value)
        else:
            nullValues += 1

        total = (base + worn + food)

    return ( \
        tabulation + "Total: " + gramsToLBS(total) + \
        tabulation + "Base: " + gramsToLBS(base) + \
        tabulation + "Worn: " + gramsToLBS(worn) + \
        tabulation + "Food: " + gramsToLBS(food) + \
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
            if isWorn.lower() == "worn":
                worn += int(quantity) * Decimal(value)
            elif isFood.lower() == "consumable":
                food += int(quantity) * Decimal(value)
            else:
                base += int(quantity) * Decimal(value)
        else:
            nullValues += 1

        total = (base + worn + food)

    return ( \
        tabulation + "Total: " + str(f'{total:,}') + \
        tabulation + "Base: " + str(f'{base:,}') + \
        tabulation + "Worn: " + str(f'{worn:,}') + \
        tabulation + "Food: " + str(f'{food:,}') + \
        nullValueFormat(nullValues))


def calcCategories(tripItems):
    categoryList = {}
    nullValues = 0

    for item in tripItems:
        category = item[1]
        if category not in categoryList:
            categoryList[category] = 1
        else:
            categoryList[category] += 1

    resultList = [[category, count] for category, count in categoryList.items()]

    returnList = ""
    for result in resultList:
        returnList += tabulation + result[0] + ": " + str(result[1])

    return str(returnList)


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
        print("\nItems: " + calcTotals(tripItems))
        print("\nWeight (lbs): " + calcWeight(tripItems))
        print("\nCost ($): " + calcCost(tripItems))
        print("\nCategories: " + calcCategories(tripItems))
        print("-----------------------------------\n")

if __name__ == "__main__":
    main()
