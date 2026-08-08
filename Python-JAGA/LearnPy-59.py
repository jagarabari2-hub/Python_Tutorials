print()
print("|========================================|"
      "| INSERT DATA INTO TABLE "
      "||========================================|")
print()
import pymysql
con = pymysql.connect(
    host="localhost",
    user="Jaga",
    password="jaga@123",
    database="python"
)
print("Connection Successful")
cmd = con.cursor()
cmd.execute("INSERT INTO customer (Name, Contact) VALUES ('PHP', 'SCRIPT')")
con.commit()
con.close()       