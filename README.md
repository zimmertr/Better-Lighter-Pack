# Better Ligher Pack

## Summary

I was frustrated with https://ligherpack.com so I made this. 

<hr>

## Instructions

1. Create CSV following this format in `trips/`:
   ```csv
   Description: 	name,description,quantity,weight,unit,url,price,worn,consumable
   Data Type:		string,string,integer,float,integer,string,decimal,boolean,boolean
   Requirement: 	optional,optional,required,required,n/a,n/a,required,optional,optional
   ```

2. Execute script against directory:
   ```shell
   # With Python
   ./python main.py trips/
   
   # With Docker
   ./docker run -it $(docker build -q .)
   ```

<hr>

## Example:

```shell
Dir: /Users/tj/git/personal/BetterLighterPack [main] U
Usr: tj - Sat 25,  7:22PM > docker run -it $(docker build -q .)
Trip: Alpine_Lakes_Grand_Slam.csv

Items:
    Total: 96
    Base: 59
    Worn: 15
    Food: 22

Weight (lbs):
    Total: 11.39
    Base: 5.27
    Worn: 4.89
    Food: 1.24
    No Data: 36

Cost ($):
    Total: 5,168.36
    Base: 2,388.72
    Worn: 2,218.51
    Food: 561.13
    No Data: 36

Categories:
    Clothing: 7
    Electronics: 9
    Feet: 3
    Food: 22
    Hiking: 5
    Human Flaws: 6
    Kitchen: 9
    Medicine: 9
    Miscellaneous: 8
    Sanitation: 11
    Sleeping: 7
-----------------------------------

Trip: Desolation_Wilderness.csv

Items:
    Total: 61
    Base: 43
    Worn: 14
    Food: 4

Weight (lbs):
    Total: 8.11
    Base: 4.52
    Worn: 3.29
    Food: 0.3
    No Data: 23

Cost ($):
    Total: 3,679.30
    Base: 2,049.38
    Worn: 1,493.50
    Food: 136.42
    No Data: 23

Categories:
    Clothing: 6
    Electronics: 8
    Feet: 3
    Food: 4
    Hiking: 5
    Human Flaws: 3
    Kitchen: 6
    Medicine: 6
    Miscellaneous: 6
    Sanitation: 7
    Sleeping: 7
-----------------------------------

Trip: Wonderland.csv

Items:
    Total: 77
    Base: 62
    Worn: 15
    Food: 0

Weight (lbs):
    Total: 9.75
    Base: 5.21
    Worn: 4.54
    Food: 0.0
    No Data: 33

Cost ($):
    Total: 4,421.29
    Base: 2,362.48
    Worn: 2,058.81
    Food: 0
    No Data: 33

Categories:
    Clothing: 7
    Electronics: 11
    Feet: 3
    Hiking: 4
    Human Flaws: 6
    Kitchen: 8
    Medicine: 10
    Miscellaneous: 9
    Sanitation: 12
    Sleeping: 7
-----------------------------------
```



