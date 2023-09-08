from functionalities import  read_file
from sql_con import connection, close

cursor , sqliteConnection = connection()

# filename = 'files/csv_file.csv'
filename = "files/Financial_data.xlsx"
splitted, df = read_file(filename, cursor, sqliteConnection)

close(sqliteConnection)
