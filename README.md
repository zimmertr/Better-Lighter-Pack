# Better Ligher Pack

## Summary

I was frustrated with https://lighterpack.com so I made this CLI tool. Your exported ligherpack CSVs should be compatible. 

<hr>

## Instructions

1. Create a CSV file following this format. Reference examples in `./trips/` if necessary:
   ```csv
   Description: 	name,description,quantity,weight,unit,url,price,worn,consumable
   Data Type:   	string,string,integer,float,integer,string,decimal,string,string
   Requirement: 	optional,optional,required,required,n/a,n/a,required,optional,optional
   Example: 	Sun Hat,Clothing,Outdoor Research Sombriolet,1,107.73,g,https://www.rei.com/product/112247/outdoor-research-sombriolet-sun-hat?sku=1122470011,31.49,Worn,
   ```
   
2. Execute the script against a CSV file or directory containing CSV files:
   ```shell
   # With Python
   ./python main.py trips/Alpine_Lakes_Grand_Slam.csv
   
   # With Python
   ./python main.py trips/
   
   # With Docker
   ./docker run -it $(docker build -q .)
   ```

<hr>

## Example:

```shell
$> python main.py trips/Alpine_Lakes_Grand_Slam.csv
Trip: trips/Alpine_Lakes_Grand_Slam.csv

Total Items:
    Total:   96
    Base:    59
    Worn:    15
    Food:    22

Total Weight:
    Total:   34.08lbs
    Base:    19.04lbs
    Worn:    5.73lbs
    Food:    9.32lbs
    No Data: 20

Total Cost:
    Total:   $5,168.36
    Base:    $2,388.72
    Worn:    $2,218.51
    Food:    $561.13
    No Data: 36

Total Categories:
    Clothing: 7
        Weight:   3.4lbs
        Value:    $349.42
    Electronics: 9
        Weight:   2.41lbs
        Value:    $2,160.90
    Feet: 3
        Weight:   1.59lbs
        Value:    $136.70
    Food: 22
        Weight:   5.28lbs
        Value:    $224.01
    Hiking: 5
        Weight:   5.37lbs
        Value:    $349.92
    Human Flaws: 6
        Weight:   0.08lbs
        Value:    $104.28
    Kitchen: 9
        Weight:   2.32lbs
        Value:    $363.20
    Medicine: 9
        Weight:   1.55lbs
        Value:    $21.16
    Miscellaneous: 8
        Weight:   0.41lbs
        Value:    $43.21
    Sanitation: 11
        Weight:   0.11lbs
        Value:    $7.99
    Sleeping: 7
        Weight:   6.39lbs
        Value:    $921.53
-----------------------------------
```



