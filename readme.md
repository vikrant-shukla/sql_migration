# Data Migration from different sources 

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)


## About <a name = "about"></a>

Assignment:  dump the data from excel sheets and csv file from database and used Python language to create this scripts and used pandas lib.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See 

### Prerequisites

What things you need to install the software and how to install them.

```
Python
Pandas
Openpyxl
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Install the requirements.txt file for dependencies. run the below command: 
```
create virtual env : virtualenv venv

activate the env : 
for macos and linux : source venv/bin/activate
for windows :  venv/Scripts/activate

pip3 install -r requirements.txt
```
## Further Steps
Run the driver file : In this file there is two files one is csv and another is excel. Uncomment one file and run the driver.py data will be stored in side the sqlite database.

### Command to run the driver.py file

```
python3 driver.py
```

Check the data is stored or not : open the check_data.py file , there is flag and its values is "all" , "limit" (by default the limit is 1 you can change it), "count", "table_data" (to check which table is created). And in tablename there is all tables mentioned you have to pass the tablename using indexing along with cursor , flag and limit. you will get the records in console
