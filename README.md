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

Category     Count
----------  -------
Base          59
Worn          15
Food          22
Total         96

Category     Weight (lbs)
----------  --------------
Base            19.04
Worn             5.73
Food             9.32
Total           34.08
No Data: 20

Category    Value
----------  ---------
Base        $2,388.72
Worn        $2,218.51
Food        $561.13
Total       $5,168.36
No Data: 36

Category        Count    Weight (lbs)   Value
-------------  -------  --------------  ---------
Clothing          7          3.4        $349.42
Electronics       9          2.41       $2,160.90
Feet              3          1.59       $136.70
Food             22          5.28       $224.01
Hiking            5          5.37       $349.92
Human Flaws       6          0.08       $104.28
Kitchen           9          2.32       $363.20
Medicine          9          1.55       $21.16
Miscellaneous     8          0.41       $43.21
Sanitation       11          0.11       $7.99
Sleeping          7          6.39       $921.53
```



