# Data Migration from different sources 

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)


## About <a name = "about"></a>

Assignment:  Dump the data from Excel sheets and CSV files to  a database and use Python to create these scripts and use pandas lib.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing. See 

### Prerequisites

What things do you need to install the software and how to install them?

```
Python
Pandas
Openpyxl
```

### Installing

A step-by-step series of examples that tell you how to get a development environment running.

Install the requirements.txt file for dependencies. run the below command: 
```
create virtual env : virtualenv venv

activate the env : 
For macOS and Linux: source venv/bin/activate
For Windows:  venv/Scripts/activate

pip3 install -r requirements.txt
```
## Further Steps
Run the driver file: In this file, there are two files one is CSV and another is Excel. Uncomment one file and run the driver.py data will be stored inside the SQLite database.

### Command to run the driver.py file

```
python3 driver.py
```

Check whether the data is stored or not: open the check_data.py file, there is  a flag variable and its values are "all", "limit" (by default the limit is 1 you can change it), "count", "table_data" (to check which table is created). And in tablename there is all tables mentioned you have to pass the table name using indexing along with cursor, flag and limit. you will get the records in the console
