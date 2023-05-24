import mysql.connector


mysql_database = mysql.connector.connect(
    host ="localhost",
    user = "avant",
    password = "root"
)

print(mysql_database)
cursorObject = mysql_database.cursor()

# cursorObject.execute("CREATE DATABASE avant_website")