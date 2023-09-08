from functionalities import check
from sql_con import close, connection

cursor , sqliteConnection = connection()

flag, limit = "all", 1
tablename = [ 'govt_data', 'govt_data2', "csv_file"]
data  = check(cursor, tablename[1], flag, limit)
print(data)

close(sqliteConnection)