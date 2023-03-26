# Better Ligher Pack

## Summary

I was frustrated with https://ligherpack.com so I made this. Your exported ligherpack CSVs should be compatible. 

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
   ./python main.py trips/
   
   # With Docker
   ./docker run -it $(docker build -q .)
   ```

<hr>

## Example:

```shell
$> python main.py trips/Alpine_Lakes_Grand_Slam.csv
Trip: trips/Alpine_Lakes_Grand_Slam.csv

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
```



