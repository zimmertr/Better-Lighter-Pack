import csv, os, sys
from decimal import *
from tabulate import tabulate
from collections import defaultdict

TRIP_PATH = sys.argv[1] if len(sys.argv) > 1 else './trips/'
TABULATION = "\n    "


def parseCSV(file):
    with open(file, "r") as csvFile:
        csvData = list(csv.reader(csvFile))
    return csvData


def calcTotals(tripItems):
    base = 0
    worn = 0
    food = 0

    for item in tripItems:
        isWorn = item[8].lower()
        isFood = item[9].lower()

        worn += bool(isWorn)
        food += bool(isFood)
        base += not isWorn and not isFood

    table = [
        ["Base", base],
        ["Worn", worn],
        ["Food", food],
        ["Total", len(tripItems)]
    ]

    headers = ["Category", "Count"]
    return tabulate(table, headers=headers, tablefmt="simple", numalign="center")


def calcWeight(tripItems):
    base = 0
    worn = 0
    food = 0
    nullValues = 0

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

    table = [
        ["Base", gramsToLBS(base)],
        ["Worn", gramsToLBS(worn)],
        ["Food", gramsToLBS(food)],
        ["Total", gramsToLBS(total)]
    ]

    headers = ["Category", "Weight (lbs)"]
    return tabulate(table, headers=headers, tablefmt="simple", numalign="center") + nullValueFormat(nullValues)


def calcCost(tripItems):
    base = 0
    worn = 0
    food = 0
    nullValues = 0

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

    table = [
        ["Base", "${:,.2f}".format(base)],
        ["Worn", "${:,.2f}".format(worn)],
        ["Food", "${:,.2f}".format(food)],
        ["Total", "${:,.2f}".format(total)]
    ]

    headers = ["Category", "Value"]
    return tabulate(table, headers=headers, tablefmt="simple", numalign="center") + nullValueFormat(nullValues)


def calcCategories(tripItems):
    tmpList = defaultdict(lambda: {"count": 0, "weight": 0, "value": 0})
    table = []

    for item in tripItems:
        category = item[1]
        weight = item[4]
        cost = item[7]

        tmpList[category]["count"] += 1
        tmpList[category]["weight"] += float(weight or 0)
        tmpList[category]["value"] += Decimal(cost or 0)

    for category, info in tmpList.items():
        count = info['count']
        weight = gramsToLBS(info['weight'])
        value = "${:,.2f}".format(info['value'])
        table.append([category, count, weight, value])

    headers = ["Category", "Count", "Weight (lbs)", "Value"]
    return tabulate(table, headers=headers, tablefmt="simple", numalign="center")


def gramsToLBS(grams):
    return format(float(grams) / 453.59237, ".2f")


def nullValueFormat(value):
    if value and value > 0:
        return f"\n\033[91mNo Data: {value}\033[0m"
    return ""


def buildTripList(TRIP_PATH):
    if os.path.isdir(TRIP_PATH):
        return [(file, parseCSV(TRIP_PATH + file)) for file in os.listdir(TRIP_PATH)]
    elif os.path.isfile(TRIP_PATH):
        return [(TRIP_PATH, parseCSV(TRIP_PATH))]


def calculateTrip(trip):
    tripName, tripItems = trip
    print("Trip: " + tripName + "\n")
    print(calcTotals(tripItems) + "\n")
    print(calcWeight(tripItems) + "\n")
    print(calcCost(tripItems) + "\n")
    print(calcCategories(tripItems) + "\n")


def main():
    listOfTrips = buildTripList(TRIP_PATH)

    for trip in listOfTrips:
        calculateTrip(trip)
        if len(listOfTrips) > 1:
            print("********************************************************\n")            


if __name__ == "__main__":
    main()
