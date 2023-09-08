import pandas as pd

def read_file(filename, cursor, sqliteConnection):
    """Read the excel and csv file and also create the columns in table dynamically 
    in sqlite db and dump the data into tables"""

    splitted_filename = filename.split(".")[-1]
    excel_file = filename
    splitted = excel_file.split(".")[0].split("/")[-1]

    if splitted_filename == 'csv':
        df = pd.read_csv(excel_file)
        tableList = cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table'
                         AND name='{splitted}'; """).fetchall()
        if tableList == []:
            query = create_table(df,splitted )
            cursor.execute(query)
        data  =  data_dump(df, splitted ,sqliteConnection)

    if splitted_filename == "xls" or splitted_filename == 'xlsx':
        xls_file = pd.ExcelFile(excel_file)
        for splitted in xls_file.sheet_names:
            df = pd.read_excel(excel_file, sheet_name=splitted)
            tableList = cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='table'
                         AND name='{splitted}'; """).fetchall()
            if tableList == []:
                query = create_table(df,splitted )
                cursor.execute(query)
            data  =  data_dump(df, splitted ,sqliteConnection)

    if data.get("msg"):
        print(data.get("msg"))
    else:
        print("data dump successfully")
    return splitted, df

def create_table(df, file_name):
    """creation of table and columns based on file columns"""

    table_name = file_name
    columns = []

    for col_name in df.columns:
        
        data_type = df[col_name].dtype

        if 'int' in str(data_type):
            sql_type = 'INTEGER'
        elif 'float' in str(data_type):
            sql_type = 'REAL'
        elif 'object' in str(data_type):
            sql_type = 'TEXT'
        else:
            sql_type = 'TEXT'
        col_name = str(col_name).replace(" ", "_") 
        columns.append(f'{col_name} {sql_type}')
        
    create_table_sql = f'CREATE TABLE {table_name} ({", ".join(columns)});'
    return create_table_sql

def data_dump(df, table_name,sqliteConnection ):
    """Data will be stored in tables"""
    try:
        df.to_sql(table_name, sqliteConnection , if_exists='replace', index=False)
        return {"success":True }
    except Exception as e:
        return {"msg":e}        
    
def check(cursor, tableName, flag, limit):
    """Queries to perform in tables"""
    
    try :
        if flag == "all":
            data =  cursor.execute(f"select * from {tableName};").fetchall()
        if flag == "limit":
            data =  cursor.execute(f"select * from {tableName} limit {limit};").fetchall()
        if flag == "count":
            data_count =  cursor.execute(f"select count(*) from {tableName};").fetchone()
            data = data_count[0]
        if flag == "table_data":
            data = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        return data
    except Exception as e:
        return e