print()
print("|========================================|"
      "| Updating Data into table "
      "||========================================|")
print()
import pymysql
con = pymysql.connect(
    host="localhost",
    user="Jaga",
    password="jaga@123",
    database="python"
)

print("Connected Successfully")
cmd = con.cursor()
try:
    cmd.execute("update student set Name='Jaga Rabari' where id=1")
    con.commit()
    print("Data Updated Successfully")
except Exception as e:
    print("Error: ", e)
    con.rollback()          