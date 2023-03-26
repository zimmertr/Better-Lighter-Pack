import csv, os, sys
from decimal import *

TRIP_PATH=sys.argv[1] if len(sys.argv) > 1 else './trips/'
TABULATION="\n    "


def parseCSV(file):
    with open(file, "r") as csvFile:
        csvData = list(csv.reader(csvFile))
    return csvData


def calcTotals(tripItems):
    base=0
    worn=0
    food=0

    for item in tripItems:
        isWorn = item[8].lower()
        isFood = item[9].lower()

        worn += bool(isWorn)
        food += bool(isFood)
        base += not isWorn and not isFood

    return ( "\n" +
        f"    Total:   {len(tripItems)}\n"
        f"    Base:    {base}\n"
        f"    Worn:    {worn}\n"
        f"    Food:    {food}"
    )


def calcWeight(tripItems):
    base=0
    worn=0
    food=0
    nullValues=0

    for item in tripItems:
        quantity = item[3]
        value = item[4]
        isWorn = item[8].lower()
        isFood = item[9].lower()

        if quantity and value:
            if isWorn != "":
                worn += int(quantity) * float(value)
            elif isFood != "":
                food += int(quantity) * float(value)
            else:
                base += int(quantity) * float(value)
        else:
            nullValues += 1

    total = base + worn + food

    return ( 
        TABULATION + f"Total:   {gramsToLBS(total)}lbs"
        + TABULATION + f"Base:    {gramsToLBS(base)}lbs"
        + TABULATION + f"Worn:    {gramsToLBS(worn)}lbs"
        + TABULATION + f"Food:    {gramsToLBS(food)}lbs"
        + nullValueFormat(nullValues)
    )


def calcCost(tripItems):
    total=0
    base=0
    worn=0
    food=0
    nullValues=0

    for item in tripItems:
        quantity = item[3]
        value = item[7]
        isWorn = item[8].lower()
        isFood = item[9].lower()

        if quantity and value:
            if isWorn:
                worn += int(quantity) * Decimal(value)
            elif isFood:
                food += int(quantity) * Decimal(value)
            else:
                base += int(quantity) * Decimal(value)
        else:
            nullValues += 1

        total = base + worn + food

    return (
        TABULATION + f"Total:   ${total:,.2f}"
        + TABULATION + f"Base:    ${base:,.2f}"
        + TABULATION + f"Worn:    ${worn:,.2f}"
        + TABULATION + f"Food:    ${food:,.2f}"
        + nullValueFormat(nullValues)
    )


def calcCategories(tripItems):
    tmpList={}
    resultList = ""
    nullValues=0

    for item in tripItems:
        category = item[1]
        weight=item[4]
        cost=item[7]        
        
        if category not in tmpList:
            tmpList[category] = {"count": 1, "weight": 0, "value": 0}
        else:
            tmpList[category]["count"] += 1

        if weight:
            tmpList[category]["weight"] += float(weight)
        if cost:
            tmpList[category]["value"] += Decimal(cost)

    for category, info in tmpList.items():
        resultList += TABULATION + f"{category}: {info['count']}"
        resultList += f"\n        Weight:   {gramsToLBS(info['weight'])}lbs"
        resultList += f"\n        Value:    ${info['value']:,.2f}"

    return resultList


def gramsToLBS(grams):
    return format(float(grams) / 453.59237, ".2f")


def nullValueFormat(value):
    if value and value > 0:
        return f"{TABULATION}\033[91mNo Data: {value}\033[0m"
    return ""


def buildTripList(TRIP_PATH):
    if os.path.isdir(TRIP_PATH):
        return [(file, parseCSV(TRIP_PATH + file)) for file in os.listdir(TRIP_PATH)]
    elif os.path.isfile(TRIP_PATH):
        return [(TRIP_PATH, parseCSV(TRIP_PATH))]


def calculateTrip(trip):
    tripName, tripItems = trip
    print("Trip: " + tripName)
    print("\nTotal Items: " + calcTotals(tripItems))
    print("\nTotal Weight: " + calcWeight(tripItems))
    print("\nTotal Cost: " + calcCost(tripItems))
    print("\nTotal Categories: " + calcCategories(tripItems))
    print("-----------------------------------\n")


def main():
    listOfTrips = buildTripList(TRIP_PATH)

    for trip in listOfTrips:
        calculateTrip(trip)


if __name__ == "__main__":
    main()
