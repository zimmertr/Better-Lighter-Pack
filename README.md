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
    Total: 34.08
    Base: 19.04
    Worn: 5.73
    Food: 9.32
    No Data: 20

Cost ($):
    Total: 5,168.36
    Base: 2,388.72
    Worn: 2,218.51
    Food: 561.13
    No Data: 36

Categories:
    Clothing: 7
	Weight:	3.4
	Value:	349.42
    Electronics: 9
	Weight:	2.41
	Value:	2160.90
    Feet: 3
	Weight:	1.59
	Value:	136.70
    Food: 22
	Weight:	5.28
	Value:	224.01
    Hiking: 5
	Weight:	5.37
	Value:	349.92
    Human Flaws: 6
	Weight:	0.08
	Value:	104.28
    Kitchen: 9
	Weight:	2.32
	Value:	363.20
    Medicine: 9
	Weight:	1.55
	Value:	21.16
    Miscellaneous: 8
	Weight:	0.41
	Value:	43.21
    Sanitation: 11
	Weight:	0.11
	Value:	7.99
    Sleeping: 7
	Weight:	6.39
	Value:	921.53
-----------------------------------
```



